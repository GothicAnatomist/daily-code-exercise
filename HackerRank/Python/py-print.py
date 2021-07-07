# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  07/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/python-print/problem
# Description:  Solution to "Python Print"
# Licence:      CC BY 4.0
# =====================================================================

if __name__ == '__main__':
    n = int(input())
    output = ""
    for x in range(1, n + 1):
        output += str(x)
    print(output)