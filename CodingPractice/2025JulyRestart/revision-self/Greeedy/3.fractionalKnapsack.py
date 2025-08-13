items = [[20, 100], [30, 120], [10, 60]]
capacity = 50


def fractional_knapsack(capacity, items):
    items = [ [x,y,y/x] for x,y in items ]
    items.sort(key=lambda x : x[2], reverse=True)
    val = 0
    i= 0
    res = 0
    while res <= capacity and i < len(items):
        if items[i][0] <= (capacity - res):
            res += items[i][0]
            val += items[i][0] * items[i][2]
        else:
            val += ((capacity - res)) * items[i][2]
            res += (capacity - res)

        # print("\nValue now : ", val)
        # print("Total Weight Takend : ", res)
        i += 1

    print("\nValue now : ", val)

    # print("\nSummary : ", items)

'''
fill the knapsack
such the value of the items wight in knapsack is maximmum and the toal is outmost

where, items can be broken down to maximise the knapsack value

approach:
get the value of item per unit 
arrange in descending order
consume the items until the weight allows
consume the fraction of the last item as much remained and respective value of the fraction taken


'''

fractional_knapsack(capacity, items)