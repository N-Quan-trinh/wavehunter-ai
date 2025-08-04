#!/usr/bin/env python3
"""
FireAnt Stock Scraper - Main Entry Point
"""

import sys
import os
import argparse

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scrapers.fireant_scraper import FireAntScraper

def main():
    """Main function"""
    # Parse arguments
    parser = argparse.ArgumentParser(description='FireAnt Stock Scraper')
    parser.add_argument('--symbol', '-s', default='VNM', help='Stock symbol (default: VNM)')
    parser.add_argument('--wait', '-w', type=int, default=60, help='Wait time in seconds (default: 60)')
    args = parser.parse_args()
    
    stock_symbol = args.symbol.upper()
    wait_time = args.wait
    
    print(f" FireAnt Stock Scraper")
    print(f" Stock: {stock_symbol}")
    print(f"  Wait time: {wait_time} seconds")
    print("=" * 50)
    
    # Create scraper
    scraper = FireAntScraper(headless=True)
    
    # Extract data
    stock_data = scraper.extract_stock_data(stock_symbol)
    
    # Save data
    scraper.save_data(stock_data, stock_symbol)
    
    if stock_data:
        print(f"✅ Successfully scraped data for {stock_symbol}")
    else:
        print(f"❌ No data found for {stock_symbol}")

if __name__ == "__main__":
    main() 