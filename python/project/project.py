# class ATM:
#     def __init__(self):
#          self.bal = 600000
#          self.a= int(input("enter your deposit money:"))
#          self.b = int(input("enter your withdraw money:"))

#     def deposit_money(self):
#          print("enter your deposit money:",self.a)

#     def withdraw_money(self):
#             print("enter withdraw money:",self.b)


#     def check_balance(self):
#          if self.a>0:
#               if self.b>0:
#                    self.bal= self.bal + self.a - self.b
#               else:
#                    self.bal = self.bal -self.b
#          else:
#               self.bal = self.bal+self.a
              
#               print("check balance:",self.bal)


# a =ATM()
# a.deposit_money()
# a.withdraw_money()
# a.check_balance()

                


class BMICalculator:
    def __init__(self):
        self.w = float(input("enter weight in kg:"))
        self.h = float(input("enter height in cm:"))
        self.sm= "sm"
    def height(self):
          c= self.h / 100
          self.sm= c*c
          print("height is in meter",self.sm)
    def weight(self):
          print("wight in kg",self.w)
    def calculate_bmi(self):
     bmi = self.w / self.sm
     print("body mass index",bmi)

     if bmi<16:
      print("severe thinness",bmi)
     elif bmi>16 or bmi<17:
      print("moderate thinness",bmi)
     elif bmi >17 or bmi<18.5:
      print("mild thinness",bmi)
     elif bmi>18.5 or bmi<25 :
      print("normal",bmi)
     elif bmi>25 or bmi<30:
      print("overweight",bmi)
     elif bmi >30 or bmi<35:
      print("obese class 1",bmi)
     elif bmi>35 or bmi<40:
      print("obsese class 2",bmi)
     else:
      print("obsese class 3",bmi)          
b = BMICalculator()
b.weight()
b.height()
b.calculate_bmi()



class BMICalculator:
  def __init__(self):
    self.w = float(input("enter weight in kg"))
    self.h = float(input("enter height in cm"))
    self.b = "b"
    self.c = "c"

  def weight(self):
      self.b= self.w*2.20
      print("your weight in pound",self.b)
  def height(self):
        d =self.h/2.54
        self.c = d*d
        print("your height in inches squre",self.c)
  def calculate_bmi(self):
        bmi = self.b/self.c
        bmi*703
        print("body mass index",bmi)
        if bmi <16:
           print("severe thinness",bmi)
        elif bmi>16 or bmi<17:
           print("moderate thinness",bmi) 
        elif bmi >17 or bmi<18.5:
           print("mild thinness",bmi)
        elif bmi>18.5 or bmi<25 :
            print("normal",bmi)
        elif bmi>25 or bmi<30:
            print("overweight",bmi)
        elif bmi >30 or bmi<35:
           print("obese class 1",bmi)
        elif bmi>35 or bmi<40:
          print("obsese class 2",bmi)
        else:
         print("obsese class 3",bmi)          
b = BMICalculator()
b.weight()
b.height()
b.calculate_bmi()



class Atm:
   def __init__(self,):
#       self.d = int(input("enter your deposit money"))
#       self.w = int(input("enter your withdraw money"))
#       self.bal = 20000
#    def balance_check(self):
#       if self.d>0:
#             if self.w>0:
#                self.bal = self.bal +self.d
#             else:
#                self.bal = self.bal-self.w
#       else:
#             self.bal = self.bal+self.d-self.w

#             print("deposited money",self.d)
#             print("withdreawal money",self.w)
#             print("check balance",self.bal)

# a = Atm()
# a.balance_check()




