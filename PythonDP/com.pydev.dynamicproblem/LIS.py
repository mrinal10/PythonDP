# global variable to store the maximum 
global maximum 


def _lis(arr , n): 

    # to allow the access of global variable 
    global maximum 

    # Base Case 
    if n == 1 : 
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1

    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere: 
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum , maxEndingHere) 

    return maxEndingHere 


def lis(arr): 

    # to allow the access of global variable 
    global maximum 

    n = len(arr) 
    maximum = 1

    _lis(arr , n) 

    return maximum 


arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
n = len(arr) 
print ("Length of lis is ", lis(arr)) 

