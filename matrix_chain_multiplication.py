def matrix_chain_order(p):
    n = len(p)-1  # Number of matrices
    # Create a table to store the minimum number of multiplications
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    # s[i][j] will store the index of the matrix after which the split occurs
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    # l is the chain length
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            m[i][j]=float('inf')
            
            for k in range(i,j):
                # Cost calculation for multiplying matrices A[i] to A[k] and A[k+1] to A[j]
                q=m[i][k]+m[k+1][j] +p[i]*p[k+1]*p[j+1]
                
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    
    return m,s

def print_optimal_parenthesization(s,i,j):
    if i==j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s,i,s[i][j])
        print_optimal_parenthesization(s,s[i][j]+1,j)
        print(")", end="")

# Example: Chain of matrices dimensions
p=[3, 2, 4, 2, 5]

# Function to calculate minimum multiplication cost
m,s=matrix_chain_order(p)

print("Minimum number of multiplications:", m[0][len(p)-2])
print("Optimal parenthesization:")
print_optimal_parenthesization(s,0,len(p)-2)
