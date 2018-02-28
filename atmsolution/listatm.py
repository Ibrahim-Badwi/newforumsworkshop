
class ATM():
    def __init__(self,atm_balance,bank_name):
        self.balance=atm_balance
        self.bank_name=bank_name
        self.withdrawal_list=[]
   

    def withdraw(self,request):
        self.print_sep() 
        print "CURRENT BALANCE="+str(self.balance)
        print "Request="+str(request)
        if request > self.balance:
            print("Can't give you all this money !!")
        elif request <= 0:
            print("More than zero plz!")
        else:
            self.withdrawal_list.append(request)
            self.balance-=request
            allowed_paper=[100,50,10,5]
            for i in allowed_paper:
               
                while request>=i:
                    print "give "+str(i)
                    request-=i
            if request>0:
                print "give "+str(request)
                request=0
        return self.balance

    def print_sep(self):
        sep="-"*25
        print sep
        print "Wellcom to "+self.bank_name

    def show_withdrawal(self):
        self.print_sep()
        for withdrawal in self.withdrawal_list:
            print"withdrawal:"+str(withdrawal)
            
balance1=10000
balance2=2000
atm1=ATM(balance1,"HSBC")
atm2=ATM(balance2,"Baraka Bank")
atm1.withdraw(674)
atm1.withdraw(700)
atm1.withdraw(170)
atm1.show_withdrawal()

atm2.withdraw(1000)
atm2.withdraw(700)
atm2.withdraw(113)
atm2.withdraw(2000)
atm2.show_withdrawal()

