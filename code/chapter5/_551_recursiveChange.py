def recursiveChange(money, coins):

    # implementation of pseudocode in https://stepik.org/lesson/369313/step/5?unit=354733

    if money == 0:
        return 0
    
    minNumCoins = float('inf')

    for i in range(len(coins)):
        if money >= coins[i]:
            numCoins = recursiveChange(money - coins[i], coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins

if __name__ == "__main__":
    

    print(recursiveChange(76,[5,4,1]))