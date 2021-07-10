# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  10/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Description:  Solution to "Python Find the Runner-Up Score!"
# Licence:      CC BY 4.0
# =====================================================================

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = sorted(list(set(arr)))
    print(lst[-2])