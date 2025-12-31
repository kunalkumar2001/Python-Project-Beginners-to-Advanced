def roman_to_decimal(roman):
    roman = roman.upper()

    roman_numerals = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    decimal_value = 0
    i = 0
    while i<len(roman):
        if i+1 <len(roman) and roman[i:i+2] in roman_numerals:
            decimal_value += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            decimal_value += roman_numerals[roman[i]]
            i += 1

    return decimal_value

roman_input = input("Enter a Roman numeral: ")
result = roman_to_decimal(roman_input)
print(f"The decimal value of {roman_input} is {result}.")