"""DB session for database operations"""

from sqlalchemy.exc import IntegrityError as SQLAlchemyIntegrityError

from app.db.custom_exceptions import IntegrityError
from app.db.sqlalchemy_adapter import get_session


class DBClient:
    def __init__(self, db_session):
        self.db = db_session

    def get_all(self, table):
        return self.db.query(table).all()

    def get_by_id(self, table, id):
        return self.db.query(table).filter(table.id == id).first()

    def get_by_unique_field(self, table, field, value):
        field = getattr(table, field)
        return self.db.query(table).filter(field == value).first()

    def create(self, obj):
        try:
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except SQLAlchemyIntegrityError as e:
            raise IntegrityError(str(e))

    def update(self, obj, new_data):
        new_data_dict = new_data.model_dump(exclude_unset=True)
        [setattr(obj, key, value) for key, value in new_data_dict.items()]
        try:
            self.db.commit()
            return obj
        except SQLAlchemyIntegrityError as e:
            raise IntegrityError(str(e))

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
        return True


def get_db():
    db = get_session()
    try:
        db_client = DBClient(db)
        yield db_client
    finally:
        db.close()
