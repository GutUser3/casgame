from random import choice
from decouple import config
from lose_conditions import calculate_winning

starting_amount = config('MY_MONEY', cast=int)
number_list = list(range(1, 31))

while True:
    print(f'You have {starting_amount}$ left')
    winning_slot = choice(number_list)
    player_bet = int(input('How much do you bet? '))
    player_slot = int(input('Choose slot: '))
    starting_amount = calculate_winning(starting_amount, player_bet, player_slot, winning_slot)
    if starting_amount <= 0:
        print('You have no money left')
        break
    game = input('Do you wish to continue? (y/n)')
    if game == 'n':
        print('exiting...')
        break
