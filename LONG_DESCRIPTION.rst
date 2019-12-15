Alegra Bindings for Python
==========================

A Python library for Alegra's API.


Setup
-----

You can install this package by using the pip tool and installing:

    $ pip install alegra

Usage
----

The library needs to be configured with your user and token which is
available in your Alegra Account: https://app.alegra.com/configuration/api

Set **alegra.user** and **alegra.token** to their values:

.. code:: python
    import alegra 

    alegra.user = "...@..."
    alegra.token = "..."

    # List contacts.
    alegra.Contact.list()

    # Create contact.
    alegra.Contact.create(
      name="Chaty",
      identification={
        "type": "RUC", "number": "20000000000",
      },
      email="developer@okchaty.com",
      type=["client"],
      address={
        "address": "Jr. Neptuno 777",
        "city": "Lima, Peru",
      },
    )

    # Retrieve contact.
    alegra.Contact.retrieve(123)

    # Modify contact.
    alegra.Contact.modify(
      resource_id=contact_id,
      identification={
        "type": "RUC",
        "number": "20000000001",
      },
    )

    # Delete contact.
    alegra.Contact.delete(123)

Using the Alegra API
--------------------

Documentation can be found here:

- https://developer.alegra.com/docs
- https://github.com/okchaty/alegra 
