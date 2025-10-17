try:  
    number=int(input('Enter a number:'))
    result=10/number
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print(f'The result is {result}')
finally:
    print("This is the final Result")

# raise error
# x=-5
# if x<0:
#     raise ValueError("nagative numbers not allowed")

#create a error
# class NegativeNumberError(Exception):
#     pass
# def check_number(num):
#     if num<0:
#         raise NegativeNumberError('Negative number not allowed')
#     else:
#         print(f'result is: {num}')
# check_number(-5)
#handle the error
# try:
#     check_number(-5)
# except NegativeNumberError as e:
#     print(e)
