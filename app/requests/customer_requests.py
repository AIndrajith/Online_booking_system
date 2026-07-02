from pydantic import BaseModel


class NewCustomerRequest(BaseModel):
    first_name : str
    last_name :str
    email : str
    phone : str
    address : str