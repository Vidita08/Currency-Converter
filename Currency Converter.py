from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        conversion_rate = c.convert(from_currency, to_currency, amount)
        return conversion_rate
    except ValueError:
        return "Invalid currency code(s) or amount."

if __name__ == "__main__":
    print("Currency Converter")
    print("-----------------")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the source currency code (e.g., USD): ").upper()
            to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
            
            result = currency_converter(amount, from_currency, to_currency)
            
            if isinstance(result, float):
                print(f"{amount} {from_currency} is equal to {result} {to_currency}")
            else:
                print(result)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
