import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value 
    
    def cardReturn(self):
        return {"suit":self.suit,"value":self.value}

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return "{} of {}".format(self.value,self.suit)

class Deck:
    suit = ("Hearts", "Diamonds", "Clubs", "Spades")
    value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    cnt = 52
    cards = []

    @classmethod
    def count(cls):
        return Deck.cnt
    
    @classmethod
    def _deal(cls,num):
        cls.num = int(num)
        if Deck.cnt == 0:
            raise ValueError("All cards have been dealt")
        elif Deck.cnt < cls.num:
            Deck.cnt = 0
        else: 
            Deck.cnt = Deck.cnt - cls.num
        return cls # good practice to return self when there is nothing to return
    
    
    def __init__(self):
        Deck.cards = []
        for s in Deck.suit:
            for v in Deck.value:
                c = Card(s,v)
                d = c.cardReturn()
                Deck.cards.append(d)
                print(c)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def shuffle(self):
        if Deck.cnt < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(Deck.cards)
        return self # good practice to return self when there is nothing to return

    def deal_card(self):
        Deck._deal(1)
        return Deck.cards[1]

    def deal_hand(self,num):
        self.num = num
        hand = []
        for i in range(0,self.num):
            hand.append(Deck.cards[i])
            Deck._deal(1)
        print(Deck.count())
        return hand

de = Deck() # create instance for Deck

de.shuffle() # shuffle our deck

c = de.deal_card() # test dealing single card

print(c)

h = de.deal_hand(2) # test dealing multiple cards

print(h)

h2 = de.deal_hand(49) # deal all remaining cards
c2 = de.deal_card() # this should raise value error as we have already dealt all cards
print(c2)