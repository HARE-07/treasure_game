print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("WELLCOME TO TE TREASURE ISLAND QUEST A ROAD TO PLEASURE ! NOW START")

person = input("do you want to start or not (y or n):-")

if person == "y":
    print("let go .....")
    start = input("select right or left (R/N) : ").lower()
    if start == "r":
        player = input("now choose swim or wait (s/w) :").lower()
        if player == "w":
            print("You choose to wait that great. now door will appear choose from them")
            player1 = input("choose any door from them : black_door, red_door, green_door (B/R/G):").upper()
            if player1 == "R":
                print("you selected red. it mean rose are red and you lose, your journey ended")
            elif player1 == "B":
                print("you choice was black_door, ayou win treasure of black devil king. you are winner")
            else:
                print("your choice was green , rest in peace ")
        else:
            print("you decided to swim such a impatient person . first drawn to death than eaten by crocodile")

    else:
        print("you were kill by  your lover.......")

else:
    print("you have end game, it your lose.....")
