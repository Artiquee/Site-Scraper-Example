from pydantic import BaseModel


# Add all new fields for data validation.
class TagvenueItem(BaseModel):
    title: str
    url: str
    price: str
