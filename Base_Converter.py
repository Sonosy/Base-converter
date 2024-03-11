#This is a program which converts between each base 2, 8, 10, 16

# Gets the required base from the user and makes sure the user's input is valid and returns the number value of the base
def get_base(menu):
    while True:
        user_input = input(menu).upper()
        if user_input in ['A', 'B', 'C', 'D']:
            return base_converter(user_input)
        else:
            print("Please select a valid choice.")


# Converts the base from user input (A, B, C, D) to the value of the base
def base_converter(base_str):
    if base_str == 'A':
        base = 10
    elif base_str == 'B':
        base = 2
    elif base_str == 'C':
        base = 8
    else:
        base = 16
    return base


# Checks if the entered number is valid in the base from which the user wants to convert
def valid_number(num, from_base):
    valid_strings = "0123456789ABCDEF"
    for digit in num:
        if digit not in valid_strings[:from_base]:
            return False
    return True


# Converts the number to decimal and then to the desired base
def result(num, from_base, to_base):
    if from_base != 16:
        num = int(num)
    if from_base == to_base or num == 0:
        return num
    dec = to_dec(num, from_base)
    if to_base == 10:
        return dec
    elif to_base == 2 or to_base == 8:
        return dec_converter(dec, 10, to_base)
    else:
        return dec_to_hex(dec)


# Decides the steps according to from which base and to which base
def to_dec(num, from_base):
    if from_base == 16:
        # Convert from hexadecimal to decimal
        symbol = "0123456789ABCDEF"
        dec = 0
        for digit in num:
            dec = dec * from_base + symbol.index(digit.upper())
        return dec
    else:
        return dec_converter(num, from_base, 10)


# Converts from decimal to binary or octal and otherwise
def dec_converter(from_num, from_base, to_base):
    to_num = 0
    power = 0
    while from_num > 0:
        to_num += (from_num % to_base) * (from_base ** power)
        from_num = from_num // to_base
        power += 1
    return to_num


# Convert from decimal to hexadecimal
def dec_to_hex(dec):
    symbols = "0123456789ABCDEF"
    hexa = ""
    while dec > 0:
        hexa = symbols[dec % 16] + hexa
        dec = dec // 16
    return hexa


while True:
    # Menu 1 to ask the user to enter a number or exit the program
    menu1 = input("** Numbering System Converter **\n"
                      "A) Insert a new number\nB) Exit program\n"
                      "Please enter your choice (A/B): ").upper()
    if menu1 == 'A':
        # Asks the user to enter a number and then the base which the user wants to converts from and to
        num = input("Please insert a number: ").upper()
        # Menu 2 to take the base which the user wants to convert the number from
        from_base_menu2 = get_base("\n** Please select the base you want to convert a number from**\n"
                                   "A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n"
                                   "Please enter your choice (A/B/C/D): ")
        if not valid_number(num, from_base_menu2):
            print("Error:", num, "is not a valid number in base", from_base_menu2, "\n")
            continue
        # Menu 3 to take the base which the user wants to convert the number to
        to_base_menu3 = get_base("\n** Please select the base you want to convert a number to **\n"
                                 "A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n"
                                 "Please enter your choice (A/B/C/D): ")
        # Print the result
        print("Result:", result(num, from_base_menu2, to_base_menu3))
    elif menu1 == 'B':
        # Exits the program
        print("Exiting the program.")
        exit()
    else:
        print("Please select a valid choice.")
        