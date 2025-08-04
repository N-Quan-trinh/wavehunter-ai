# FireAnt Stock Scraper

A simple web scraper for extracting stock data from FireAnt.vn

## Features

- ✅ Connects to FireAnt.vn successfully
- ✅ Waits for page content to load (configurable wait time)
- ✅ Extracts current price and table data
- ✅ Saves data to JSON files
- ✅ Headless browser support

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python3 main.py
```

### With Custom Stock Symbol
```bash
python3 main.py --symbol VNM
```

### With Custom Wait Time
```bash
python3 main.py --symbol VNM --wait 120
```

### Command Line Options
- `--symbol, -s`: Stock symbol (default: VNM)
- `--wait, -w`: Wait time in seconds (default: 60)

## Output

The scraper will:
1. Connect to the FireAnt.vn website
2. Navigate to the specified stock page
3. Wait for content to load
4. Extract available data
5. Save to a JSON file (e.g., `vnm_data.json`)
6. Display the extracted data

## Project Structure

```
data processing/
├── main.py                 # Main entry point
├── scrapers/
│   └── fireant_scraper.py  # Main scraper class
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Example Output

```
🚀 FireAnt Stock Scraper
📈 Stock: VNM
⏱️  Wait time: 60 seconds
==================================================
Chrome driver setup completed successfully
Navigating to https://fireant.vn/ma-chung-khoan/VNM
Page loaded successfully
Waiting 60 seconds for content to load...
Wait completed
Current price: 60.40
Found 2 tables
Tham chiếu: 60.00
Mở cửa: 59.80
Data saved to vnm_data.json

📊 Extracted Data:
==================================================
current_price: 60.40
Tham chiếu: 60.00
Mở cửa: 59.80
==================================================
✅ Successfully scraped data for VNM
``` 