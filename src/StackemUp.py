import itertools
import sys

class Card:
    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"{self.value} of {self.suit}"
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.initDeck()
    def initDeck(self):
        combination = list(itertools.product(self.suits, self.values))
        self.cards = []
        self.cards.append(None)
        for suit,value in combination:
            card = Card(value, suit)
            self.cards.append(card)
    def __str__(self):
        result = ""
        for card in self.cards:
            if card is None:
                continue
            result += (str(card) + "\n")
        return result.rstrip()
    def swapCardsPosition(self, cardIndex, newIndex):
        card = self.cards[cardIndex]
        self.cards.pop(cardIndex)
        self.cards.insert(newIndex, card)


    

class Shuffle:
    def __init__(self, info):
        self.info = info
    def shuffleCards(self, deck):
        newDeck = [None]
        for cardIndex in self.info:
            newDeck.append(deck.cards[int(cardIndex)])
        deck.cards = newDeck
        return deck
            
            




class StackemUp:
    def __init__(self):
        self.run()
    def run(self):
        cases = int(input())
        for case in range(cases):
            deck = Deck()
            n = input()
            if n == '':
                n = input()
            n = int(n)
            shuffles = []
            for i in range(n):
                shuffleInfo = input().split(" ")
                shuffle = Shuffle(shuffleInfo)
                shuffles.append(shuffle)
            shuffleOrder = []
            while True:
                try:
                    shuffleOrder.append(int(input()))
                except:
                    break
            for k in shuffleOrder:
                deck = shuffles[k-1].shuffleCards(deck)
            print(deck)

            
            