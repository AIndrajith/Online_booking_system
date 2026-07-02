import uuid

from app.db.postgresDB import db_connection
from app.models import pg_models
from app.response.response_model import ErrorResponseModel

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

        except Exception as e:
            print(str(e))
            return ErrorResponseModel(str(e), 400)


customerObj = Customer()