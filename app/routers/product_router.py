from fastapi import APIRouter

from app.controllers.product_controller import productObj
from app.requests.product_requests import NewProductRequest, UpdateProductRequest

product_router = APIRouter(
    tags=["Product routes"]
)

@product_router.post("/product")
def create_new_product(request:NewProductRequest):
    return productObj.create_new_product(request)

@product_router.get("/product")
def get_all_product_list():
    return productObj.get_all_products()

@product_router.get("/product/{product_id}")
def view_product_details(product_id:int):
    return productObj.view_product_details(product_id)

@product_router.put("/product/{product_id}")
def update_product_data(request:UpdateProductRequest):
    return productObj.update_product(request)

@product_router.delete("/product/{product_id}")
def delete_product(product_id:int):
    return productObj.delete_product(product_id)