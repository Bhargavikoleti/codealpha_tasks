def save_portfolio(stock, quantity, buy_price, current_price):
    with open("portfolio.txt", "a") as file:
        file.write(
            f"{stock},{quantity},{buy_price},{current_price}\n"
        )


portfolio = {}

while True:

    print("\n===== SMART INVESTMENT PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Search Stock")
    print("4. Remove Stock")
    print("5. Total Investment Value")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        stock = input("Enter stock name: ").upper()
        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter buying price: "))
        current_price = float(input("Enter current price: "))

        portfolio[stock] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "current_price": current_price
        }

        save_portfolio(stock, quantity, buy_price, current_price)

        print("Stock added successfully!")

    elif choice == "2":

        if len(portfolio) == 0:
            print("Portfolio is empty.")
        else:

            for stock, details in portfolio.items():

                value = details["quantity"] * details["current_price"]

                profit_loss = (
                    details["current_price"] -
                    details["buy_price"]
                ) * details["quantity"]

                print("\nStock:", stock)
                print("Quantity:", details["quantity"])
                print("Current Value:", value)
                print("Profit/Loss:", profit_loss)

    elif choice == "3":

        name = input("Enter stock name: ").upper()

        if name in portfolio:
            print(portfolio[name])
        else:
            print("Stock not found.")

    elif choice == "4":

        name = input("Enter stock to remove: ").upper()

        if name in portfolio:
            del portfolio[name]
            print("Removed successfully.")
        else:
            print("Stock not found.")

    elif choice == "5":

        total = 0

        for details in portfolio.values():
            total += (
                details["quantity"] *
                details["current_price"]
            )

        print("Total Investment Value =", total)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")