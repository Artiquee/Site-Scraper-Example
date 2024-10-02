# MAIN LOGIC
import queue
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from database.commands import bulk_add_to_db, check_if_exists
from selectolax.parser import Node
from database.db_settings import get_db
from scraper.tagvenue_scraper import TagvenueSingleItem
from items.tagvenue_item import TagvenueItem
from utils.get_html import get_html
from utils.logger import logger
from database.models.tagvenue_model import TagvenueModel


class Scraper:
    def __init__(self):
        self.queue = queue.Queue(maxsize=100)  # edit max size
        self.db = next(get_db())
        self.total_items = 0

    @staticmethod
    def get_urls() -> list[Node]:
        """Fetch and filter URLs from the sitemap."""
        html = get_html("https://www.tagvenue.com/sitemap-rooms")
        urls = html.css('loc')

        # Filter out existing URLs
        new_urls = [url for url in urls if not check_if_exists(TagvenueModel, url=url.text())]

        logger.info(f"Found {len(urls)} URLs, {len(new_urls)} new URLs.")
        return new_urls[:1000]

    @staticmethod
    def get_single_page(url: str) -> TagvenueItem:
        """Scrape a single page and return a TagvenueItem."""
        page = get_html(url)
        items = TagvenueSingleItem(html_page=page)

        return TagvenueItem(
            title=items.get_title(),
            url=url,
            price=items.get_price()
        )

    def main(self, url: Node):
        """Main scraping logic."""
        try:
            item = self.get_single_page(url.text())
            self.queue.put(item)
            self.total_items += 1

            if self.queue.full():
                items_to_db = [self.queue.get() for _ in range(self.queue.qsize())]
                bulk_add_to_db(items_to_db, TagvenueModel)
                logger.info(f"{self.total_items} Items added to DB.")
        except Exception as e:
            logger.error(f"Error processing URL {url.text()}: {e}")


if __name__ == '__main__':
    START_SCRAPING = datetime.now()
    logger.info(f"[START] {START_SCRAPING}")
    scraper = Scraper()
    urls = scraper.get_urls()

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(scraper.main, urls)

    if not scraper.queue.empty():
        items_to_db = [scraper.queue.get() for _ in range(scraper.queue.qsize())]
        bulk_add_to_db(items_to_db, TagvenueModel)
    logger.info(f"[FINISH] - {datetime.now() - START_SCRAPING} - WORK TIME")
