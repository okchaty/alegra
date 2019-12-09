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
                "exchangeRate": 3350,
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
        # Modify invoice.
        response = alegra.Invoice.modify(
            resource_id=invoice_id,
            payments=[{
                "date": "2019-12-09",
                "amount": 778,
                "paymentMethod": "transfer",
                "currency": {
                    "code": "USD",
                    "exchangeRate": 3350,
                },
            }],
        )
        assert response.status_code == 200
        # Send invoice by email.
        response = alegra.Invoice.email(
            resource_id=invoice_id,
            emails=["chaty@yopmail.com"],
            sendCopyToUser=True,
            invoiceType="copy",
        )
        assert response.status_code == 400
        # Open invoice.
        response = alegra.Invoice.open(
            resource_id=invoice_id,
            stamp={
                "generateStamp": True,
            }
        )
        assert response.status_code == 400
        # Void invoice.
        response = alegra.Invoice.void(
            resource_id=invoice_id,
            cause="testing",
        )
        assert response.status_code == 400
