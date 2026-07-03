# Car Data Extraction Tool with Excel/CSV/JSON Export

A Python Flask web scraping MVP for collecting car listing data from FINN.no, displaying the results in a simple web interface, and exporting the collected data to CSV, Excel, and JSON formats.

## Overview

This project demonstrates a basic but practical web scraping workflow:

1. Send a request to a car marketplace page.
2. Parse HTML content with BeautifulSoup.
3. Extract structured car listing data.
4. Display the results in a Flask web interface.
5. Export the data into common file formats.

The project was built as a portfolio MVP to show web scraping, data extraction, data cleaning, and file export skills.

## Features

- Scrapes car listings from FINN.no
- Extracts structured vehicle data
- Displays results in a simple web dashboard
- Exports scraped data to:
  - CSV
  - Excel
  - JSON
- Uses a clean Flask-based interface
- Separates scraping and file export logic into different modules

## Extracted Data

The scraper collects the following fields:

- Car name
- Price
- Year
- Mileage
- Driving range
- Image URL

## Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup
- lxml
- OpenPyXL
- HTML
- Bootstrap

## Project Structure

```
.
├── main.py
├── scrapper_finn_no.py
├── do_csv.py
├── do_excel.py
├── do_json.py
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Kerally/Car-Data-Extraction-Tool-with-Excel-CSV-JSON-Export.git
```

Go to the project folder:

```bash
cd Car-Data-Extraction-Tool-with-Excel-CSV-JSON-Export
```

Install dependencies:

```bash
pip install Flask requests beautifulsoup4 lxml openpyxl
```

## Usage

Run the Flask application:

```bash
python main.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000/
```

Use the web interface to:

1. Run the scraper.
2. View extracted car listings.
3. Download results as CSV, Excel, or JSON.

## Export Formats

### CSV

The CSV export is useful for spreadsheets, simple data analysis, and importing data into other tools.

### Excel

The Excel export provides a spreadsheet format that is easy to open, review, filter, and share.

### JSON

The JSON export is useful for APIs, databases, backend processing, and structured data storage.

## Possible Improvements

Future improvements could include:

- Search filters
- Database storage
- Pagination support
- Scheduled scraping
- Duplicate listing detection
- Better error handling
- Telegram or email notifications
- Deployment to a cloud platform

## Disclaimer

This project is created for educational and portfolio purposes. When scraping websites, always respect the website's terms of service, robots.txt rules, and applicable laws.

## Author

Created by [Kerally](https://github.com/Kerally)
