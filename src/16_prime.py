num = input("Input a number to see if it's prime.")
if int(num) % 2 == 0 and int(num) % 3 == 0 and int(num) % 5 == 0 and int(num) % 7 == 0:
    print("Not prime.")
else:
    print("Prime!")
    