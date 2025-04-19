"""DB session for database operations"""

from sqlalchemy.exc import IntegrityError as SQLAlchemyIntegrityError

from app.db.custom_exceptions import IntegrityError
from app.db.sqlalchemy_adapter import get_session, init_db


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

    def create(self, obj, save=True):
        try:
            self.db.add(obj)

            if save:
                self.save_changes()
                self.db.refresh(obj)

            return obj
        except SQLAlchemyIntegrityError as e:
            raise IntegrityError(str(e))

    def update(self, obj, new_data, save=True):
        [setattr(obj, key, value) for key, value in new_data.items()]

        if save:
            self.save_changes()

        return obj

    def delete(self, obj, save=True):
        self.db.delete(obj)

        if save:
            self.save_changes()
        return True

    def save_changes(self):
        try:
            self.db.commit()
        except SQLAlchemyIntegrityError as e:
            raise IntegrityError(str(e))

    def get_top_words(self, table, count_field, limit, skip):
        count_field = getattr(table, count_field)
        skip_words = skip if skip else [""]
        query = self.db.query(table).filter(table.id.notin_(skip_words)).order_by(count_field.desc()).limit(limit)
        return query.all()


def get_db():
    init_db()
    db = get_session()
    try:
        db_client = DBClient(db)
        yield db_client
    finally:
        db.close()
