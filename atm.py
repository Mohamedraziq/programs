user={
    'pin' : 1234,
    'bal' : 5000
}
msg='''
--------------------
WELCOME TO AXIS BANK
--------------------
   1.cash withdraw
   2.bal enquiry
   3.cash deposit
   4.exit
'''
pin=int(input("enter your pin:"))
while True:
    if pin==user['pin']:
        print(msg)
        ch = int(input ("enter your choice[1-4]: "))
        if ch==1:
            cw= int(input("enter the amount: "))
            if cw>user['bal']:
                print("you dont have sufficient balance")
                print("you have",user["bal"],"rupees")
            else:
                user['bal']=user["bal"]-cw
                print(cw,"rupees successfully withdraw")
                print(user["bal"])
        if ch==2:
            print("you have",user["bal"],"rupees")
        if ch==3:
            cd=int(input("enter the amount to deposit: "))
            if cd<100:
                print("please deposit more than 100")
            else:
                user["bal"]=user["bal"]+cd
                print(cd,"rupees successfully deposited")
                print("you have",user['bal'],"rupees")
        if ch==4:
            print("thanks for using this bank")
            break
    else:
        print("you entered pin is wrong...!!")
        break