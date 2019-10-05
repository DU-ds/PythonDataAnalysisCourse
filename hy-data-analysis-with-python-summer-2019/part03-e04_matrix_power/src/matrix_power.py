#!/usr/bin/env python3
import numpy as np
import functools as funk
import itertools as it

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
    Nice way to make n copies:
    https://stackoverflow.com/questions/38607546/create-3d-array-from-a-2d-array-by-replicating-repeating-along-the-first-axis
    write three recursive functions. 
    n == 0 give identiy matrix
    n > 0 apply matrix multiply n-1 times
    n < 0 apply inverse n-1 times
    """
    if n > 0:
        A = np.repeat(a[np.newaxis,...], n, axis = 0)
        G = ( A[i,:,:] for i in range(n) )
        return funk.reduce(lambda x, y: x @ y , (a for a in G))
    elif n == 0:
        return np.eye(a.shape[0])
    else:
        a_inv = numpy.linalg.inv(a)
        n *= -1
        A = np.repeat(a_inv[np.newaxis,...], n, axis = 0)
        G = ( A_inv[i,:,:] for i in range(n) )
        return funk.reduce(lambda x, y: x @ y , (a for a in G))

# G = ( 100*a + 10*b + c for a in range(0,10)
#                        for b in range(0,10)

    # np.eye(2)
    # def recursive_matrix_multiply(a, n):
    #     """only call with positive integer n args"""
    #     if n == 1:
    #         return a
    #     else:
    #         return a @ recursive_matrix_multiply(a, n-1)
    # def recursive_matrix_inverse(a, n):
    #     """positive n"""
    #     if n == 1:
    #         return np.linalg.inv(a)
    #     else:
    #         return np.linalg.inv(a) @ recursive_matrix_inverse(a, n-1)
    # if n == 0:
    #     return np.eye(a.shape[0])
    # elif n > 0:
    #     return recursive_matrix_multiply(a, n)
    # else:
    #     return recursive_matrix_inverse(a, -n)

    
    # https://docs.python.org/3/library/functools.html
    # https://www.python.org/dev/peps/pep-0289/
    # https://pymotw.com/3/functools/

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



# G = ( 100*a + 10*b + c for a in range(0,10)
#                        for b in range(0,10)
#                        for c in range(0,10)
#                        if a <= b <= c )