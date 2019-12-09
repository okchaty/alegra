from alegra.api_requestor import APIRequestor


class APIResource:
    @classmethod
    def retrieve(cls, resource_id, user=None, token=None, api_base=None,
                 api_version=None, **params):
        requestor = APIRequestor(
            user=user,
            token=token,
            api_base=api_base,
            api_version=api_version,
        )
        url = cls.class_url() + str(resource_id)
        response = requestor.request(
            method="get",
            url=url,
            params=params,
        )
        return response

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

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform "
                "actions on its subclasses (e.g. Contact, Invoice)"
            )
        return "{}/".format(cls.OBJECT_NAME)
