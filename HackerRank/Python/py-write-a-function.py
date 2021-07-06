# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  06/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/write-a-function/problem
# Description:  Solution to "Write a Function"
# Licence:      CC BY 4.0
# =====================================================================

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))