# =====================================================================
# Author:       James Walker (GothicAnatomist)
# Create date:  08/07/2021
# Site:         HackerRank
# URL:          https://www.hackerrank.com/challenges/python-lists/problem
# Description:  Solution to "Python Lists"
# Licence:      CC BY 4.0
# =====================================================================

def ListCommands(input, curr_list=[]):
    temp = input.split()
    command = temp[0]

    if command == "insert":
        curr_list.insert(int(temp[1]), int(temp[2]))
    elif command == "remove":
        curr_list.remove(int(temp[1]))
    elif command == "append":
        curr_list.append(int(temp[1]))
    elif command == "sort":
        curr_list.sort()
    elif command == "pop":
        curr_list.pop()
    elif command == "reverse":
        curr_list.reverse()
    elif command == "print":
        print(curr_list)

    return curr_list


if __name__ == '__main__':
    N = int(input())
    lst = []
    for x in range(0, N):
        lst = ListCommands(input(), lst)
