import math
import string
import random
class player(object):
    def __init__(self,bootamount):
        self.bootamount=bootamount

    def addplayeramount(self,amount):
        self.bootamount+=amount
        return self.bootamount

    def subtractplayeramount(self,amount):
        self.bootamount-=amount
        return self.bootamount
    
class card(object):
    def __init__(self,deck):
        self.deck=deck
    def playcard(self):
        return random.choice(self.deck)



class dealer(object):
    def __init__(self,dealerbootamount):
        self.dealerbootamount=dealerbootamount

    def adddealeramount(self,amount):
        self.dealerbootamount+=amount
        return self.dealerbootamount

    def subtractdealeramount(self,amount):
        self.dealerbootamount-=amount
        return self.dealerbootamount


def card_total():
    betAmount=0;
    dealerTotal=0;
    playerTotal=0;
    dealerCardSum=0;
    playerCardSum1=0;
    dealerAce=False;
    playerhit=True;
    dealerhit=True;
    d=dealer(1000)
    pl=player(1000)
    betAmount=int(input("Enter your bet amount for this round"))
    print(betAmount)
    while(playerhit or dealerhit):

        if(dealerhit):
                #print(dealerCounter)
                if(dealerCardSum<17):
                    score=c.playcard()
                    if(score=="A"):
                        if(dealerCardSum+11<=21):
                            dealerCardSum+=11
                        else:
                            dealerCardSum+=1
                    else:
                        dealerCardSum+=int(score)
                elif(dealerCardSum in range(17,22)):
                    option = input("Does the dealer want to hit or stand?")
                    if(option=='h'):
                        score=c.playcard()
                        if(score=="A"):
                            if(dealerCardSum+11<=21):
                                dealerCardSum+=11
                            else:
                                dealerCardSum+=1
                        else:
                            dealerCardSum+=int(score)
                    else:
                        dealerhit=False;
                elif(dealerCardSum>21):
                        print("dealer Bust")
                        break;

        print("dealer current total:",dealerCardSum)
        if(playerhit):
            if(playerCardSum1<22):
                optionplayer=input("Does the player want to hit or stand")
                if(optionplayer=='h'):
                    playerhit=True;
                    score=c.playcard()
                    if(score=="A"):
                        if(playerCardSum1+11<=21):
                            playerCardSum1+=11
                        else:
                            playerCardSum1+=1;
                    else:
                        playerCardSum1+=int(score)
                        print("player current total is:",playerCardSum1)
                else:
                    playerhit=False;
                    #break;                      
            else:
                 print("player bust")
                 break;

    if(dealerCardSum<22 and (dealerCardSum>playerCardSum1 or playerCardSum1>21)):
        print("dealer won")
        print("dealer money left:",d.adddealeramount(betAmount))
        print("player money left:",pl.subtractplayeramount(betAmount))
    elif(playerCardSum1<22 and (playerCardSum1>dealerCardSum or dealerCardSum>21)):
        print("Player won")
        print("player money left:",pl.addplayeramount(betAmount))
        print("dealer money left:",d.subtractdealeramount(betAmount))

    

c=card([2,3,4,5,6,7,8,9,10,"A"])
c.playcard()
card_total()


    
