from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    Date,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    id = Column("customerid", Integer, primary_key=True)
    first_name = Column("firstname", String(50), nullable=False)
    last_name = Column("lastname", String(50), nullable=False)
    address = Column("address", String(100))
    city = Column("city", String(50))
    state = Column("state", String(50))
    zip_code = Column("zipcode", String(10))
    email = Column("email", String(100), unique=True, nullable=False)
    phone_number = Column("phonenumber", String(20))

    accounts = relationship("Account", back_populates="customer")


class Account(Base):
    __tablename__ = "accounts"

    id = Column("accountid", Integer, primary_key=True)
    customer_id = Column("customerid", Integer, ForeignKey("customers.customerid"))
    account_type = Column("accounttype", String(20), nullable=False)
    balance = Column("balance", DECIMAL(15, 2), default=0.0)
    date_opened = Column("dateopened", Date, default=datetime.date.today)

    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column("transactionid", Integer, primary_key=True)
    account_id = Column("accountid", Integer, ForeignKey("accounts.accountid"))
    transaction_type = Column("transactiontype", String(20), nullable=False)
    amount = Column("amount", DECIMAL(15, 2), nullable=False)
    transaction_date = Column(
        "transactiondate", DateTime, default=datetime.datetime.utcnow
    )

    account = relationship("Account", back_populates="transactions")