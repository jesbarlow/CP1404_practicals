items = int(input("Please enter the number of items:"))
if items <= 0:
    print("Invalid number of items")
    items = input("Please enter the number of items:")

prices = []
count = 0

for i in range(items):
    count = count + 1
    item_cost = float(input("What is the price of item {}?: $".format(count)))
    prices.append(item_cost)

num = 0
for elem in prices:
    num = num + 1
    print("The cost of item {} is:".format(num))
    print ("${:,.2f}".format(elem))


print("The total cost of all items is: $",sum(prices))












