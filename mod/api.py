import sqlalchemy as sa
from .db import SqlAlchemyBase

class Group(SqlAlchemyBase):
    __tablename__ = 'groups'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    data = sa.Column(sa.String, nullable=True)
    link = sa.Column(sa.String, nullable=True)
    messages = sa.Column(sa.String, nullable=True)
    users = sa.Column(sa.String, nullable=True)

class User(SqlAlchemyBase):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, nullable=True)
    date = sa.Column(sa.String, nullable=True)
    friends = sa.Column(sa.String, nullable=True)
    data = sa.Column(sa.String, nullable=True)