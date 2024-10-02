from concurrent.futures import ThreadPoolExecutor


def start_threading(urls, max_workers=10):
    """
    Decorator that starts a thread pool of workers.
    Use if needed.
    :param urls:
    :param max_workers:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                executor.map(func, urls)
        return wrapper
    return decorator
