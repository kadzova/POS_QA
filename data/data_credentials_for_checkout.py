from faker import Faker


class CredentialsForCheckout:
    fake = Faker('en_US')
    state = 'California'
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    street_address = fake.street_address()
    city = fake.city()
    zip_code = '90210'
    phone_number = fake.phone_number()
