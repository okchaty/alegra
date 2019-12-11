# Alegra in Python
Wrapper in python for [Alegra](https://alegra.com).

## Usage

The library needs to be configured with your user and token which is
available in your [Alegra Account](https://app.alegra.com/configuration/api).
Set `alegra.user` and `alegra.token` to their values:

```python
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
```
