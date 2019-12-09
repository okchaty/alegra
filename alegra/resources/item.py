from alegra.resources.abstract import CreateableAPIResource 
from alegra.resources.abstract import ListableAPIResource
from alegra.resources.abstract import UpdateableAPIResource


class Item(
    ListableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "items"
