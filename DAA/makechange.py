def make_change(amount, coins):
    change = []
    #desending order
    coins.sort(reverse=True)
    for coin in coins:
        if coin <= amount: 

            count = amount // coin
            amount = count * coin
            change.append((coin, count))
            return change
        
n = 437
c = [1000,5000,200,20,10,5,2,1]
change = make_change(n,c)
print(change)
                                                                                      
