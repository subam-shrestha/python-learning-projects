name = input("What's your name?: ")
n = int(input("Pick a number from 1-10:"))
color = input("pick a color (red/blue/green): ")
if n>=5 and color=="red":
    print(f"{name}, you will be a hoe CONGRATS!!")
elif n <= 5 and (color == "green" or color == "red" or color == "blue"):
    print(f"{name}, you wont be a hoe at the very least, CONGRATS!!")
elif n>=5 and color=="blue":
    print(f"{name}, You will successfull person MARK MY WORDS!!")
else:
    print(f"{name}, Man you mysterious asf i dont know u might just be a bat man or the greatest person alive")