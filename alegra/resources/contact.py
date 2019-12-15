from alegra.resources.abstract import CreateableAPIResource
from alegra.resources.abstract import DeleteableAPIResource
from alegra.resources.abstract import ListableAPIResource
from alegra.resources.abstract import UpdateableAPIResource


class Contact(
    CreateableAPIResource,
    DeleteableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "contacts"
