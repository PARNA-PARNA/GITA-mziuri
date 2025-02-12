class BankAccount:

    def __init__(self, account_holder, balance):
        if initial_balance < 0:
            raise ValueError
        self.__account_holder = account_holder
        self.__balance = balance


    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("თანხა არ შეიძლება იყოს 0 ზე ნაკლები")
        self.__balance += amount

    def withdraw(self,amount):
        if  amount <= 0:
            raise ValueError("გატანი თანხა უნდა იყოს 0 ზე მეტი")
        if  amount > self.__balance:
            raise ValueError("ბალანსზე არ არის საკმარისი თანხა")
        self.__balance -=amount


