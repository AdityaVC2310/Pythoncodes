#user input
amount_inr = float(input("amount in Indian Rupees (INR): "))

# Exchange rates
exchange_rate_usd = 80.00
exchange_rate_cad = 0.017
exchange_rate_aed = 0.060
exchange_rate_yen = 1.55
exchange_rate_eur = 0.035

# Conversion to other currencies
amount_usd = amount_inr * exchange_rate_usd
amount_cad = amount_inr * exchange_rate_cad
amount_aed = amount_inr * exchange_rate_aed
amount_yen = amount_inr * exchange_rate_yen
amount_eur = amount_inr * exchange_rate_eur

# Displaying the converted amounts
print("Amount in USD:", amount_usd)
print("Amount in CAD:", amount_cad)
print("Amount in AED:", amount_aed)
print("Amount in YEN:", amount_yen)
print("Amount in Euros:", amount_eur)
