from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql.functions import func
from sqlalchemy.dialects import mysql


base=declarative_base()

class Partner(base):
    __tablename__="partners"
    id = Column("id", mysql.INTEGER, primary_key=True, autoincrement=True)
    name = Column("name", String(100), primary_key=True)
    created = Column("created", DateTime, default=func.now(), server_default=func.now())
    updated = Column("modified", DateTime, default=func.now(), server_default=func.now(), onupdate=func.now(), server_onupdate=func.now())
    description = Column("description", String(200))


class Member(base):
    __tablename__="members"
    id = Column("id", mysql.INTEGER(100), primary_key=True, autoincrement=True)
    name = Column("name", String(100), primary_key=True)
    created = Column("created", DateTime, default=func.now(), server_default=func.now())
    updated = Column("modified", DateTime, default=func.now(), server_default=func.now(), onupdate=func.now(), server_onupdate=func.now())
    description = Column("description", String(200))


class PartnerMemberRelation(base):
    __tablename__="partner_member"
    id = Column("id", mysql.INTEGER, primary_key=True, autoincrement=True)
    partner_name = Column("partner_name", String(200), nullable=False)
    member_name = Column("member_name", String(200), nullable=False)