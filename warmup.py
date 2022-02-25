# Siona Ravi
# CSCI 236
# Aug 29
# Program 00 - Warmup
# 2hrs

def checkIfCurzonNumber(N): 
  
    powerTerm, productTerm = 0, 0
  
    # Find 2^N + 1 
    powerTerm = pow(2, N) + 1
  
    # Find 2*N + 1 
    productTerm = 2 * N + 1
  
    # Check for divisibility 
    if (powerTerm % productTerm == 0): 
        print("Yes") 
    else: 
        print("No") 
  
# Driver code 
if __name__ == '__main__': 
      
    N = 5
    checkIfCurzonNumber(N) 
  
    N = 10
    checkIfCurzonNumber(N) 