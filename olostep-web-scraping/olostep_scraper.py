
import os
import threading
from getpass import getpass

from olostep import Olostep, Olostep_BaseError

# 1. Set up Olostep client

api_key = os.getenv("OLOSTEP_API_KEY") or getpass("Olostep API key: ")
client = Olostep(api_key=api_key)


# 2. Scrape a page to Markdown

def scrape_markdown(url):
    page = client.scrapes.create(
        url_to_scrape=url,
        formats=["markdown"],
    )

    print("Credits used:", page.credits_consumed)
    print(page.markdown_content[:400])
    return page


# 3. Choose output formats

def scrape_all_formats(url):
    page = client.scrapes.create(
        url_to_scrape=url,
        formats=["html", "markdown", "text"],
    )

    print("Credits used:", page.credits_consumed)
    print("HTML characters:", len(page.html_content))
    print("Markdown characters:", len(page.markdown_content))
    print("Text characters:", len(page.text_content))

    return page


# 4. Scrape JavaScript-rendered pages

def scrape_javascript(url):
    page = client.scrapes.create(
        url_to_scrape=url,
        formats=["markdown"],
        wait_before_scraping=2000,
    )

    print(page.markdown_content[:500])
    return page


# 5. Scrape with browser actions

def scrape_with_actions(url):
    page = client.scrapes.create(
        url_to_scrape=url,
        formats=["markdown"],
        actions=[
            {"type": "wait", "milliseconds": 1500},
            {"type": "scroll", "direction": "down", "amount": 1000},
        ],
    )

    print(page.markdown_content[:500])
    return page


# 6. Handle scraping errors

def custom_thread_excepthook(args):
    error = str(args.exc_value)

    if "RequestValidationFailed" in error or "ValidationError" in error:
        return

    threading.__excepthook__(args)


threading.excepthook = custom_thread_excepthook


def safe_scrape(url):
    try:
        page = client.scrapes.create(
            url_to_scrape=url,
            formats=["markdown"],
        )

        print("Credits used:", page.credits_consumed)
        return page

    except (Olostep_BaseError, KeyError) as error:
        print(f"Skipped {url}: {error}")
        return None


# 7. Run examples

def main():
    print("Starting Olostep Web Scraper")

    print("\nMarkdown scraping")
    scrape_markdown("https://books.toscrape.com/")

    print("\nMultiple output formats")
    scrape_all_formats("https://books.toscrape.com/")

    print("\nJavaScript scraping")
    scrape_javascript("https://quotes.toscrape.com/js/")

    print("\nBrowser actions")
    scrape_with_actions("https://quotes.toscrape.com/js/")

    print("\nError handling")
    safe_scrape("not-a-url")

    print("\nScraping completed!")


if __name__ == "__main__":
    main()
