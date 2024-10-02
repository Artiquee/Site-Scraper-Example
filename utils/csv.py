import csv
from database.commands import get_all_undelivered
from database.models.tagvenue_model import TagvenueModel
from utils.logger import logger


def export_csv():
    """
    Simple function to export a CSV file containing only new data.

    This function retrieves all undelivered items from the database
    and writes them to a CSV file named 'items.csv'. If there are
    no items to export, an informational log message is generated.

    :return: None
    """
    items = get_all_undelivered(TagvenueModel)
    if items:
        with open('items.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)
    else:
        logger.info("No data to export")
