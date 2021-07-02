# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  02/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/py-if-else/problem
# Description:  Solution to "Python If-Else"
# Licence:      CC BY 4.0
# =====================================================================

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0 and (n in range(2, 5) or n > 20):
        print("Not Weird")
    else:
        print("Weird")