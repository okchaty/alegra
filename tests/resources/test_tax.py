import alegra


class TestTax:
    def test_crud(self):
        # List taxes.
        response = alegra.Tax.list()
        assert response.status_code == 200
        # Retrieve tax item.
        response = alegra.Tax.retrieve(1)
        assert response.status_code == 200
