import time
from random import randint
from curl_cffi import requests
from selectolax.parser import HTMLParser
from fake_useragent import UserAgent
from utils.logger import logger

ua = UserAgent()


def get_html(url: str) -> HTMLParser:
    """
    Get html from url.
    :param url:
    :return HTMLParser:
    """
    try:
        resp = requests.get(url, impersonate="chrome", headers={'User-Agent': ua.random})
        time.sleep(randint(0, 1))
        if resp.status_code == 200:
            html = HTMLParser(resp.text)
            return html
        else:
            logger.info(f"[Error]: [{resp.status_code}] - {url}")
    except Exception as e:
        logger.info(f"[Error]: {e}")
