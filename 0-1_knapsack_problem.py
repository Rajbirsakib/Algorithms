def knapsack(item_numbers,values,weights,capacity):
    n=len(values)
    # Create a DP table
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # Fill the DP table
    for i in range(1,n+1):
        for w in range(1, capacity+1):
            if weights[i-1]<=w:  # Item can fit in the current knapsack
                dp[i][w]=max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])  # Exclude the item, Include the item
            else:  # Item cannot fit
                dp[i][w]=dp[i-1][w]

    # Backtrack to find the selected items
    selected_items =[]
    w=capacity
    for i in range(n,0,-1):
        if dp[i][w]!= dp[i-1][w]:  # Item was included
            selected_items.append(item_numbers[i-1])  # Add item number from the list
            w -=weights[i-1]

    selected_items.reverse()  # Reverse to maintain the order of items
    return dp[n][capacity], selected_items

item_numbers=[1, 2, 3, 4] # Item numbers
values=[4, 3, 6, 5] # Values of items
weights=[3, 2, 5, 4] # Weights of items
capacity=5 # Maximum capacity of the knapsack

max_value, selected_items=knapsack(item_numbers,values,weights,capacity)
print("Maximum value:", max_value)
print("Selected item:", selected_items)
