import random

import art
import playercomputer
import replit
from art import logo
from playercomputer import acak


def blackjack():
    print(logo)
    com=[]
    player=[]
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    com+=[acak(),acak()]
    player+=[acak(),acak()]

    print(f'computer first card: {com[0]}'.title())
    print(f'Your card: {player}'.title())
    print(f'Your card is {sum(player)}')
    lanjut=input('"n" for stand and "y" for hit? '.title())
    while lanjut == 'y':
        player+=[acak()]
        print(player)
        print(f'Your card is {sum(player)}')
        if 11 in player:
            if sum(player)>21:
                p=player.index(11)
                player[p]=1
        if sum(player)>21:
            print('BUST!!')
            break
        elif sum(player)==21:
            break
        else:
            lanjut=input('"n" for stand and "y" for hit? '.title())
    x=1
    while lanjut=='n':
        x+=1
        print(f'computer card: {com}'.title())
        if 11 in com:
            if sum(com)>21:
                c=com.index(11)
                com[c]=1
        if sum(com)<sum(player):
            com+=[acak()]
        if sum(com)>sum(player) and sum(com)<22:
            print(f'computer card: {sum(com)}'.title())
            print(f'Your card is: {sum(player)}')
            print('YOU LOSE!')
            break

        elif sum(com)==sum(player) and x>=3:
                print(f'computer card: {sum(com)}'.title())
                print(f'Your card is: {sum(player)}'.title())
                print('DRAW!')
                break

        elif sum(com)>22:
                print(f'computer card is: {sum(com)}'.title())
                print('BUST!')
                print('YOU WIN!')
                break
        
        elif sum(com)>sum(player) and sum(com)<22:
            print(f'Your card is: {sum(player)}'.title())
            print('YOU LOSE!')
            break
    if input('Wanna Play again? "y" or "n" '.lower())=='y':
         replit.clear()
         blackjack()
    else:
        replit.clear()