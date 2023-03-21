# QAP 4
# Program that calculates insurance policy information.
# Author: Michael Bennett
# Date: 2023-03-18
import re
import datetime
import FormatValues as FV
# Imports

# Constants
# Read the constants from the OSICDef.dat file
f = open('OSICDef.dat', 'r')

POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CAR_DISC = float(f.readline())
EXTRA_LIABILITY = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_COV = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROC_FEE = float(f.readline())
VALID_NAME_CHAR = set(f.readline())

f.close()

# List of valid province abbreviations for user input validation
prov_list = ["AB", "BC", "MB", "NB", "NL" "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
allowed_postal = set("ABCEGHJKLMNPRSTVWXYZabceghjklmnprstvwxyz1234567890 ")

# Functions

# Main Program
# Inputs
while True:
    while True:
        first_name = input('Enter the customer\'s first name: ').title()
        if first_name == '':
            print("Cannot be empty - please try again")
        elif not all(char in VALID_NAME_CHAR for char in first_name):
            print('Invalid characters entered - please try again.')
        else:
            break

    while True:
        last_name = input('Enter the customer\'s last name: ').title()
        if last_name == '':
            print("Cannot be empty - please try again")
        elif not all(char in VALID_NAME_CHAR for char in last_name):
            print('Invalid characters entered - please try again.')
        else:
            break

    print('Enter the customer\'s address information')

    while True:
        street = input('Street Address: ')
        if street == '':
            print("Cannot be empty - please try again")
        else:
            break

    while True:
        city = input('City: ').title()
        if city == '':
            print('Cannot be empty - please try again.')
        elif not all(char in VALID_NAME_CHAR for char in city):
            print('Invalid characters entered - please try again.')
        else:
            break

    while True:
        province = input('Province ("AB", "BC", "MB", "NB", "NL" "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"): ').upper()
        if province == '':
            print('Cannot be empty - please try again.')
        elif province not in prov_list:
            print('Invalid province abbreviation entered - please try again.')
        else:
            break

    while True:
        postal_code = input('Postal Code (L0L 0L0): ').upper()
        if postal_code == '':
            print('Cannot be empty - please try again.')
        elif len(postal_code) != 7:
            print('Must be 7 characters in length (including the space) - please try again.')
        elif not set(postal_code).issubset(allowed_postal):
            print('Invalid characters entered - please try again.')
        elif not re.match(r'^[A-Z]\d[A-Z]\s\d[A-Z]\d$', postal_code):
            print('Invalid format entered - please try again.')
        else:
            break

    while True:
        phone_number = input('Phone Number (0000000000): ')
        if phone_number == '':
            print('Cannot be blank - please try again.')
        elif not phone_number.isdigit():
            print('Must contain numbers only - please try again.')
        elif len(phone_number) != 10:
            print('Must be 10 digits in length - please try again.')
        else:
            break

    while True:
        num_cars_ins = input('Enter the number of cars insured: ')
        if num_cars_ins == '':
            print('Cannot be empty - please try again.')
        try:
            num_cars_ins = int(num_cars_ins)
        except ValueError:
            print('Must be an integer number - please try again.')
        else:
            break

    while True:
        extra_liability = input('Do you want extra liability? ([Y]es or [N]o): ').upper()
        if extra_liability == '':
            print('Cannot be blank - please try again.')
        elif extra_liability != 'Y' and extra_liability != 'N':
            print('Invalid input (Enter "Y" or "N") - please try again.')
        else:
            break

    while True:
        glass_coverage = input('Does the customer want glass coverage ([Y]es or [N]o): ').upper()
        if glass_coverage == '':
            print('Cannot be blank - please try again.')
        elif glass_coverage != 'Y' and glass_coverage != 'N':
            print('Invalid input (Enter "Y" or "N") - please try again.')
        else:
            break

    while True:
        loaner_car = input('Does the customer want loaner car coverage ([Y]es or [N]o): ').upper()
        if loaner_car == '':
            print('Cannot be blank - please try again.')
        elif loaner_car != 'Y' and loaner_car != 'N':
            print('Invalid input (Enter "Y" or "N") - please try again.')
        else:
            break

    while True:
        payment_type = input('Does the customer want to pay in full or monthly ([F]ull or [M]onthly): ').upper()
        if payment_type == '':
            print('Cannot be blank - please try again.')
        elif payment_type != 'F' and payment_type != 'M':
            print('Invalid input (Enter "F" or "M") - please try again.')
        else:
            break

    # Calculations
    # Calculate the premium
    if num_cars_ins > 1:
        premium = BASIC_PREM + (BASIC_PREM * ADD_CAR_DISC) * num_cars_ins - 1
    else:
        premium = BASIC_PREM

    # Calculate the cost of extra liability
    if extra_liability == 'Y':
        extra_liability = "(Yes)"
        extra_liability_cost = EXTRA_LIABILITY * num_cars_ins
    else:
        extra_liability = "(No)"
        extra_liability_cost = 0

    # Calculate the cost of glass coverage
    if glass_coverage == 'Y':
        glass_coverage = "(Yes)"
        glass_coverage_cost = GLASS_COV * num_cars_ins
    else:
        glass_coverage = "(No)"
        glass_coverage_cost = 0

    # Calculate the cost of loaner coverage
    if loaner_car == 'Y':
        loaner_car = "(Yes)"
        loaner_car_cost = LOANER_COV * num_cars_ins
    else:
        loaner_car = "(No)"
        loaner_car_cost = 0

    # Calculate the total cost including extra costs and HST
    total_extra_costs = extra_liability_cost + glass_coverage_cost + loaner_car_cost
    total_ins_premium = premium + total_extra_costs
    HST = total_ins_premium * HST_RATE
    total_cost = total_ins_premium + HST

    # Calculate the cost of monthly payments if customer chooses to pay monthly
    if payment_type == 'M':
        monthly_payment = (total_cost + MONTHLY_PROC_FEE) / 8
    else:
        monthly_payment = 'NA'

    # Get the current date and assign it to invoice_date variable
    invoice_date = datetime.datetime.now()

    # Calculate the next month
    if invoice_date.month == 12:
        next_month = 1
        next_year = invoice_date.year + 1
    else:
        next_month = invoice_date.month + 1
        next_year = invoice_date.year

    # Assign next payment date
    next_pay_date = datetime.datetime(next_year, next_month, 1)

    # Combine first and last names in one variable
    full_name = f'{first_name} {last_name}'

    # Format the output in the style of a receipt
    print()
    print('                ONE STOP INSURANCE')
    print('             CUSTOMER POLICY SUMMARY')
    print('-' * 50)
    print(f'Date:                                   {invoice_date.strftime("%Y-%m-%d")}')
    print()
    print(f'Client: {full_name:<22s}')
    print(f'        {street:<22s}')
    print(f'        {city:<17s}, {province} {postal_code}')
    print(f'Phone:  {phone_number}')
    print()
    print(f'Policy Details')
    print(f'    Number of cars insured: {num_cars_ins}')
    print(f'    Premium:                             {FV.FDollar2(premium):>9}')
    print(f'    Extra Liability:        {extra_liability} Cost:  {FV.FDollar2(extra_liability_cost):>9}')
    print(f'    Glass Coverage:         {glass_coverage} Cost:  {FV.FDollar2(glass_coverage_cost):>9}')
    print(f'    Loaner car coverage:    {loaner_car} Cost:  {FV.FDollar2(loaner_car_cost):>9}')
    print(f'                                         ---------')
    print(f'    Total Extra Cost:                    {FV.FDollar2(total_extra_costs):>9}')
    print()
    print(f'    Total Insurance Premium:             {FV.FDollar2(total_ins_premium):>9}')
    print(f'    HST:                                 {FV.FDollar2(HST):>9}')
    print('                                         ---------')
    print(f'    Total Cost:                          {FV.FDollar2(total_cost):>9}')
    print('                                         ---------')
    print(f'    Monthly Payment:                     {FV.FDollar2(monthly_payment):>9}')
    print('                                         ---------')
    print(f'Next Payment Date:                      {next_pay_date.strftime("%Y-%m-%d")}')
    print('-' * 50)
    print('    Thank You For Choosing One Stop Insurance!')
    print('                 Have A Great Day!')

    # Save values to file Policies.dat
    f = open('Policies.dat', 'a')

    f.write('{}, '.format(str(POLICY_NUM)))
    f.write('{}, '.format(str(invoice_date.strftime('%Y-%m-%d'))))
    f.write('{}, '.format(str(first_name)))
    f.write('{}, '.format(str(last_name)))
    f.write('{}, '.format(str(street)))
    f.write('{}, '.format(str(city)))
    f.write('{}, '.format(str(province)))
    f.write('{}, '.format(str(postal_code)))
    f.write('{}, '.format(str(phone_number)))
    f.write('{}, '.format(str(num_cars_ins)))
    f.write('{}, '.format(str(extra_liability)))
    f.write('{}, '.format(str(glass_coverage)))
    f.write('{}, '.format(str(loaner_car)))
    f.write('{}, '.format(str(payment_type)))
    f.write('{},\n'.format(str(total_ins_premium)))

    f.close()

    print('Policy information processed and saved.')

    POLICY_NUM += 1

    # Give user an option to process another or quit
    run_again = input('Would you like to process another policy? ([Y]es or [N]o): ').upper()
    if run_again != "Y":
        break

# Write the current values back to the OSICDefaults.dat file
f = open('OSICDef.dat', 'w')

f.write('{}\n'.format(str(POLICY_NUM)))
f.write('{}\n'.format(str(BASIC_PREM)))
f.write('{}\n'.format(str(ADD_CAR_DISC)))
f.write('{}\n'.format(str(EXTRA_LIABILITY)))
f.write('{}\n'.format(str(GLASS_COV)))
f.write('{}\n'.format(str(LOANER_COV)))
f.write('{}\n'.format(str(HST_RATE)))
f.write('{}\n'.format(str(MONTHLY_PROC_FEE)))
f.write('{}\n'.format(str(VALID_NAME_CHAR)))

f.close()
