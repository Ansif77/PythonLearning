try:  
    number=int(input('Enter a number:'))
    result=10/number
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print(f'The result is {result}')
finally:
    print("This is the final Result")