from sqlalchemy import Column, func

from api import db


class CRUDMixin(object):
    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True


class BaseModel(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, index = True)
    created_at = Column(db.DateTime(), server_default=func.now(), comment="创建时间")
    is_delete = Column(db.Boolean(), server_default=db.text("False"), comment="是否删除，True已删 False未删", index=True)
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
