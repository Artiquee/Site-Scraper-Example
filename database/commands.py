from sqlalchemy.dialects.postgresql import insert
from .db_settings import get_db


def add_to_db(data, model):
    """
    Add a new, single item to the database.
    :param data: Data from page as a dictionary
    :param model: SQLAlchemy model
    """
    session = next(get_db())
    try:
        item = model(**data)
        session.add(item)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def bulk_add_to_db(items: list, model):
    """
    Add multiple items to the database in bulk.
    :param items: List of items to add
    :param model: SQLAlchemy model
    """
    session = next(get_db())
    try:
        data_list = [item.dict() for item in items]
        session.execute(insert(model), data_list)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def update_db(data, model):
    """
    Update an existing item in the database.
    :param data: Data containing the updated values
    :param model: SQLAlchemy model
    """
    session = next(get_db())
    try:
        item = session.query(model).filter(model.id == data['id']).first()

        if item is None:
            raise ValueError('Item not found')

        for key, value in data.items():
            setattr(item, key, value)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def check_if_exists(model, **filters):
    """
    Check if a record exists in the database based on the provided filters.
    :param model: SQLAlchemy model
    :param filters: Dictionary of conditions to filter by (e.g., {'id': 1}, {'url': 'example.com'})
    :return: True if item exists, False otherwise
    """
    session = next(get_db())
    try:
        item = session.query(model).filter_by(**filters).first()
        return item is not None
    finally:
        session.close()


def get_all_undelivered(model):
    """
    Retrieve all undelivered products from the database.
    The retrieved records can then be exported
    to a CSV file or processed in another way.
    The 'delivered' column is used for tagging new data scraped after the last run.

    :param model: SQLAlchemy model
    :return:
    """
    session = next(get_db())
    try:
        return session.query(model).filter(model.delivered == False).all()
    finally:
        session.close()
