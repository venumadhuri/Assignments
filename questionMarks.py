#/user/bin/python3
import re

def findQuestionMarks(s):
    matches = []
    matchFound = False
    # the below pattern checks for 3 questions marks between two numbers
    pattern = re.compile(r'\d[A-Za-z]*?\?[A-Za-z]*?\?[A-Za-z]*?\?[A-Za-z]*?\d')

    # find all the matches in the strings
    matches = pattern.findall(s)

    # iterate through all the patterns found for examples (6?er?jie?y4)
    # add the numbers and find the total equals 10
    for match in matches:
        print(match)
        if (int(match[0]) + int(match[-1]) == 10):
            print('match found')
            matchFound = True

    return matchFound


def main():
    myString = '5cce??3&&&67ru8???2*dfjdf6?er?jie?y4fdfdf'
    findQuestionMarks(myString)

    return

if __name__ == "__main__":
    main()