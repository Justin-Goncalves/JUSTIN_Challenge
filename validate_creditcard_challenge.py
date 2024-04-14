import re

def validate_credit_card(card_number):
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card_number):
        card_number = card_number.replace('-', '')
        if re.match(r'(?!.*(\d)\1{3,})', card_number):
            return "Valid"
    return "Invalid"


how_many_cards = int(input("How many credit cards would you like to validate?\n"))

for index in range(how_many_cards):
    current_card = input(f"Enter credit card number {index + 1}\n")
    print(validate_credit_card(current_card))
