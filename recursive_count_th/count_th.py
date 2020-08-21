'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    print(word)
    counter = 0

    if len(word) < 2:
        return counter
    

    if word[:2] == 'th':
        counter += 1

    if word[1:3] == 'th':
        counter += 1

    counter += count_th(word[3:])

    return counter
