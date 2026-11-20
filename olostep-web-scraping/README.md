
# Olostep Web Scraper

A Python web scraping project using the Olostep SDK.

Read the tutorial on freeCodeCamp: [How to Scrape Websites in Python with Olostep](https://www.freecodecamp.org/news/how-to-scrape-websites-in-python-with-olostep/)

## Features

- Scrape websites into Markdown
- Extract HTML, Markdown, and plain text
- Scrape JavaScript-rendered websites
- Perform browser actions such as scrolling and waiting
- Handle scraping errors

## Requirements

- Python 3.11+
- Olostep API key

## Installation

Install the required package:

    pip install olostep

## Setup

Get your API key from:

https://www.olostep.com/

The script will ask for your API key when you run it.

Alternatively, set the OLOSTEP_API_KEY environment variable.

## Run the Project

    python olostep_scraper.py

## Example Websites

- https://books.toscrape.com/
- https://quotes.toscrape.com/js/

## Project Structure

    olostep-project/
    ├── olostep_scraper.py
    └── README.md

## Notes

- Scraping consumes Olostep API credits.
- Check website terms of service and robots.txt before scraping.
- Only scrape data you are authorized to access.

