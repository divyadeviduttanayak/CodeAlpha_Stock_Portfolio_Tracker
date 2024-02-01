import requests
print(" \n \n ")
print ("welcome to CodeAlpha Stock Portfolio Tracker : ")
print("\n enter your stocks data  : \n")

api_key = "pk_59412382c5054b52b3e06358ed1c259d"
user_stock_data_list= []

def user_input():
    numb_of_stockes= int(input("enter no. of company in which you have invested : "))
    for i in range(numb_of_stockes) :
        symbol= input("enter company SYMBOL : ")
        initial_amount_perstock= int(input("Enter intial amount of that stock : "))
        numb_of_shares= int(input("enter quantity of shares : "))
        data_dict= { 
            "Symbol": symbol,
            "Initial_price": initial_amount_perstock,
            "No._of_shares_invested": initial_amount_perstock 
        }
        user_stock_data_list.append(data_dict)

def get_current_stock_price(symbol):
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["latestPrice"]

def performance_calculator():
    for data in user_stock_data_list :
        print ("Below is the Data of :"+data.get("Symbol"))
        current_stock_price= get_current_stock_price(data.get("Symbol"))
        print("Current Stock Price : "+str(current_stock_price))
        amount_invested = data.get("Initial_price")* data.get("No._of_shares_invested")
        print("Total amount you invested in this stock :"+str(amount_invested))
        current_amount= data.get("No._of_shares_invested")*current_stock_price
        print("current price of amount you invested: "+str(current_amount))
        if(current_amount > amount_invested):
            increament_amount= current_amount - amount_invested
            print("Increase in Amount :"+str(increament_amount))
            change_percentage= (increament_amount*100)/amount_invested
            print("increase percentage : +"+str(change_percentage))

        else :
            decrement_amount= amount_invested - current_amount
            print("Decrease in amount :"+str(decrement_amount))
            change_percentage= (decrement_amount*100)/amount_invested
            print(" Decrease percentage : -"+str(change_percentage))
        
       

user_input()
performance_calculator()

        





    