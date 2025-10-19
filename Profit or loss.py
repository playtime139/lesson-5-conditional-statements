actual_cost = float(input("please enter the Actual product price: "))
sale_amount = float(input("please enter the Sale amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("NO profit!!")