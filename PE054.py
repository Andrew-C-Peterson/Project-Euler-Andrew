#Given 1000 poker hands between 2 players as a text file (i saved as csv)
#I want to find how many hands each player wins

#This is a bit messy and I could do some clean-up within the functions, 
#but overall this is pretty fast and I'm happy with it!

#I do some repeated actions within the functions - such as sorting values
#One way to improve efficiency is to streamline this and only do each action
#once.

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
#third value is the next tie breaker - if valid, some hands only have one
#fourth is the next
#fifth is the next
#sixth is the last - again, if valid. depends on the hand how many tiebreakers
    
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

def check_flush(hand):
    #Here, I check if all the cards are the same suit
    #Returns true or false
    suit = []
    for j in range(0,5):
        suit.append(hand[j][1])
    return len(set(suit)) == 1
    
def flush_scores(hand):
    #This checks for all hands that involve flushes
    score = []
    nums = []
    if check_flush(hand):
    #If it's a flush, we sort the numbers
    #If the highest is an A and the lowest is a 10, we know it's a royal flush
    
    #If the difference between the highest and lowest is 4, it's a straight flush
    #And also we need to check for the possibility of an A,2,3,4,5 straight
        
    #For straights, the tie breaker is the highest number in the straight
        
    #Finally, if it's not any kind of straight it's just a flush
    #The first tie breaker is the highest card, 2nd tiebreaker the 2nd high, etc.
        
    #If it's not a flush, I just report the score as 0
        for j in range(0,5):
            nums.append(hand[j][0])
            nums.sort()
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
    else:
        score.append(0)
        
    return score

def score_straight(hand):
    #Here, I check for straights
    #Again, if there are 5 different valued cards and the difference 
    #between the high and low is 4, it's a straight
    #And must also acount for the A, 2,3,4,5 straight
    #Tie breaker is the highest value in the straight
    
    #If it's not a straight and there are 5 different valued cards
    #The only possibility for the hand is high card
    #so this returns the score list for 'high card', with tie breakers
    
    score = []
    nums = []
    for j in range(0,5):
        nums.append(hand[j][0])
        nums.sort()
    vals = set(nums)
    
    if len(vals) == 5:
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
    else:
        score.append(0)
        for k in range(4,-1,-1):
            score.append(nums[k])
    return score

def Score_4k_FH(hand):
    #This function checks for 4 of a kind or full house
    #These both require having 2 different valued cards in the hand
    #For 4 of a kind, the first tie breaker is the value of 4 cards
    #The second tie breaker is the value of the other card
    #For full house, the first tie breaker is the value of the 3 cards
    #Second tie breaker is the value of the 2 cards
    
    #If it's neither of these, return 0
    score = []
    nums = []
    for j in range(0,5):
        nums.append(hand[j][0])
    vals = set(nums)
    
    if len(vals) == 2:
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
    else:
        score.append(0)
    return score

def pair_2pair_3k_score(hand):
    #This checks for 3 of a kind, 2 pair, and pair.
    #3 of a kind and 2 pair both require 3 different values of cards
    #For 3 of a kind, first tie breaker is the value of the 3
    #2nd is the value of the highest remaining, and the 3rd is the final card
    #For two pair, the first tie breaker is the highest pair
    #2nd is the lowest pair, and the 3rd is the final card
    
    #A pair requires 4 different values of cards
    #First tie breaker is the value of the pair, and then each 
    #following tie breaker is the highest remaining card
    
    #If it's none of these, returns 0
    score = []
    nums = []
    for j in range(0,5):
        nums.append(hand[j][0])
        nums.sort()
    vals = set(nums)
    
    if len(vals) ==3:
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
    else:
        score.append(0)

    return score

def score_hand(hand):
    #All right, this function determines the score list for the input hand
    
    #First, let's check if there's any flushes
    score = flush_scores(hand)
    
    #If it's a royal flush or straigh flush, we can just end it.
    #Those are the two highest possibilites.
    #IF it's a flush, there's no way we can have 4kind of FH.
    #So we will also just end it.
    if score[0] >= 8 or score[0]==5:
        return score
    else:
        #If it's 4 of a kind of a full house, we can just end it.
        #Those are the next two highest
        score_1 = Score_4k_FH(hand)
        
        if score_1[0] == 6 or score_1[0] == 7:
            return score_1
    #The next highest possibility is a straight, so let's check for that
    #If it is a straight, we can end it
    score_2 = score_straight(hand)
    if score_2[0] > 0:
        return score_2
    else:
        #If it's not a straight, we now check for pair, 2 pair, or 3 of a kind
        #If it's none of those, we the only thing left is high card
        
        score_3 = pair_2pair_3k_score(hand)
        if score_3[0]>0:
            return score_3
        else:
            return score_2
    
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
    score_1 = score_hand(h_1)
    score_2 = score_hand(h_2)
    
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
            