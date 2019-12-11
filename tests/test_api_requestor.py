from alegra import api_requestor


class TestAPIRequestor:
    def test_authorization_header(self):
        requestor = api_requestor.APIRequestor(
            user = "ejemploapi@alegra.com",
            token = "tokenejemploapi12345",
        )
        assert requestor.authorization_header() == "Basic ZWplbXBsb2FwaUBhbGVncmEuY29tOnRva2VuZWplbXBsb2FwaTEyMzQ1"
