#Take an input string parameter and determine if exactly 3 question marks exist between every
# pair of numbers that add up to 10. If so, return true, otherwise return false.
# Some examples test cases are below: arrb6???4xxbl5???eee5" => true
# "acc?7??sss?3rr1??????5" => true
# "5??aaaaaaaaaaaaaaaaaaa?5?5" => false
# "9???1???9???1???9" => true
# "aa6?9" => false

def QuestionsMarks(s):
    a, b = 0, 0
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
               a, b = i, j
    new = s[a+1:b+1]
    if new.count('?') == 3:
        return 'true'
    else:
        return 'false'

print( QuestionsMarks(input('Please enter a string parameter')))
