from database.db_settings import Base
from sqlalchemy import Column, String, Boolean, text
from database.mixins import psql_primary_key_mixin, psql_timestamps_mixin


class TagvenueModel(
    Base,
    psql_primary_key_mixin.PsqlPrimaryKeyMixin,
    psql_timestamps_mixin.PsqlTimestampsMixin
):
    __tablename__ = 'tagvenue'

    title = Column(String(768), nullable=False, index=True, comment="Title of the venue")
    url = Column(String(255), unique=True, nullable=False, comment="URL of the venue")
    price = Column(String(length=255), nullable=False)
    delivered = Column(Boolean, default=False, nullable=False, server_default=text('FALSE'))
