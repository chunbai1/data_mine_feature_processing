print("this is a simple interactive game, please enjoy it!")

name = input("Please input your name:")
level = input("Please input the game level(easy or midiem or hard):")

print("Ok! Let's begin!")
print("to be continued...")
print("ok! Let't going on!")
print("********************************")
direction = input("Now the tree in on your left, the car is on your right, the dog is infront of you, the wall is behind of you. Now is your turn to select:")
if direction == "behind":
    print("You Win!")
else:
    print("You Died!")