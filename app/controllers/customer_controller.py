import uuid

from app.db.postgresDB import db_connection
from app.models import pg_models
from app.response.response_model import ErrorResponseModel, SuccessResponseModel

db:Session = next(db_connection())

class Customer():
    def create_new_customer(self, request):
        try:
            customer_id = str(uuid.uuid4())
            data = pg_models.Customer(
                customer_id= customer_id,
                first_name=request.first_name,
                last_name=request.last_name,
                email=request.email,
                phone=request.phone,
                address=request.address
            )

            db.add(data)
            db.commit()
            db.refresh(data)

            return SuccessResponseModel(data, "successfully response")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e), 400)

    def get_all_customers(self):
        try:
            # select * from customer
            customer_list = db.query(pg_models.Customer).all()

            return SuccessResponseModel(customer_list, "Successfully returned")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e), 400)

    def view_customer_details(self, customer_id):
        try:
            # select * from customer where customer_id == ***

            customer = db.query(pg_models.Customer).filter(
                pg_models.Customer.customer_id == customer_id
            ).first()

            if customer is None:
                return ErrorResponseModel("Customer Not Found", 404)

            return SuccessResponseModel(customer, "Successfully returned the customer")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e), 400)

    def delete_customer(self,customer_id):
        try:
            customer = db.query(pg_models.Customer).filter(
                pg_models.Customer.customer_id == customer_id
            ).first()

            db.delete(customer)
            db.commit()

            return SuccessResponseModel(customer_id, "Successfully deleted")

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e), 400)

    def update_customer(self,request):
        try:

            customer = db.query(pg_models.Customer.customer_id).filter(
                pg_models.Customer.customer_id == request.customer_id
            ).first()

            if customer is None:
                return ErrorResponseModel("Customer not found", 404)

            customer.first_name = request.first_name,
            customer.last_name = request.last_name,
            customer.email = request.email,
            customer.phone = request.phone,
            customer.address = request.address

            db.commit()
            db.refresh(customer)

        except Exception as e:
            print(e)
            return ErrorResponseModel(str(e), 400)


customerObj = Customer()