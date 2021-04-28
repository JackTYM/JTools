import os
import sys

def err():
    print('An error has occured')
    print('Please choose an option:')
    print('(1) Return to main menu')
    print('(2) Close window')
    returning = input()

    if returning == ('1'):
        os.system('cls')
        jtools()
    else:
        sys.exit()

def jtools():
    print('JTools')

    print('(1) List Creator')
    print('(2) Ascii Art Converter')
    print('(3) Character Counter')
    print('(4) Random Number Generator')
    print('(5) Random Word Generator')
    #print('() Multi Program Proccess')

    program = input()

    if program:
        if program == ('1'):
            os.system('cls')
            import ListCreator
            err()
        elif program == ('2'):
            os.system('cls')
            import AsciiArtConverter
            err()
        elif program == ('3'):
            os.system('cls')
            import CharacterCounter
            err()
        elif program == ('4'):
            os.system('cls')
            import RandomNumber
            err()
        elif program == ('5'):
            os.system('cls')
            import RandomWord
            err()
        else:
            print('That is not an option!')
            jtools()
jtools()
