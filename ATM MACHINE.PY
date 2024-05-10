
import time

print("please insert your card properly")

time.sleep(5)

password=1234
secretno=int(input("enter the secretno:"))
  
balance=5000

if secretno==password:
    while True:
        print("""
            1==balance
            2==withdraw amount
            3==deposit balance
            4==exit
            """
            )
        try:
            option=int(input("Please Enter Your Choice"))
        except:
            print("Please Enter Valid Option")
        if option==1:
            print(f"your current balance is {balance}")
            print("====================================================================================")
            print("====================================================================================")
            print("====================================================================================")

        if option==2:
            withdraw_amount=int(input("please enter withdraw_amount"))
            print("====================================================================================")
            print("====================================================================================")
            print("====================================================================================")
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")
            print("====================================================================================")
            print("====================================================================================")
        if option==3:
            deposit_amount=int(input("please enter deposit_amount"))
            balance=balance+deposit_amount
            print("====================================================================================")
            print("====================================================================================")
            print(f"{deposit_amount} is credited to your account")
            print("====================================================================================")
            print("====================================================================================")
            print(f"your updated balance is {balance}")
            print("====================================================================================")
            print("====================================================================================")
        if option==4:
            break
else:
    print("wrong secretno please try again")