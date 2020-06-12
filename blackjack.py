suit = ('Copas','Paus', 'Ouros', 'Espadas')
rank = ('Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Valete', 'Dama', 'Rei','Ás')
value = {'Dois':2,'Três':3,'Quatro':4,'Cinco':5,'Seis':6,'Sete':7,'Oito':8,'Nove':9,'Dez':10,'Valete':10, 'Dama':10, 'Rei':10,'Ás':11}
import random

class Hand:
    def __init__(self):
        self.cards_in_hand = []
        self.value = 0
        self.aces_count = 0
    
    def pick_card(self,card):
        self.cards_in_hand.append(card)
        self.value += value[card.rank]
        if card.rank == 'Ás':
            self.aces_count += 1
    def adjust_for_ace_value(self):
        if self.value > 21 and self.aces_count:
            self.value -= 10
            self.aces_count -= 1     

class Chips:
    def __init__(self,chips_amount = 1000):
        self.chips_amount = chips_amount
        self.bet = 0
    def win_bet(self):
        self.chips_amount += self.bet
    def lose_bet(self):
        self.chips_amount -= self.bet

class Decks:  
    def __init__(self):

        self.deck = []
        for i in suit:
            for j in rank:
                self.deck.append(Card(i,j))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__()+'\n'
        return "O Deck é composto por 52 cartas: \n"+deck_comp
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Card:

    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank+" de "+self.suit

test_deck = Decks()
test_deck.shuffle_deck()
print(test_deck)
