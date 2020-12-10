#This is basically the same as the previous iteration, but I combined the
#functions for scoring the hand into one function. Doing this, I was 
#able to cut down on some repeated actions and  very slightly increase 
#the efficiency

#I didn't comment this one as well, since the code is basically the same
#as the previous

import numpy as np
import time 
import csv

start = time.time()

#Import the hands
with open('p054_poker.csv', newline='') as csvfile:
    cards = list(csv.reader(csvfile))
    
#To score, let's make a 'score' list for each hand
#First value is the type of hand
#Let's say: 0 high card, 1 pair, 2 two pair, 3 three of kind, 4 straight, 
#5 flush, 6 full house, 7 four of a kind, 8 straight flush, 9 royal flush
#Second value is the high card, ie the tie breaker
#third value is the next tie breaker - if valid, straights only have 1 tiebreaker
#fourth is the next
#fifth is the next
#sixth is the last - again, if valid. depends on the hand how many tiebreakers
#We should never need to make it this far down the list of tiebreakers, but
#may as well include them
    
#My code does not account for the possibility of a tie - which could 
#possibly occur. Would not be that hard to add this to the 'game' function tho

def split_hand(hand_1):
    #This splits the hand into a list of lists for the hand.
    #Each nested list contains an integer for the value of the card
    #And a letter for the suit
    h_1 = []
    for j in range(0,len(hand_1)):
        if hand_1[j][0] == 'A':
            h_1.append([14,hand_1[j][1]])
        elif hand_1[j][0]=='T':
            h_1.append([10,hand_1[j][1]])
        elif hand_1[j][0]=='J':
            h_1.append([11,hand_1[j][1]])
        elif hand_1[j][0]=='Q':
            h_1.append([12,hand_1[j][1]])
        elif hand_1[j][0]=='K':
            h_1.append([13,hand_1[j][1]])
        else:
            h_1.append([int(hand_1[j][0]),hand_1[j][1]])
        
    return h_1
    
def score(hand):
    suit = []
    nums = []
    score=[]
    
    #Seperate out the suits and values of the cards
    for j in range(0,5):
        suit.append(hand[j][1])
        nums.append(hand[j][0])
    nums.sort()
    vals = set(nums)
    
    #The following block check for hands involving flushes - if it's a flush, it 
    #can't possibly be any other hand not involving a flush
    if len(set(suit)) == 1:
        if nums[0] == 10 and nums[4] == 14:
            score.append(9)
            score.append(nums[4])
        elif nums[4] - nums[0] == 4:
            score.append(8)
            score.append(nums[4])
        elif nums[3] - nums[0] == 3 and nums[0] == 2 and nums[4]==14:
            score.append(8)
            score.append(nums[3])
        else:
            score.append(5)
            for k in range(4,-1,-1):
                score.append(nums[k])
    
    #The following block checks for hands with 5 different valued cards
    #The only possibilites here are straight or high card
    #(Or flush, but we already checked for that in previous step)
    elif len(vals) ==5:
        if nums[4] - nums[0] == 4:
            score.append(4)
            score.append(nums[4])
        elif nums[3] - nums[0] == 3 and nums[0] == 2 and nums[4]==14:
                score.append(4)
                score.append(nums[3])
        else:
            score.append(0)
            for k in range(4,-1,-1):
                score.append(nums[k])
                
    #The following block checks for hands with 2 different valued cards
    #The only possibilities here are 4 of a kind or full house
    elif len(vals) == 2:
        vals = list(vals)
        count = [0,0]
        for num in nums:
            if num ==vals[0]:
                count[0]+=1
            elif num == vals[1]:
                count[1]+=1
        
        if max(count) == 3:
            score.append(6)
            score.append(vals[count.index(3)])
            score.append(vals[count.index(2)])
        elif max(count)==4:
            score.append(7)
            score.append(vals[count.index(4)])
            score.append(vals[count.index(1)])
     
    #The following block checks for hands with 3 different valued cards
    #The only possibilities here are 3 of a kind or 2 pair
    elif len(vals) ==3:
        vals = list(vals)
        count = [0,0,0]
        for num in nums:
            if num == vals[0]:
                count[0]+=1
            elif num == vals[1]:
                count[1]+=1
            elif num == vals[2]:
                count[2]+=1
        
        if max(count)==3:
            score.append(3)
            score.append(vals[count.index(3)])
            vals.remove(vals[count.index(3)])
            vals.sort()
            score.append(vals[1])
            score.append(vals[0])
        
        if max(count) == 2:
            score.append(2)
            pairs_index=[]
            for j in range(0,3):
                if count[j]==2:
                    pairs_index.append(j)
            
            pairs = [vals[pairs_index[0]],vals[pairs_index[1]]]
            pairs.sort()
            score.append(pairs[1])
            score.append(pairs[0])
            score.append(vals[count.index(1)])
     
    #The following block checks for hands with 4 different valued cards
    #The only possibility here is a pair
    elif len(vals) ==4:
        vals = list(vals)
        count = [0,0,0,0]
        for num in nums:
            for j in range(0,4):
                if num == vals[j]:
                    count[j]+=1
                    break
        score.append(1)
        score.append(vals[count.index(2)])
        vals.remove(vals[count.index(2)])
        vals.sort()
        score.append(vals[2])
        score.append(vals[1])
        score.append(vals[0])
        
    return score
            
def game(score_1,score_2):
    #Takes two hands and finds the winner
    #If winner = 1, score_1 wins. and if winner = 2, score_2 wins
    
    winner = 0
    if score_1[0] > score_2[0]:
        winner = 1
    elif score_1[0]< score_2[0]:
        winner = 2
    else:
        for j in range(1,len(score_1)):
            if score_1[j] > score_2[j]:
                winner = 1
                break
            elif score_1[j] < score_2[j]:
                winner = 2
                break
    return winner    
    
#Counts the number of games won
player1 = 0
player2 = 0      

#Iterates through each round
for i in range(0, len(cards)):
    
    #Splits the round into the two hands
    hand_1 = np.array(cards[i][0:5])
    hand_2 = np.array(cards[i][5:10])
        
    #Split each hand into a number and letter for each card
    h_1 = split_hand(hand_1)
    h_2 = split_hand(hand_2)
    
    #Score each hand, returning the score list
    score_1 = score(h_1)
    score_2 = score(h_2)
    
    #See who has the better hand
    #Add 1 game to the winner
    winner = game(score_1,score_2)
    if winner ==1:
        player1+=1
    elif winner ==2:
        player2+=1
    
    
print('Player 1 wins: ', player1)
print('Player 2 wins: ', player2)
print('Time is: ', time.time()-start)