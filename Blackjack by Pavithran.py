import random

def initialize_game():
    # Initialize cards and deal initial cards to dealer and guest
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    cards_dealer_one = random.randint(2, 11)
    cards_dealer_two = random.randint(2, 11)
    cards_dealer = [cards_dealer_two + cards_dealer_one]
    
    total_sum_dealer = sum(cards_dealer)
    print(f"First dealer card is {cards_dealer_one}")
    
    cards_guest = random.sample(cards, 2)
    total_sum_guest = sum(cards_guest)
    print(f"You have {cards_guest}, total sum is {total_sum_guest}")
    
    return cards, cards_dealer, total_sum_dealer, cards_guest, total_sum_guest

def game():
    cards, cards_dealer, total_sum_dealer, cards_guest, total_sum_guest = initialize_game()
    
    next_cards = True

    while next_cards:
        one_more_time = input("Do you want one more card? 'y' for Yes: ")
        if one_more_time.lower() == "y":
            # Guest takes one more card
            third_card_user = random.randint(2, 11)
            cards_guest.append(third_card_user)
            total_sum_guest += third_card_user
            print(f"You have {cards_guest}, total sum is {total_sum_guest}")
            
            if total_sum_guest > 21:
                print("House won")
                break
        else:
            next_cards = False
            print(f"Dealer has {cards_dealer}")
            
            # Dealer takes cards until their total sum is less than 17
            while total_sum_dealer < 17:
                third_card_dealer = random.randint(2, 11)
                cards_dealer.append(third_card_dealer)
                print(f"Dealer calls one more card. It is {third_card_dealer}")
                total_sum_dealer += third_card_dealer
                print(f"Total sum of dealer's cards is {total_sum_dealer}")
                
            # Determine the winner
            determine_winner(total_sum_dealer, total_sum_guest)

def determine_winner(total_sum_dealer, total_sum_guest):
    if total_sum_guest == 21 and total_sum_dealer == 21:
        print("Deuce")
    elif total_sum_dealer > 21:
        print("You won")
    elif total_sum_dealer <= 21 and total_sum_dealer > total_sum_guest:
        print(f"House won with a score of {total_sum_dealer}")
    elif total_sum_dealer <= 21 and total_sum_dealer < total_sum_guest:
        print("You won")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    game()
