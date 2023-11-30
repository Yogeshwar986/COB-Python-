import requests

def get_exchange_rate(from_curr, to_curr):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_curr}")
    data = response.json()
    exchange_rate = data['rates'][to_curr]
    return exchange_rate

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount


from_curr = str(input("Enter a currency to convert:")).upper()
to_curr = str(input("Enter a cuurency to convert to:")).upper()
amount = float(input("Enter the amount:"))
converted_amount = convert_currency(amount, from_curr, to_curr)
print(f"{amount} {from_curr} is equal to {converted_amount} {to_curr}")

