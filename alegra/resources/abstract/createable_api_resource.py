from alegra.resources.abstract.api_resource import APIResource
from alegra.api_requestor import APIRequestor


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, user=None, token=None, api_base=None, api_version=None,
             **json):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url()
        response = requestor.request(
            method="post",
            url=url,
            json=json,
        )
        return response
