import phonenumbers
from phonenumbers import carrier 

service_provider = phonenumbers.parse("+919876543210")
# this will print the country name 
print(geocoder.description_for_number(phone_number, 'en'))  
# this will print the service provider name 
print(carrier.name_for_number(service_provider, 'en'))  