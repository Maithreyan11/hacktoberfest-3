from random import randint

def enter_number():
    number = int(input('Enter a number between 1 and 100: '))
    if (number>100) or (number<=0):
        print('This number is not allowed')
        enter_number()
    return number

number = enter_number()

count = 0
while True:
    count += 1
    random_number = randint(1, 100)
    print(f'the random number is: {random_number}')
    if (number-random_number) == 0:
        print(f'{count} attempts were spent until the result was 0')
        break
