class Bank:
    BNAME = 'STATE BANK OF INDIA'
    def __init__(self,pin,bal):
        self.pin=pin
        self.bal=bal
    def Balcheck(self):
        count=0
        while count<3:
            if self.Checkpin()==self.pin:
                print('Availble Balance is :',self.bal)
                break
            else:
                print('Incorrect Password')
                count=count+1
    def Checkpin(self):
             password = int(input('Enter the your password:'))
             return password
            
    def deposite(self):
        amount=int(input('Enter the Amount:'))
        if amount<=100000:
            self.bal+=amount
            print('Deposited Successfully...')
            print('Availble Balance is:',self.bal)
        else:
            print('Deposite of maxiumm Amount is 100000')

    def withdraw(self):
        amount=int(input('Enter the Amount:'))
        if amount<=50000:
            self.bal-=amount
            print('Withdraw Successfully...')
            print('Availble Balance is:',self.bal)
        else:
            print('withdraw Maximum amount is 50000')
        
                 

user=Bank(4444,50000)
print(Bank.BNAME)
user.Balcheck()
user.deposite()
user.withdraw()
