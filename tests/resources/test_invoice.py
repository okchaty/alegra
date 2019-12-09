import alegra


class TestInvoice:
    def test_crud(self):
        # List invoices.
        response = alegra.Invoice.list()
        assert response.status_code == 200
        # Create invoice.
        response = alegra.Invoice.create(
            date="2019-12-09",
            dueDate="2019-12-09",
            client=1,
            currency={
                "code": "USD",
                "code": 3350,
            },
            items=[{
                "id": 1,
                "price": 678,
                "quantity": 1,
            }, {
                "id": 2,
                "price": 100,
                "quantity": 1,
            }],
        )
        assert response.status_code == 201
        # Retrieve invoice.
        invoice_id = response.json().get("id")
        response = alegra.Invoice.retrieve(invoice_id)
        assert response.status_code == 200
        # Send invoice by email.
        response = alegra.Invoice.email(invoice_id)
        assert response.status_code == 200
        # Open invoice.
        response = alegra.Invoice.open(invoice_id)
        assert response.status_code == 200
        # Modify invoice.
        response = alegra.Invoice.modify(
            resource_id=invoice_id,
            price=100,
        )
        assert response.status_code == 200
        # Void invoice.
        response = alegra.Invoice.void(invoice_id)
        assert response.status_code == 200
