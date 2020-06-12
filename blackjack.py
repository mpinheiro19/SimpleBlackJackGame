suit = ('Copas','Paus', 'Ouros', 'Espadas')
rank = ('Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Valete', 'Dama', 'Rei','Ás')
value = {'Dois':2,'Três':3,'Quatro':4,'Cinco':5,'Seis':6,'Sete':7,'Oito':8,'Nove':9,'Dez':10,'Valete':10, 'Dama':10, 'Rei':10,'Ás':10}
import random

class Hand:
    pass

class Chips:
    pass

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
