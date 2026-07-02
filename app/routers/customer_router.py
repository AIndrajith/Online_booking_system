from fastapi import APIRouter

from app.controllers.customer_controller import customerObj
from app.requests.customer_requests import NewCustomerRequest

router = APIRouter(
    tags=['Customer Routers']
)

@router.post("/customers")
def create_new_customer(request:NewCustomerRequest):
    return customerObj.create_new_customer(request)