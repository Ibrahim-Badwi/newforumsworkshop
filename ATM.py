m=7000
r=2000
class ATM():
    def __init__(self,atmbalance,bankname):
        self.balance=atmbalance
        self.bank_name=bankname
while r>0:
    if r>=100:
        print "give 100"
        r=r-100
    elif r>=50:
        print "giv 50"
        r=r-50
    elif  r>= 10:
         print "give 10"
         r=r-10
    elif r>=5:
        print "give 5"
        r=r-5
    else:
        print "give 1"
        r=r-1