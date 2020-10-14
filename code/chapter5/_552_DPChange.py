def dynamicProgChange(money, coins):

    table = [0]
    currMoney = 1
    while currMoney<= money:
        minNumCoins = float('inf')
        for i in range(len(coins)):
            if currMoney >= coins[i]:
                numCoins = table[currMoney - coins[i]]
                if numCoins < minNumCoins:
                    minNumCoins = numCoins
        table.append(1+minNumCoins)
        currMoney +=1
    
    return table[money]


if __name__ == "__main__":
    
    print(dynamicProgChange(17002,[19,5,3,1]))