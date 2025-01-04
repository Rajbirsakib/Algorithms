def rod_cutting(lengths,prices,n):
    # Initialize the DP array and a tracker for the selected lengths
    dp=[0]*(n+1)
    selected_lengths=[-1]*(n+1)  # To track cuts for each length

    # Build the DP array iteratively
    for i in range(1,n+1):
        for j in range(len(lengths)):
            if lengths[j]<=i:  # Only consider valid cuts
                if dp[i]<prices[j]+dp[i-lengths[j]]:
                    dp[i]=prices[j]+dp[i-lengths[j]]
                    selected_lengths[i]=lengths[j]  # Track the length chosen

    # Reconstruct the selected lengths
    result_lengths=[]
    current_length=n
    while current_length>0:
        result_lengths.append(selected_lengths[current_length])
        current_length -=selected_lengths[current_length]

    return dp[n],result_lengths

lengths=[1, 2, 3, 4]  # Available rod lengths
prices=[2, 3, 6, 9]  # Prices for respective lengths
rod_length=5

max_value,selected_lengths =rod_cutting(lengths,prices,rod_length)
print(f"Maximum Value: {max_value}")
print(f"Selected Lengths: {selected_lengths}")
