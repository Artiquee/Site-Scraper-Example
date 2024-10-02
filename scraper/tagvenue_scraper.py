class TagvenueSingleItem:
    """
    A class used to parse specific details from a Site HTML page.

    This class extracts structured data from the provided HTML page, such as
    room title and price. It can be easily extended with additional methods
    to parse more elements as needed.

    Attributes:
    ----------
    html_page : Node
        Parsed HTML content (using Selectolax) representing a Site page.

    Methods:
    -------
    get_title() -> str
        Extracts and returns the product/item title from the HTML.

    get_price() -> str
        Extracts and returns the product/item price from the HTML.

    # Add new methods below to extend functionality.
    """

    def __init__(self, html_page):
        self.html_page = html_page

    def get_title(self):
        """
        Extract the room title from the HTML page.

        :return: A string containing the room title.
        """
        return self.html_page.css_first('h1.room__name').text(strip=True)

    def get_price(self):
        """
        Extract the room price from the HTML page.

        :return: A string containing the room price.
        """
        return self.html_page.css_first('span.c-pricing-table__price_value').text(strip=True)
