import random
import os

def RandomNumber():
    print('How many numbers to generate?')
    amount = int(input())

    if amount > 0:
        print('Input the minimum number:')
        min = int(input())

        if min:
            print('Input the maximum number:')
            max = int(input())

            if max > min:
                print('\n')
                count = 0
                while count < amount:
                    print(random.randint(min, max))
                    count += 1
            print('Task is finished')
            print("Press the 'Enter' key to close the window")
            close = input()

            if close:
                sys.exit()
    else:
        os.system('cls')
        print(amount, 'is lower than 0, please try again.')
        RandomNumber()
RandomNumber()