#wipro
#Best Day to Trade
#scenario: A trader records stock prices daily. Find the maximum profit by buying once and selling once.
price=eval(input("enter list: "))
minPrice=price[0]
maxProfit=0
for i in range(1, len(price)):
    if price[i] < minPrice:  #this will update minPrice is smaller than current price.
        minPrice = price[i]
    elif price[i] - minPrice > maxProfit:
        maxProfit = price[i] - minPrice
print(maxProfit)

#input:enter list: [7,1,5,3,6,4]
#output:5