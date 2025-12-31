def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert_fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

#--------------------------------------------------------------------------------


def convert_fahrenheit_to_celsius(fahrenheit=98.6):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
result = convert_fahrenheit_to_celsius()
print(f"98.6°F is equal to {result:.2f}°C")
