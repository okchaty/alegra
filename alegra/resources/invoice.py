from alegra.resources.abstract import CreateableAPIResource 
from alegra.resources.abstract import ListableAPIResource
from alegra.resources.abstract import UpdateableAPIResource


class Invoice(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "invoices"
