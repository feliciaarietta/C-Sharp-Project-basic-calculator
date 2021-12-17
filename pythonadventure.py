print ("Welcome to my first game!")
name= input ("What is your name? ")
age= int (input ("What is your age? "))
print("Hello", name, "You are", age, "years old.")

health= 10
print ("You are starting with",health, "health" )

if age >= 18:
    print("You are old enough to play!")


    wants_to_play= input ("Do you want to play?").lower()
    if wants_to_play== "yes":
        print("Let's play!")

        left_or_right= input("First choice....Left or Right (left/right)?")
        if left_or_right== "left":
            ans = input("Nice,you follow the path and reach the lake...Do you swim across or go around (across/ around)? ")

            if ans== "around":
                print("You went around and reached the other side of the lake ")

            elif ans== "across":
                print ("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans= input("You notice a house and the river. Which do you go to (river/house)? ")
            if ans=="house":
                print ("You go to the house and are greeted by the owner...He doesn't like you and you lose 5 health")
                health -= 5

                if health <=0:
                    print("You now have 0 health and you lose the game...")
                else:
                    print("You have survived...You win!")
            else:
                print( "You fell down and lost")


        else:
            yes_or_no = input ("You have to go to the jungle. Do you want to continue? (yes/no)? ").lower()
            if yes_or_no== "yes":
                ans= input("Now you're in the jungle. Someone is watching. Do you want to (hide/attack?) ")

                if ans == "hide":
                    print("Do nothing and wait for help...")

                elif ans == "attack":
                    ans= input("Ready your weapon... Choose your weapon (sword/arrow)")
                    if ans== "sword":
                        print("You win!")
                    elif ans== "arrow":
                        print("You missed the target. You lost!")



            else:
                print("Back to the start.")

    else:
        print("See ya")

elif age >= 14:
    print("You can play with supervision")
else:
    print("You are not old enough to play...")


