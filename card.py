"""
Egor Eliseev
11/27/16
Module that allows user to play BlackJack
"""
#Import two functions (randit and choice) from random
from random import randint, choice
#Define a class Card
class Card():
    #Define __init__ function to initialize a card
    def __init__(self,rank,suite):
        if (int(rank) > 13) or (int(rank) < 1):
            print ("Value of a card should be from 1 to 13")
        else:
            self.rank = rank
            self.suite = suite
    #Define a function that returns a rank of a card
    def getRank(self):
        return self.rank
    #Define a function that returns a suit of a card
    def getSuit(self):
        return self.suite
    #Define a function that returns the game value of a card
    def getBJValue(self):
       #Let the user choose a value for the Ace (either 1 or 11)
       if self.rank == 1:
            if input('How do want to count your Ace?(1 or 11) ') == '1':
                return 1
            else:
                return 11
        #if rank of a card is less than 10, then return it
       if self.rank < 10:
            return self.rank
       self.rank = 10
       return self.rank
    #Define a function that returns a verbous description of card
    def __str__(self):
        cardSuite = str() #empty variable for a card suit
        cardRank = 0 #empty variable for a card rank
        #Two dicitionaries with full values that correspond to short values of a card
        suite = {'s':'Spades','d':'Diamonds','c':'Clubs','h':'Hearts'}
        faceCard = {'1':'Ace','11':'Joker','12':'Queen','13':'King'}
        #Check for facecard or Ace
        if self.rank > 10 or self.rank == 1:
            cardRank = faceCard[str(self.rank)]
        else:
            cardRank = self.rank
        #Get the suit for a card
        cardSuite = suite[self.suite]
        #returned string with full name of a card
        return '{} of {}'.format(cardRank, cardSuite)

#Define a function that lets user to draw, function recieves: total value of players hand(named total, and equals to zero by default), number of card (also zero by default), and empty list to hold all cards
def draw(total = 0, cardNumber = 0, cards = []):
    #List with short values for a card suit
    suites = ['s','d','c','h']
    #Creating a random card
    cards.append(Card(randint(1, 13), choice(suites)))
    #Output of what card user recieved (name)
    print ('You got a {}'.format(cards[cardNumber]))
    #Add the value of card to total
    total+=int(cards[cardNumber].getBJValue())
    #Incriment the number of card
    cardNumber+=1
    while total < 21:
        #Print the current total
        print ('Your current total is: {}'.format(total))
        #Ask a user if he want's to draw a new card
        if input('You want to draw another card?(y or n): ') == 'y':
            #If yes recall the function
            draw(total, cardNumber, cards)
        else:
            #If not show the total of his hand
            print ('Your hand equals to {}'.format(total))
        break
    else :
        if total == 21:
            print ('Congratulations you hit 21!')
        else:
        #If user hit more than 21 print his lost hand
            print ('You lost with total of {}'.format(total))
