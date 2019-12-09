from alegra.api_requestor import APIRequestor
from alegra.resources.abstract.api_resource import APIResource


class EmailableAPIResource(APIResource):
    @classmethod
    def email(cls, resource_id, user=None, token=None, api_base=None,
              api_version=None, **json):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url() + str(resource_id) + "/email/"
        response = requestor.request(
            method="post",
            url=url,
            json=json,
        )
        return response
