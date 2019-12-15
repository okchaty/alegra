import alegra


class TestRetention:
    def test_crud(self):
        # List retentions.
        response = alegra.Retention.list()
        assert response.status_code == 200
        # Retrieve retention item.
        response = alegra.Retention.retrieve(1)
        assert response.status_code == 200
