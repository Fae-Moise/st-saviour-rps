import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to rock, paper, scissors! 🗿📃✂️')
    options = ('rock' , 'scissors' , 'paper' )
    choice = random.randint (0, 2 )


    print ('computer player selected: ' + options[choice])
    computer = options[choice]

    response = input('please choose rock, paper, or scissors:')

    while response != 'rock' and response !='scissors' and response != 'paper':
        response = input ('choose rock,paper, or scissors: ')

    print(f'player selected{response}')

    if response == 'rock' and computer == 'rock':
        print('you tie!')
    if response == 'rock' and computer  == 'scissors':
        print('you win!')
    if response == 'rock' and computer == 'paper':
        print('you lose!')
    
    if response == 'scissors' and computer == 'scissors':
        print('you tie!')
        if response == 'scissors' and computer == 'paper':
            print('you win!')
        if response == 'paper' and computer == 'scissors':
            print('you lose!')
                
            if response == 'paper' and computer == 'paper':
                    print('you tie!')
                    if response == 'paper' and computer == 'rock':
                        print('you win!')
                    if response == 'paper' and computer == 'scissors':
                        print ('you lose!')