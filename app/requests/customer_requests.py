from uuid import UUID

from pydantic import BaseModel


class NewCustomerRequest(BaseModel):
    first_name : str
    last_name :str
    email : str
    phone : str
    address : str

class UpdateCustomerRequest(BaseModel):
    customer_id : UUID
    first_name : str
    last_name :str
    email : str
    phone : str
    address : str