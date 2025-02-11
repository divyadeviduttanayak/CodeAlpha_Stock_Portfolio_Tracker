import yfinance as yf

print("\n\nWelcome to CodeAlpha Stock Portfolio Tracker : ")
print("\nEnter your stocks data:\n")

user_stock_data_list = []

def user_input():
    try:
        numb_of_stocks = int(input("Enter no. of companies in which you have invested: "))
        for i in range(numb_of_stocks):
            symbol = input("Enter company SYMBOL: ").upper().strip()
            initial_amount_per_stock = float(input("Enter initial price of that stock: "))
            numb_of_shares = int(input("Enter quantity of shares: "))
            
            data_dict = {
                "Symbol": symbol,
                "Initial_price": initial_amount_per_stock,
                "No_of_shares_invested": numb_of_shares
            }
            user_stock_data_list.append(data_dict)
    except ValueError:
        print("Invalid input! Please enter numbers where required.")
        user_input()

def get_current_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
        return round(current_price, 2)
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

def performance_calculator():
    for data in user_stock_data_list:
        symbol = data.get("Symbol")
        print(f"\nBelow is the data for: {symbol}")
        
        current_stock_price = get_current_stock_price(symbol)
        
        if current_stock_price is None:
            print(f"Skipping {symbol} due to missing stock price data.")
            continue
        
        print(f"Current Stock Price: {current_stock_price}")
        
        amount_invested = data["Initial_price"] * data["No_of_shares_invested"]
        print(f"Total amount invested: {amount_invested}")

        current_amount = data["No_of_shares_invested"] * current_stock_price
        print(f"Current value of investment: {current_amount}")

        if current_amount > amount_invested:
            increment_amount = current_amount - amount_invested
            change_percentage = (increment_amount * 100) / amount_invested
            print(f"Increase in Amount: +{increment_amount}")
            print(f"Increase Percentage: +{change_percentage:.2f}%")
        else:
            decrement_amount = amount_invested - current_amount
            change_percentage = (decrement_amount * 100) / amount_invested
            print(f"Decrease in Amount: -{decrement_amount}")
            print(f"Decrease Percentage: -{change_percentage:.2f}%")

# Run program
user_input()
performance_calculator()
