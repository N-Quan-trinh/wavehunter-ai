from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from datetime import datetime

class FireAntScraper:
    """Simple FireAnt.vn scraper"""
    
    def __init__(self, headless=True):
        self.headless = headless
        self.driver = None
    
    def setup_driver(self):
        """Setup Chrome driver"""
        try:
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("Chrome driver setup completed successfully")
            return True
        except Exception as e:
            print(f"Failed to setup Chrome driver: {str(e)}")
            return False
    
    def navigate_to_stock(self, stock_symbol):
        """Navigate to stock page"""
        try:
            url = f"https://fireant.vn/ma-chung-khoan/{stock_symbol}"
            print(f"Navigating to {url}")
            self.driver.get(url)
            print("Page loaded successfully")
            return True
        except Exception as e:
            print(f"Failed to navigate: {str(e)}")
            return False
    
    def wait_for_content(self, wait_time=60):
        """Wait for page content to load"""
        print(f"Waiting {wait_time} seconds for content to load...")
        time.sleep(wait_time)
        print("Wait completed")
    
    def extract_stock_data(self, stock_symbol):
        """Extract stock data from the page"""
        try:
            print(f"Searching for {stock_symbol} data...")
            
            # Setup driver
            if not self.setup_driver():
                return {}
            
            # Navigate to stock page
            if not self.navigate_to_stock(stock_symbol):
                return {}
            
            # Wait for content to load
            self.wait_for_content(60)
            
            # Extract data
            stock_data = {}
            
            # Get current price (usually the main price display)
            try:
                price_elements = self.driver.find_elements(By.TAG_NAME, "span")
                for element in price_elements:
                    text = element.text.strip()
                    if text and any(c.isdigit() for c in text) and '.' in text:
                        # This might be a price
                        try:
                            float(text)
                            stock_data['current_price'] = text
                            print(f"Current price: {text}")
                            break
                        except:
                            continue
            except Exception as e:
                print(f"Could not find current price: {str(e)}")
            
            # Get additional data if available
            try:
                # Look for any table data
                tables = self.driver.find_elements(By.TAG_NAME, "table")
                print(f"Found {len(tables)} tables")
                
                for table in tables:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    for row in rows:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 2:
                            label = cells[0].text.strip()
                            value = cells[1].text.strip()
                            if label and value:
                                stock_data[label] = value
                                print(f"{label}: {value}")
            except Exception as e:
                print(f"Could not extract table data: {str(e)}")
            
            return stock_data
            
        except Exception as e:
            print(f"Failed to extract stock data: {str(e)}")
            return {}
        finally:
            if self.driver:
                self.driver.quit()
                print("Chrome driver closed")
    
    def save_data(self, stock_data, stock_symbol):
        """Save data to JSON file"""
        try:
            if not stock_data:
                print("No data to save")
                return
            
            # Create data structure
            data = {
                "stock_symbol": stock_symbol,
                "timestamp": datetime.now().isoformat(),
                "data": stock_data
            }
            
            # Save to file
            filename = f"{stock_symbol.lower()}_data.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"Data saved to {filename}")
            
            # Display the data
            print("\n📊 Extracted Data:")
            print("=" * 50)
            for key, value in stock_data.items():
                print(f"{key}: {value}")
            print("=" * 50)
            
        except Exception as e:
            print(f"Failed to save data: {str(e)}")

def main():
    """Main function"""
    scraper = FireAntScraper(headless=True)
    stock_symbol = "VNM"  # Default stock
    
    # Extract data
    stock_data = scraper.extract_stock_data(stock_symbol)
    
    # Save data
    scraper.save_data(stock_data, stock_symbol)

if __name__ == "__main__":
    main() 