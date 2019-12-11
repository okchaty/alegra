from alegra.resources.abstract.api_resource import APIResource
from alegra.api_requestor import APIRequestor


class DeleteableAPIResource(APIResource):
    @classmethod
    def delete(cls, resource_id, user=None, token=None, api_base=None,
               api_version=None, **params):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url() + str(resource_id)
        response = requestor.request(
            method="delete",
            url=url,
            params=params,
        )
        return response
