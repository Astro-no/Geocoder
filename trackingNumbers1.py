import phonenumbers
from phonenumbers import geocoder, carrier

def process_phone_numbers(phone_numbers):
    print("\nPhone Numbers Location and Carrier Information\n")
    for number in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number)
            location = geocoder.description_for_number(parsed_number, "en")
            service_provider = carrier.name_for_number(parsed_number, "en")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            print(f"Number: {formatted_number}")
            print(f"Location: {location}")
            print(f"Carrier: {service_provider}\n")
        except phonenumbers.NumberParseException as e:
            print(f"Error parsing number {number}: {e}")

phone_numbers = [
    "+123456789012",
    "+123456789012"
]

process_phone_numbers(phone_numbers)
