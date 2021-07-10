# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  10/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/list-comprehensions/problem
# Description:  Solution to "Python List Comprehension"
# Licence:      CC BY 4.0
# =====================================================================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([
        [ i, j,k] for i in range( x + 1)
            for j in range( y + 1)
                for k in range(z + 1)
        if ( ( i + j + k ) != n )
    ])