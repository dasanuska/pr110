import random

#Take a variable to store response to keep rolling a dice
response="y"

while response == "y":

    #Gnenerates a random number
    #between 1 to 6 (including
    # both 1 and 6)
    no = random.randint(1,6)

    #codition to check the number value
    if no ==1 :
        print("[_____]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[_____]")
    if no ==2 :
        print("[_____]")
        print("[  0  ]")
        print("[     ]")
        print("[    0]")
        print("[_____]")
    if no ==3 :
        print("[_____]")
        print("[  0  ]")
        print("[ 0   ]")
        print("[    0]")
        print("[_____]")
    if no ==4 :
        print("[_____]")
        print("[  0  ]")
        print("[ 0  0]")
        print("[ 0   ]")
        print("[_____]")
    if no ==5 :
        print("[_____]")
        print("[  0 0]")
        print("[ 0   ]")
        print("[ 0  0]")
        print("[_____]")
    if no ==6 :
        print("[_____]")
        print("[  0 0]")
        print("[ 0  0]")
        print("[ 0  0]")
        print("[_____]")

    #Ask user to enter a response
    response=input("press y to roll again and n to exit:")
    print("/n")