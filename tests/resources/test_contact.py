import alegra


class TestContact:
    def test_crud(self):
        # List contacts.
        response = alegra.Contact.list()
        assert response.status_code == 200
        # Create contact.
        response = alegra.Contact.create(
            name="Chaty",
            identification={
                "type": "RUC",
                "number": "20000000000",
            },
            email="developer@okchaty.com",
            type=["client"],
            address={
                "address": "Jr. Neptuno 777",
                "city": "Lima, Peru",
            },
        )
        assert response.status_code == 201
        # Retrieve contact.
        contact_id = response.json().get("id")
        response = alegra.Contact.retrieve(contact_id)
        assert response.status_code == 200
        # Modify contact.
        response = alegra.Contact.modify(
            resource_id=contact_id,
            identification={
                "type": "RUC",
                "number": "20000000001",
            },
        )
        assert response.status_code == 200
        # Delete contact.
        response = alegra.Contact.delete(contact_id)
        assert response.status_code == 200
