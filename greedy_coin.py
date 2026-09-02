#Greedy Coin Calculator
coins = [25,20,10,5,1]
amount, count, i = 63, 0, 0

while amount > 0:
    if coins[i] <= amount:
        amount -= coins[i] #Subtract coin
        count += 1
    else:
        i += 1
print(f"Minimum coins: {count}")  