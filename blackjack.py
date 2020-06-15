suit = ('Copas','Paus', 'Ouros', 'Espadas')
rank = ('Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Valete', 'Dama', 'Rei','Ás')
value = {'Dois':2,'Três':3,'Quatro':4,'Cinco':5,'Seis':6,'Sete':7,'Oito':8,'Nove':9,'Dez':10,'Valete':10, 'Dama':10, 'Rei':10,'Ás':11}
import random
playing = True


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
    def __init__(self,chips_amount=500):
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
    
    def __len__(self):
        return len(self.deck)

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

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Quanto deseja apostar? "))
            if chips.bet > chips.chips_amount:
                print("Opa, você não tem isso tudo!")
                continue
            else:
                break
        except:
            print("Ops! Não é válido. Tem que apostar um número inteiro!")

def hit(Decks, Hand):
    Hand.pick_card(Decks.deal())
    Hand.adjust_for_ace_value()

def show_hand(hand):
    print("Cartas na mão:", *player_hand.cards_in_hand, sep='\n ')
    print("Valor da mão: ", hand.value)

def hit_stand(Decks, Hand):
    global playing
    
    while playing:
        choice = input("Digite 'H' para pedir carta e ou 'S' para encerrar seu turno: ")
        if choice[0].lower() == 'h':
            hit(Decks,Hand)
            show_initial(player_hand,dealer_hand)
            player_hand.adjust_for_ace_value()
            if player_hand.value >=21:
                playing = False               
        elif choice[0].lower() == 's':
            print("Ok. Agora é o turno da casa.")
            playing = False
        else:
            print('Ops, tente novamente.')
            continue        

def show_initial(player,dealer):
    print("\nMão do dealer: ({})".format(value[dealer_hand.cards_in_hand[1].rank]))
    print(" <Carta virada para baixo>")
    print(" ",dealer_hand.cards_in_hand[1])
    print(f"\nMão do jogador: ({player_hand.value})", *player_hand.cards_in_hand, sep='\n ')

def jogar_novamente():
    escolha = input("Deseja jogar novamente? s/n: ")
    return escolha[0].lower()
def dealer_turn(deck,hand):
    while dealer_hand.value <= 17:
        dealer_hand.pick_card(deck.deal()) 
        dealer_hand.adjust_for_ace_value()

def show_all(player, dealer):
    print(f"\nMão da casa: ({dealer_hand.value})", *dealer_hand.cards_in_hand, sep='\n ')
    print(f"\nMão do jogador: ({player_hand.value})", *player_hand.cards_in_hand, sep='\n ')    


if __name__ == '__main__':
    while True:
        deck = Decks()
        deck.shuffle_deck()
        chips = Chips()

        while len(deck)>10 and chips.chips_amount >0:
            player_hand = Hand()
            dealer_hand = Hand()

            dealer_hand.pick_card(deck.deal())
            dealer_hand.pick_card(deck.deal())

            player_hand.pick_card(deck.deal())
            player_hand.pick_card(deck.deal())

            show_initial(player_hand, dealer_hand)
            
            take_bet(chips)

            while playing:
                hit_stand(deck, player_hand)
                    
            if player_hand.value <= 21:
                dealer_turn(deck, dealer_hand)
                show_all(player_hand, dealer_hand)
            
            if player_hand.value > 21:
                print("\nJogador estourou\nVitória da Casa!")
                chips.lose_bet()
                #print("Saldo atual em: ", chips.chips_amount)
            elif player_hand.value > dealer_hand.value and player_hand.value <= 21:
                print("Jogador Venceu!")
                chips.win_bet()
            elif player_hand.value == dealer_hand.value:
                print("Empate!\nNinguém leva!")
            else:
                print("Jogador Perdeu!")
                chips.lose_bet()            
            print("Saldo atual em: ", chips.chips_amount)
            rep = jogar_novamente()
            if rep == 's':   
                playing = True
                continue            
            else:
                print("Obrigado por jogar.\nAté a próxima.")
        break        