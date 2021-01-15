''' Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, 
create good-looking XML documents, fill-in your persistence to stress test it, 
or anonymize data taken from a production service, Faker is for you.'''

from faker import Faker
from faker.providers import internet
# Create Instances
fake = Faker()
fake.add_provider(internet)
# Creating the Data

print ("Name :", fake.name())
print ("Email :", fake.email())
print ("Url :", fake.url())
print ("Text :", fake.text())
print ("Country :", fake.country())
print ("Address :", fake.address())
print ("Year :", fake.year())
print("IP-Address : ", fake.ipv4_private())