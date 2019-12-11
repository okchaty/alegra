from alegra.api_requestor import APIRequestor
from alegra.resources.abstract import CreateableAPIResource 
from alegra.resources.abstract import EmailableAPIResource
from alegra.resources.abstract import ListableAPIResource
from alegra.resources.abstract import UpdateableAPIResource
from alegra.resources.abstract import VoidableAPIResource


class Invoice(
    CreateableAPIResource,
    EmailableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    VoidableAPIResource,
):
    OBJECT_NAME = "invoices"

    @classmethod
    def open(cls, resource_id, user=None, token=None, api_base=None,
             api_version=None, **json):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url() + str(resource_id) + "/open/"
        response = requestor.request(
            method="post",
            url=url,
            json=json,
        )
        return response
