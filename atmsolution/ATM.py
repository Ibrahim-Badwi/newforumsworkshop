
class ATM():
    def __init__(self,atm_balance,bank_name):
        self.balance=atm_balance
        self.bank_name=bank_name
        


    def withdraw(self,request):
        print "----------------------------"
        print "Wellcom to "+self.bank_name 
        print "Request="+str(request)
        print "CURRENT BALANCE="+str(self.balance)
        result=self.balance
        if request > self.balance:
            print("Can't give you all this money !!")
        elif request <= 0:
            print("More than zero plz!")
        else:
            result=self.balance-request
            while request>0:

                if request>=100:
                    print "give 100"
                    request-=100
                elif request>=50:
                    print "give 50"
                    request-=50
                elif request>= 10:
                    print "give 10"
                    request-=10
                elif request>=5:
                    print "give 5"
                    request-=5
                else:
                    print ("give"+str(request))
                    request=0
        return result 

            
balance1=1000
balance2=500
atm1=ATM(balance1,"HSBC")
atm2=ATM(balance2,"Baraka Bank")


atm1.withdraw(670)
atm1.withdraw(2000)
atm2.withdraw(300)


