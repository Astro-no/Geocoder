import phonenumbers
from phonenumbers import geocoder
""" 
Works for some numbers.
Sadly, for Kenyan numbers, it shows just the country.
Replace with your desired numbers. I couldn't leave mine, LOL 
"""

phone_number1 = phonenumbers.parse("+123456789012")
phone_number2 = phonenumbers.parse("+123456789012")
phone_number3 = phonenumbers.parse("+123456789012")
phone_number4 = phonenumbers.parse("+123456789012")

print("\n Phone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));

