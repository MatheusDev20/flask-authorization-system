from typing import Any

from app.db import db


class BaseDbOperations:
    def __init__(self, model: type) -> None:
        self.model = model

    def add(self, data: dict[str, Any]) -> None:
        if not isinstance(data, dict):
            return

        db.session.add(self.model(**data))
        db.session.commit()

    def get_by_email(self, email: str) -> dict[str, Any] | None:
        if not email:
            return None

        user_info = self.model.query.filter_by(email=email).first()

        if not user_info:
            return {"status": 404, "message": "User not found"}

        return {"status": 200, "message": "Success", "data": user_info}

    def get_all(self) -> list:
        return self.model.query.all()

    def exclude(self, user) -> dict[str, Any] | None:
        if not user:
            return None
        try:
            db.session.delete(user)
            db.session.commit()
            return {"status": 200, "message": "Success", "data": user}
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> dict[str, Any] | None:
        if not id:
            return None

        user_info = self.model.query.filter_by(id=id).first()
        return {"status": 200, "message": "Success", "data": user_info}
