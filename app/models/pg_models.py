from sqlalchemy import Column, UUID, String, DateTime, func, Integer, Numeric, ForeignKey
from app.db.postgresDB import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(UUID(as_uuid=True),primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    phone = Column(String(10), nullable=False)
    address = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CartItem(Base):
    __tablename__ = "cart_items"

    cart_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(UUID, ForeignKey("customer.customer_id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.product_id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())