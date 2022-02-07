class Category:
  def __init__(self,category):
    self.Category = category
    self.ledger = []
    self.balance = 0

    #print
  def __str__(self):
    title = self.Category.center(30,"*") + "\n"
    line = ""
    for i in self.ledger:
      i["amount"] = "%.2f" % i["amount"]
      spaces = " "*(30-(len(i["description"][:23]) + len(str(i["amount"]))))
      line+= (i["description"][:23] + spaces + str(i["amount"])).rjust(30) + "\n"
    total = f"Total: {self.balance}"
    output = title + line + total
    return output

  def deposit (self,amount,description=""):
    """
    A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    """
    if amount < 0:
      amount = amount * -1
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
  def withdraw (self,amount, description=""):
    """
    A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    """
    if  self.check_funds(amount) !=False:
      if amount > 0:
        amount = amount * -1
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount
      return True
    else:
      return False

  def transfer(self,amount,budgetcat):
    """
    A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    """
    if self.check_funds(amount) !=False:
      self.withdraw(amount, "Transfer to " + budgetcat.Category)
      budgetcat.deposit(amount, f"Transfer from {self.Category}" )
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    """
    A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    """
    if amount > self.balance:
      return False
    else:
      return True
### below this line everything is for create_spend_chart
  def get_withdraw(self):
    withdrawtotal = 0
    for item in self.ledger:
      if item["amount"]<0:
        withdrawtotal += item["amount"]
    return round(withdrawtotal,2)

  def get_totals(categories):
    total = 0
    loneints = []
    for cat in categories:
      total += cat.get_withdraw()
      loneints.append(cat.get_withdraw())
    percentage = list(map(lambda x: x/total),loneints)
    return percentage

def create_spend_chart(category):

  # round number to multipale of 10
  def round_down(num):
    return num - (num%10)

  withdrawals_list= [a.get_withdraw() for a in category]
  
  # sum of all category total withdrawals  
  total_withdrawals = 0
  for item in withdrawals_list:
    total_withdrawals += item

  catpercent = []
  for value in withdrawals_list:
    percentage = (value / total_withdrawals)*100
    # round percentage multipale of 10
    roundpercent = round_down(percentage)
    catpercent.append(roundpercent)


  # for chart part: 
  result = "Percentage spent by category\n"
  line = "    " + "".join(["-" for i in range(len(category) * 3 + 1)])
  barra = ""
  for i in range(100, -1, -10):
    if i == 100:
      barra = "100| "
    elif i == 0:
      barra = "  0| "
    else :
      barra = " " + str(i) + "| "

    for item in catpercent:
      if i <= item:
        barra += "o  "
      else:
        barra += "   "
    result += barra + "\n"  
  result += line + "\n"

  # for name printing : 
  maxnamelen = 0
  for i in category:
    if len(i.Category) > maxnamelen:
      maxnamelen = len(i.Category)
  for i in range(maxnamelen):
    result += "    "
    for c in category:
      if i < len(c.Category):
        result += " " + c.Category[i] + " "
      else:
        result += "   "
    if i == maxnamelen - 1:
      result += " "
    else:
      result += " \n"


  return result 
