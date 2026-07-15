class BankAccount:
  ROI = 10.5

  def __init__(self,A,B):
    self.Name = A
    self.CurrentAmount = B
    
  def Display(self):
   print(f"Account holder name is:{self.Name} and current Balance is:{self.CurrentAmount}")

  def Deposit(self):
    AddBalance = int(input("Enter Deposit amount:"))
    self.CurrentAmount = self.CurrentAmount  + AddBalance
    print("Current balance after deposit is:",self.CurrentAmount)

  def Withdraw(self):
    withdrawamount = int(input("Enter Withdraw Amount:"))
    if(withdrawamount > self.CurrentAmount):
      print("Not sufficient balance to withdraw")
    else:  
     withdraw_amount = self.CurrentAmount -withdrawamount
     print("after withdraw remaining BankBalance amount is :",withdraw_amount)
  
  def CalculateIntrest(self):
        Intrest = (self.CurrentAmount * self.ROI /  100)
        print(f"Based on this {self.ROI} rate of intrest :",Intrest)

def main():
  Name = input("Enter Account holder Name:")
  Amount= int(input("Enter Amount:"))
  bobj1 = BankAccount(Name,Amount)
  bobj1.Display()
  bobj1.Deposit()
  bobj1.Withdraw()
  bobj1.CalculateIntrest()
  print("Thank You For Using My Applicataion")

  print("_ "*78)

  Name = input("Enter Account holder Name:")
  Amount= int(input("Enter Amount:"))
  bobj2 = BankAccount(Name,Amount)
  bobj2.Display()
  bobj2.Deposit()
  bobj2.Withdraw()
  bobj2.CalculateIntrest()
  print("Thank You For Using My Applicataion")

  
if  __name__ == "__main__":
  main()
      
