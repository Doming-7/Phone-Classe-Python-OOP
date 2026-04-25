#Exercice 1
class Phone:
    def __init__(self,brand,model,storage,inStock):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.inStock = inStock

    def Afficher(self):
        if self.inStock == True:
            currently = "in stock"
        else:
            currently = "out of stock"
        print(f"{self.model} by {self.brand} has {self.storage}GB of storage and is currently {currently}")

p1 = Phone("Samsung","Galaxy S23",128,True)
p2 = Phone("Apple","Iphone 15 Pro",256,False)
p3 = Phone("Xiaomi","Redmi Note 12",64,True)

print("====Phone1====")
p1.Afficher()
print("====Phone2====")
p2.Afficher()
print("====Phone3====")
p3.Afficher()

#Exericce 2
class BankAccount:
    def __init__(self, owner, bank, balance, isActive):
        self.owner = owner
        self.bank = bank
        self.balance = balance
        self.isActive = isActive

    def Afficher(self):
        if self.isActive == True:
            current = "active"
        else:
            current = "inactive"
        print(f"{self.owner}'s account at {self.bank} has a balance of ${self.balance} and is {current}.")

acc1 = BankAccount("Alice", "Attijariwafa", 5000, True)
acc2 = BankAccount("Bob", "CIH Bank", 1200, False)
acc3 = BankAccount("Sara", "Banque Populaire", 8500, True)

print("====Account1====")
acc1.Afficher()
print("====Account2====")
acc2.Afficher()
print("====Account3====")
acc3.Afficher()