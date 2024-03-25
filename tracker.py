# # tracker.py

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def track_number(num):
    # Check number country
    check_number = phonenumbers.parse(num)
    number_location = geocoder.description_for_number(check_number, "en")
    print("Number location:", number_location)

    # Mobile carrier/provider logic
    service_provider = phonenumbers.parse(num)
    number_country = carrier.name_for_number(service_provider, "en")
    print("Number country:", number_country)

    return number_location, number_country
