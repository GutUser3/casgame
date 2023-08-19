def calculate_winning(starting_amount, bet_amount, chosen_slot, winning_slot):
    if chosen_slot == winning_slot:
        starting_amount += bet_amount * 2
        print(f'You won! Now you have {starting_amount} \n')
        return starting_amount
    else:
        starting_amount -= bet_amount
        print(f'You lost! Now you have {starting_amount} \n')
        return starting_amount

