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
