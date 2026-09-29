def fratcional_knashap(item_wt, price, capacity):

    n = len(item_wt)

    items = [(price[i],item_wt[i], price[i]/item_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i +1 , n):
            if (items[i][2] < items[j][2]):
                items[i] , items[j] = items[j] , items[i]

    profit = 0.0

    for price, item_wt , priceperkg in items:
        if (capacity >= item_wt):
            capacity = capacity - item_wt
            profit = profit + price
        else: 
            profit = profit + (capacity * priceperkg)

    print("total Profit : ", profit)

price = [24, 21, 12, 10]
item_wt = [7, 3, 4, 5]
capacity = 20

fratcional_knashap(item_wt, price, capacity)