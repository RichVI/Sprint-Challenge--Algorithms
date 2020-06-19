'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Loop through the word array and return 0 if the words are less than two characters
    if (len(word) < 2):
        return 0

    count = 0 
    if word[:2] == 'th':
        count += 1

    # Use recurion for every two letters everytime it's called
    count += count_th(word[1:])

    return count

    # #abcthxyz
    # word  count
    # ab    0
    # bc    0
    # ct    0
    # th    1
    # hx    0
    # xy    0
    # yz    0
