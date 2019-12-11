from alegra.resources.abstract.api_resource import APIResource
from alegra.api_requestor import APIRequestor


class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, user=None, token=None, api_base=None, api_version=None,
             **params):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url()
        response = requestor.request(
            method="get",
            url=url,
            params=params,
        )
        return response
