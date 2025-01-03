class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.ratio=value/weight

def knapsack(weights,values,capacity):
    n = len(values)
    items = [Item(values[i], weights[i]) for i in range(n)]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value=0
    total_weight=0  # To track the total weight added
    for item in items:
        if capacity>=item.weight:
            # Take the entire item
            total_value+=item.value
            total_weight+=item.weight
            capacity-=item.weight
        else:
            # Take a fraction of the item
            total_value+=item.ratio*capacity
            total_weight+=capacity  # Adding the remaining capacity
            break
    
    return total_value,total_weight

weights=[2, 3, 5, 7, 1, 4, 1]
values=[10, 5, 15, 7, 6, 18, 3]
capacity=15

max_value,total_weight=knapsack(weights,values,capacity)
print(f"Total profit / Maximum value: {max_value:.2f}")
print(f"Total weight: {total_weight:.2f}")
