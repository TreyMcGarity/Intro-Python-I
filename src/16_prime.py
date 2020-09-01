num = input("Input a number to see if it's prime.")
if int(num) > 1:
   for i in range(2,int(num)): #from 2 to inputted number check..
       if (int(num) % i) == 0: #if num is divisable by value in range
           print("not Prime")  #no remainder means not prime
           break
   else:
       print("Prime!") #any remainder means prime
else:
   print("not Prime") #1 is not a prime number
