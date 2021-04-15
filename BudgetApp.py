#Budget App
#Create a Budget class that can instantiate objects based on different budget categories like food, 
# clothing, and entertainment. These objects should allow for
#1.  Depositing funds to each of the categories
#2.  Withdrawing funds from each category
#3.  Computing category balances
#4.  Transferring balance amounts between categories

class Budget:
    balance = 0

    def DepositFund (self):
        Deposit =int(input('How much would you like to deposit? \n'))
        self.balance += Deposit
        print('\nYour balance is: ', self.balance)
        print('Transaction Successful!')
    
    def WithdrawFund (self):
        Withdrawal =int(input('\nHow much would you like to withdraw? \n'))
        self.balance -= Withdrawal
        print('\nYour balance is: ', self.balance)
        print('Please take your cash!')

    def TransferFund (self, Category):
        Transfer = int(input('\nHow much would you like to transfer? \n'))
        self.balance -= Transfer
        Category.balance += Transfer
        print('Transaction Successful!')


#Food = Budget(3000, 500, 1000)

Food = Budget()
Clothing = Budget()
Food.DepositFund()
Food.WithdrawFund()
Food.TransferFund(Clothing)
Clothing.TransferFund(Food)
print(Food.balance)
print(Clothing.balance)


Clothing = Budget()
Clothing.DepositFund()
Clothing.WithdrawFund()
Clothing.TransferFund(Food)


Entertainment = Budget()
Entertainment.DepositFund()
Entertainment.WithdrawFund()
Entertainment.TransferFund(Clothing)