#credit cards

def credit_card(number):
    if len(number) == 16 and number[0] == '5':
        print('this is a valid MasterCard card number')
    elif len(number) == 16 and number[0] == '4':
        print('this is a valid Visa card number')
    elif len(number) == 16 and number[0] == '6':
        print('this is a valid Discover card number')
    elif len(number) == 15 and number[0] == '3':
        print('this is a valid Amex card number')
    else:
        print('That is not a valid credit card number')

number = input('Enter your credit card number: ')
credit_card(number)


#calculate_gtin13_barcode_check_digit
# Multiply every second digit by 3 (even number), and every other digit by 1 (odd number).
# Add up all the multiplied numbers.
# You can now get the check digit by working out what number 
# would have to be added to 
# the sum in order to bring it up to a multiple of 10. 
# If the number is already a multiple of 10, the check digit is 0.

def calculate_gtin13_barcode_check_digit(gtin):
    while len(gtin) != 12:
        print('That is not a 12 digit barcode')
        gtin = input("Try entering the barcode again: ")
    else:

        index = []
        for digit in gtin:
            index.append (int(digit))
        even = index[1::2]  
        odd = index[0::2]

        counter = 0
        multiplied = []
        while counter < 6:
            multiplied.append (even[0 + counter] * 3)
            counter += 1
        
        even = sum(multiplied)
        odd = sum(odd)

        total = odd + even

        remainder = total % 10
        check_digit = 10 - remainder

        print(check_digit)

gtin = input ('Enter your 12 digit barcode to get the GTIN-13 check digit: ')    
calculate_gtin13_barcode_check_digit(gtin)




#calculate_isbn10_barcode_check_digit
# 1. Multiply the first digit in the barcode by 10. Add the result to the sum.
# 2. Multiply the second digit in the barcode by 9. Add the result to the sum.
# 3. Multiply the third digit in the barcode by 8. Add the result to the sum.
# ....
# 4. Multiply the last number in the barcode by 1. Add the result 
# to the sum.
# 5. Calculate the remainder of the sum when divided by 11.
# The check digit is 11 minus the remainder of the result 
# in step 6 when divided by 11. 
# If the check digit is 10, it is replaced with an ‘X’.

def calculate_isbn10_barcode_check_digit(isbn):
    while len(isbn) != 9:
        print('That is not a 9 digit barcode')
        gtin = input("Try entering the barcode again: ")
    else:
        index = []
        for digit in isbn:
            index.append (int(digit))
        
        counter = 0
        multiply = 10
        multiplied = []
        while counter < 9:
            multiplied.append (index[0 + counter] * multiply)
            counter += 1
            multiply -= 1

        total = sum(multiplied)
        remainder = total % 11
        check_digit_before = 11 - remainder
        
        if check_digit_before != 10:
            print(check_digit_before)
        else:
            check_digit_before = 'X'
            print(check_digit_before)

isbn = input ('Enter your 9 digit barcode to get your ISBN-10 check digit: ')
calculate_isbn10_barcode_check_digit(isbn)