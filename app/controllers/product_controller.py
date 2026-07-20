from sqlalchemy.orm import Session

from app.db.postgresDB import db_connection
from app.models import pg_models
from app.response.response_model import ErrorResponseModel, SuccessResponseModel

db:Session = next(db_connection())

class Product():
    def create_new_product(self,request):
        try:
            data = pg_models.Product(
                name=request.name,
                description=request.description,
                price=request.price,
                stock_quantity=request.stock_quantity,
                category=request.category
            )
            db.add(data)
            db.commit()
            db.refresh(data)

            return SuccessResponseModel(data,"Successfully created!")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e),400)

    def get_all_products(self):
        try:
            product_list = db.query(pg_models.Product).all()

            return SuccessResponseModel(product_list,"Successfully returned")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e),400)

    def view_product_details(self,product_id):
        try:
            product = db.query(pg_models.Product).filter(
                pg_models.Product.product_id == product_id
            ).first()

            if product is None:
                return ErrorResponseModel("Product Not Found",404)

            return SuccessResponseModel(product, "Successfully Returned")

        except Exception as e:
            str(e)
            return ErrorResponseModel(str(e),400)

    def update_product(self,request):
        try:
            product = db.query(pg_models.Product).filter(
                pg_models.Product.product_id == request.product_id
            ).first()

            if product is None:
                return ErrorResponseModel("Product not Found", 404)

            product.name = request.name
            product.description = request.description
            product.price = request.price
            product.stock_quantity = request.stock_quantity
            product.category = request.category

            db.commit()
            db.refresh(product)

        except Exception as e:
            str(e)
            return ErrorResponseModel(str(e),400)

    def delete_product(self,product_id):
        try:
            product = db.query(pg_models.Product).filter(
                pg_models.Product.product_id == product_id
            ).first()

            db.delete(product)
            db.commit()

            return SuccessResponseModel(product_id, "Successfully Deleted")

        except Exception as e:
            str(e)
            return ErrorResponseModel(str(e),400)


productObj = Product()