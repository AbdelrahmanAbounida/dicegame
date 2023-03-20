
from app.extensions import db 
from sqlalchemy.types import TypeDecorator
from sqlalchemy import DateTime
import datetime
import pytz 

# custom dataType for sqlalchemy

tzaware_datetime = datetime.datetime.now(pytz.utc)

class AwareDataTime(TypeDecorator):
    impl = DateTime(timezone=True)

    def process_bind_param(self,value,dialect):
        if isinstance(value, datetime.datetime) and value.tzinfo is None:
            raise ValueError(f"{value} must be TZ-aware")
        return value

    def __repr__(self):
        return 'AwareDateTime()'

# Write custom mixin for user
class ResourceMixin():
    created_on = db.Column(AwareDataTime(),default=tzaware_datetime) # when a record is created 
    updated_on = db.Column(AwareDataTime(),default=tzaware_datetime,onupdate=tzaware_datetime) # when a record is updated

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        if self.username:
            return self.username
        return self.email
