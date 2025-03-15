class Account : 
    def __init__(self, AccountID, AccountPassword):
        self.__AccountID= AccountID
        self.AccountPassword= AccountPassword

    def __showAccountID(self):
        print(self.AccountID)

accountOne = Account(4532, 2454)
print(accountOne.AccountID)
print(accountOne.showAccountID())