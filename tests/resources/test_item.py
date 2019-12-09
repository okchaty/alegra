import alegra


class TestItem:
    def test_crud(self):
        # List items.
        response = alegra.Item.list()
        assert response.status_code == 200
        # Create item.
        response = alegra.Item.create(
            name="Cobro por servicio tecnológico",
            price=200,
        )
        assert response.status_code == 201
        # Retrieve item.
        item_id = response.json().get("id")
        response = alegra.Item.retrieve(item_id)
        assert response.status_code == 200
        # Modify item.
        response = alegra.Item.modify(
            resource_id=item_id,
            price=100,
        )
        assert response.status_code == 200
        # Delete item.
        response = alegra.Item.delete(item_id)
        assert response.status_code == 200
