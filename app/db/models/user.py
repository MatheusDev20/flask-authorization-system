from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.dialects.postgresql import UUID

from app.db import db
from app.db.enums.role import Roles

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    admin = db.Column(db.Boolean(), default=False, nullable=False)
    role = db.Column(pgEnum(Roles), nullable=False, default='operation')
    avatar = db.Column(db.String(200), nullable=False)
    user_uuid = db.Column(UUID(as_uuid=True), nullable=False)
    extra_info = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return f'<User {self.username!r}>'
