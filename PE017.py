#Count letters in numbers
one = "one"
two="two"
three="three"
four="four"
five="five"
six="six"
seven="seven"
eight="eight"
nine="nine"

length=0
for i in range(1,10):
    if i == 1:
        number=one
    elif i ==2:
        number = two
    elif i ==3:
        number = three
    elif i ==4:
        number = four
    elif i ==5:
        number = five
    elif i ==6:
        number = six
    elif i ==7:
        number = seven
    elif i ==8:
        number = eight
    elif i ==9:
        number = nine
        
    length=length+len(number)
#for 10-19    
length = length + len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
#for 20-99

length=length+(10*(6+6+5+5+5+7+6+6)+8*36)

