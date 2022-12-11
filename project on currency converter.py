# Project to make a currency Generator
currency={"USD":81.77,"EUR":84.71,"INR":1,"POUND":98,"CAD":61.11,"CNY":11.41,"RUB":1.35,"AED":22.41}
def convert(c1,a,c2):
    
        if(c2=="INR"):
            print("The Currency After Converting into %s is"%c2,(amount*currency[c1]))
        elif(c1=="INR"):
            print("The Currency After Converting into %s is"%c2,(amount/currency[c2]))
        else:    
            print("The Currency After Converting into %s is"%c2,(amount/currency[c1])*currency[c2])



print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
while(True):
    c1=input("Enter The Currency: ") #The Currency given
    amount=eval(input("Enter The Amount: ")) # The amount in the given currency
    c2=input("Enter The Currency you want to convert to: ") # The currency you want to covert the amountUSD
    convert(c1,amount,c2)
    x=input("Is you want to convert more(Y/N): ")
    if x=="N":
        print("                   ")
        print("-------------------")
        print("| Have a nice day |")
        print("-------------------")
        break
    else:
        continue
