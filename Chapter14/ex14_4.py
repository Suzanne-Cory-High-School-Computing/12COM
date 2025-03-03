# This is the code in Practice booklet 3 OOP in python
# The comments below explain how inheritance works (see comments on Parent class)

class Card:
    def __init__(self,value,suit): # constructor called automatically when a new Card object is created
        self.value = value # class Card has a variable called value
        self.suit = suit # class Card has a variable called suit
    
    def __str__(self):
        names = ['Jack','Queen','King','Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value,self.suit)
        else:
            return '{} of {}'.format(names[self.value-11],self.suit)
        
import random

class Card_group:
    def __init__(self, cards=[]): # constructor called automatically when a new Card_group object is created
        self.cards = cards # class Card_group has a variable called cards
    
    def nextCard(self): # class Card_group has a method called nextCard
        return self.cards.pop(0)
    
    def hasCard(self): # class Card_group has a method called hasCard
        return len(self.cards)>0
    
    def size(self): # class Card_group has a method called size
        return len(self.cards)
    
    def shuffle(self): # class Card_group has a method called shuffle
        random.shuffle(self.cards) # the random module has a method called shuffle
                                    # the shuffle() method takes in a the list and reorders the items

class Standard_deck(Card_group): # the Standard_deck class inherits from the Card_group class
    def __init__(self): # constructor called automatically when a new Standard_deck is created
        self.cards = [] # class Standard_deck has a variable called cards which is a list

        for s in ['Hearts','Diamonds','Clubs','Spades']:
            for v in range (2,15):
                self.cards.append(Card(v,s)) # iterate to create all the cards on the deck
                                            # and add them to the cards list in each Standard_deck object
                                            # 11 is Jack, 12 is Queen, 13 is King, 14 is Ace

deck = Standard_deck() # create a Standard_deck object and call it "deck"
deck.shuffle() # call the method shuffle() inside the Standard_deck object
                # because Standard_deck does not define a new method shuffle()
                # the shuffle() method of its parent Card_group will be used

new_card = deck.nextCard() # call the nextCard() method in the Standard_deck object we just instantiated called "deck"
                            # because the Standard_deck does not define a new method nextCard()
                            # the nextCard() method of its parent Card_group will be used

print('\n',new_card)
choice = input("Higher (h) or lower (l): ")
streak = 0

while (choice=='h' or choice=='l'):
    if not deck.hasCard(): # in the object deck of class Standard_deck that we instantiated, call the hasCard() method in the parent Card_group class
        deck = Standard_deck() # if the deck is now empty, create a new Standard_deck and assign it to "deck"
        deck.shuffle()

    old_card = new_card
    new_card = deck.nextCard()

    if (choice.lower() =='h' and new_card.value > old_card.value or
        choice.lower() == 'l' and new_card.value < old_card.value):
        streak = streak + 1
        print("Right! That's", streak, "in a row!")

    elif (choice.lower() =='h' and new_card.value < old_card.value or
        choice.lower() == 'l' and new_card.value > old_card.value):
        streak = 0
        print('Wrong.')
    
    else:
        print('Push.') # do nothing in this cycle in terms of streak/right/wrong.  we are just running deck.nextCard() again and placing the previous in old_card

    print('\n',new_card)
    choice = input("Higher (h) or lower (l): ")