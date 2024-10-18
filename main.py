'''
1 for stone 
-1 for paper 
0 for scissor
'''
import random
 
computer= random.choice([-1,0,1])
user=int(input("Enter -1 for stone 0 for paper 1 for scissor "))
dict={'stone':-1,'paper':0,'scissor':1}
rev_dict={-1:'stone',0:'paper',1:'scissor'}
print("Computer choose ", rev_dict[computer] )
print("you choose ",rev_dict[user])
if (computer == user):
    print("Its a Draw")
else:
    if (computer == -1 and user==1): 
        print("You lost!!!")
    elif (computer == 1 and user==-1):
        print("You won!!!")
    elif (computer == 0 and user==1): 
        print("You won!!!")
    elif (computer == 1 and user==0): 
        print("You lost!!!")
    elif (computer == -1 and user==0): 
        print("You won!!!")
    elif (computer == 0 and user==-1): 
        print("You lost!!!")
    else:
        print("Something went wrong or u might have entered wrong input")



