# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  09/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/python-tuples/problem
# Description:  Solution to "Python Tuples"
# Licence:      CC BY 4.0
# =====================================================================

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(hash(t))