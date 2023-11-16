import pandas as pd
import numpy as np
from datetime import date

PRODUCT=[]
PRICE=[]
DATE=[]
TYPE=[]

def addexp(product,prices,date,type):
    PRODUCT.append(product)
    PRICE.append(prices)
    DATE.append(date)
    TYPE.append(type)

choice=-1
while(choice!=0):
    print("____________________________________________________")
    print("Welcome")
    print("____________________________________________________")
    print("1.Personal")
    print("2.Food")
    print("3.Common")
    print("4.Show Report")
    print("5.EXIT")

    choice=int(input("Please enter a choice:"))
    if(choice==5):
        print("Thanks for using our service")
        break
    elif(choice==1):
        print('Personal Expenses')
        type='Personal'
    elif(choice==2):
        print('Food Expenses')
        type='Food'
    elif(choice==3):
        print("Common Expenses")
        type='Common'
    elif(choice==4):
        print("Monthly Report")
        data=pd.DataFrame()
        data['PRODUCT']= PRODUCT
        data['PRICE']= PRICE
        data['DATE']= DATE
        data['TYPE']=TYPE
        data.to_csv('expence.csv')
        print(data)
        total=sum(float(x) for x in PRICE)
        print("Total Expense="+str(total))
    else:
        print('Please select a valid choice')
    if choice==1 or choice==2 or choice==3:
        product=input("Enter the product type:"+type+ ':\n')
        prices=float(input('Enter the price:'))
        today=date.today()
        addexp(product,prices,today,type)
    print()






    
