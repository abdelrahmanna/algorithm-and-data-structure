def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    currentProfit = 0
    lowDay = None 
    for i in prices:
        if not lowDay:
            lowDay = i
            continue
        
        if lowDay > i:
            lowDay = i
            print("in:", i)
        else:
            print("in2:", i, lowDay)
            
            possibleProfit = i - lowDay
            if possibleProfit > currentProfit:
                currentProfit = possibleProfit
    return currentProfit


if __name__ == "__main__":
    print(maxProfit([2,1,2,1,0,1,2]))