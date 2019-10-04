#!/usr/bin/env python3
import numpy as np

def matrix_power(a, n):
    """
    so they gave an implementation and I ignored it cause I don't like it. 
    Now to do it their way.
    
    inspiration:
    https://stackoverflow.com/questions/28259967/how-do-i-apply-a-function-n-times
    recursion:
    https://stackoverflow.com/a/28260210
    Also has a nice section on composing as a string and evaluating it! :
    https://stackoverflow.com/a/28259986
    
    write three recursive functions. 
    n == 0 give identiy matrix
    n > 0 apply matrix multiply n-1 times
    n < 0 apply inverse n-1 times
    """
    # np.eye(2)
    def recursive_matrix_multiply(a, n):
        """only call with positive integer n args"""
        if n == 1:
            return a
        else:
            return a @ recursive_matrix_multiply(a, n-1)
    def recursive_matrix_inverse(a, n):
        """positive n"""
        if n == 1:
            return np.linalg.inv(a)
    
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return recursive_matrix_multiply(a, n)
    else:
        return recursive_matrix_inverse(a, -n)

def main():
    s = np.array([[1, 6, 7],[7, 8, 1],[5, 9, 8]])
    print(s)
    s_inv = matrix_power(s, -1)
    print(s_inv)
    print(s @ s_inv)
    mat = np.array([[1, 2],[3, 4]])
    mat_squared = matrix_power(mat, 2)
    print("\nmat:\n", mat)
    print("\nmat%*%mat:\n",mat_squared)

if __name__ == "__main__":
    main()
