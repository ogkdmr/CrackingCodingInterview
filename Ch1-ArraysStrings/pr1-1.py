'''
Without using a data structure. 
Space complexity: O(1), Time complexity: O(n^2) where n is the length of the string.
'''
def is_unique_method1(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

print(is_unique_method1('merhaba'))
print(is_unique_method1('box'))


'''
Using set data structure. 
Space complexity O(n), Time Complexity O(1)
'''
def is_unique_method2(string):
    return len(set(string)) == len(string)

print(is_unique_method2('merhaba'))
print(is_unique_method2('box'))


'''
Using an array.
Space complexity O(n), Time Complexity O(n)
'''

def is_unique_method3(string):
    letters = []
    for letter in string:
        if letter in letters:
            return False
        letters.append(letter)
    return True

print(is_unique_method3('merhaba'))
print(is_unique_method3('box'))

'''
Using sorting. 
Space complexity O(n), Time Complexity: O(nlog(n) + n) 
'''
def is_unique_method4(string):
    sorted_letters = sorted(string)
    for i in range(len(sorted_letters)-1):
        if sorted_letters[i] == sorted_letters[i+1]:
            return False
    return True

print(is_unique_method4('merhaba'))
print(is_unique_method4('box'))
print(is_unique_method4(''))
