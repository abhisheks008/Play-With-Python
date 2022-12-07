import random

def display(pout):
    if pout==1:
        print("|       |")
        print("|   0   |")
        print("|       |\n")
    elif pout==2:
        print("| 0     |")
        print("|       |")
        print("|     0 |\n")
    elif pout==3:
        print("| 0     |")
        print("|   0   |")
        print("|     0 |\n")
    elif pout==4:
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |\n")
    elif pout==5:
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |\n")
    elif pout==6:
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |\n")
print(" WHO DARES WIN GAME \n")
print("Here, You will begin with the position start and you have to reach till position Dare 30 by rolling the dice if you complete the all the dares which comes in your path You will win the Game")
print("And lucking if you are at position Dare 25 and you got 6 then you will automatically shift to the Dare 30 and so on\n")
print("Welcome to the Game, you are now at position Start\n")
print("Roll the Dice to know your Dare\n")

Dare1='You are at Dare 1 so Pick the third number on your contacts list and message them a silly poem.'
Dare2='You are at Dare 2 so Open up all your windows and sing an entire song as loud as you can.'
Dare3='You are at Dare 3 so Take a video of yourself doing a crazy dance and post it to social media.'
Dare4='You are at Dare 4 so Walk around the block and talk to yourself the entire time, even when people are around.'
Dare5='You are at Dare 5 so Brush your teeth with peanut butter or another condiment and send me a pic.'
Dare6='You are at Dare 6 so Pretend to be a cat for five minutes and send a video to your friend.'
Dare7='You are at Dare 7 so Find the spiciest thing in your house and eat an entire spoonful of it.'
Dare8='You are at Dare 8 so Knock on someones door and try to run away before they answer!'
Dare9='You are at Dare 9 so Message someone you have not talked to in at least 1 year on Facebook or Instagram'
Dare10='You are at Dare 10 so Act out the I am the King of the World” scene from Titanic with a partner of your choice'
Dare11='You are at Dare 11 so Act like a mime for 5 minutes, Mimes do not talk; do not forget that.'
Dare12='You are at Dare 12 so Find the nearest pole or pillar and give the group your best pole dance.'
Dare13='You are at Dare 13 so Call a restaurant and try to order food in a foreign language. If you do not speak another language, use a foreign accent.'
Dare14='You are at Dare 14 so Learn how to say “I love you” in another language and say it to 5 random people on the street.'
Dare15='You are at Dare 15 so Go into an elevator and stand in the corner facing the wall. Keep doing it until three people have gotten on. It sounds like a horror movie does not it? Do not laugh while you are in there.'
Dare16='You are at Dare 16 so Go to a random person on the street and ask if you could buy their shirt. If they say yes, you have to buy it!'
Dare17='You are at Dare 17 so Walk in the street where there is a small crowd and talk to yourself in a loud voice.'
Dare18='You are at Dare 18 so Run to a group of strangers, pretend to cry, and tell them you are lost.'
Dare19='You are at Dare 19 so Call your parents and tell them you are in jail. This is why it is under the storyteller category. Be as believable as possible!'
Dare20='You are at Dare 20 so Let someone draw on your face with a permanent marker.'
Dare21='You are at Dare 21 so Let the friends give you a complete makeover.'
Dare22='You are at Dare 22 so Draw a moustache and glasses on your face.'
Dare23='You are at Dare 23 so Balance a cup of water on your head for 3 minutes. If you fail, you have to do it again until you succeed.'
Dare24='You are at Dare 24 so You need to be the servant of your friend for 10 minutes'
Dare25='You are at Dare 25 so Call a bestfriend, pretend it is his/her birthday, and sing Happy Birthday to You.'
Dare26='You are at Dare 26 so Play air guitar for one minute.'
Dare27='You are at Dare 27 so Read aloud the most personal text you have sent in recent days.'
Dare28='You are at Dare 28 so Ask a neighbor if they have fifty cents.'
Dare29='You are at Dare 29 so Order five pizzas to your house right now and give them to your neighbor.'
Dare30='You are at Dare 30 so Pretend to be playing a sport in your living room untill your family see you'


response=str(input("Press D to roll "))
if (response=='D' or response=='d'):
    pout=(random.randint(1, 6))
    display(pout)
    i=pout
    while i<30:
        if i==1:
            print (Dare1)
        elif i==2:
            print (Dare2)
        elif i==3:
            print (Dare3)
        elif i==4:
            print (Dare4)
        elif i==5:
            print (Dare5)
        elif i==6:
            print (Dare6)
        elif i==7:
            print (Dare7)
        elif i==8:
            print (Dare8)
        elif i==9:
            print (Dare9)
        elif i==10:
            print (Dare10)
        elif i==11:
            print (Dare11)
        elif i==12:
            print (Dare12)
        elif i==13:
            print (Dare13)
        elif i==14:
            print (Dare14)
        elif i==15:
            print (Dare15)
        elif i==16:
            print (Dare16)
        elif i==17:
            print (Dare17)
        elif i==18:
            print (Dare18)
        elif i==19:
            print (Dare19)
        elif i==20:
            print (Dare20)
        elif i==21:
            print (Dare21)
        elif i==22:
            print (Dare22)
        elif i==23:
            print (Dare23)
        elif i==24:
            print (Dare24)
        elif i==25:
            print (Dare25)
        elif i==26:
            print (Dare26)
        elif i==27:
            print (Dare27)
        elif i==28:
            print (Dare28)
        elif i==29:
            print (Dare29)
        print("\nif you complete your dare then")
        check=str(input("Press D for next Task "))
        if(check=='d'or check=='D'):
            nout=(random.randint(1, 6))
            display(nout)
        else:
            print("You are Exit,Thank you")
        i+=nout
        if(i>30 or i==30):
          print(Dare30)
          final=str(input("Press D if you done with your Dare "))
          if(final=='d' or final=='D'):
            print("\nYou Win")
          else:
            print("You are Exit,Thank you")
else:
    print("You are Exit,Thank you")
