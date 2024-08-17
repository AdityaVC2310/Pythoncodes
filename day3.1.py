#user input
temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert temperature to Celsius
temperature_celsius = (temperature_fahrenheit - 32) * 5/9

# Print the converted temperature
print("Temperature in Celsius:", temperature_celsius)