import requests

API_KEY = "YOUR_API_KEY"

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    return data["rates"][target_currency]

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    
    return converted_amount

def main():
    print("Welcome to Currency Converter!")
    print("Enter the amount, base currency, and target currency for conversion:")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == "q":
            break
        
        amount, base_currency, target_currency = user_input.split()
        amount = float(amount)
        
        converted_amount = convert_currency(amount, base_currency, target_currency)
        print(f"{amount} {base_currency} = {converted_amount} {target_currency}\n")
    
    print("Thank you for using Currency Converter!")

if __name__ == "__main__":
    main()
