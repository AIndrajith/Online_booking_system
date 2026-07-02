from uuid import UUID

from fastapi import APIRouter

from app.controllers.customer_controller import customerObj
from app.requests.customer_requests import NewCustomerRequest, UpdateCustomerRequest

router = APIRouter(
    tags=['Customer Routers']
)

@router.post("/customers")
def create_new_customer(request:NewCustomerRequest):
    return customerObj.create_new_customer(request)

@router.get("/all-customers")
def get_all_customer_list():
    return customerObj.get_all_customers()

@router.get("/customer/{customer_id}")
def get_customer_data(customer_id:UUID):
    return customerObj.view_customer_details(customer_id)

@router.delete("/delete-customer/{customer_id}")
def delete_customer_details(customer_id:UUID):
    return customerObj.delete_customer(customer_id)

@router.put("/update-customer-data")
def update_customer_data(request:UpdateCustomerRequest):
    return customerObj.update_customer(request)