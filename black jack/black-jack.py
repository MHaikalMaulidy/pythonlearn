import art
import bj
import playercomputer
from art import logo
from bj import blackjack
from playercomputer import acak

if input('do you want to play blackjack? "y" or "n" '.title().lower())=='y':
    blackjack()
else:
    print('have a good time!')