#is_permutation: Task: given two strings, compute whether they are permutations of each other.
#**Note: All these methods should first check if string lengths are equal, if not, just return False. Omitting for brevity but important in practice.


'''
Convert the characters into ASCII (or Unicode depending on the assumption) codes. See if their sum is equal.
Time Complexity O(n+m), Space Complexity O(n+m) where n is length of str1, m is length of str2
'''
def is_permutation_method1(str1, str2):
    return sum([ord(i) for i in str1]) == sum([ord(j) for j in str2])

print(is_permutation_method1('abcd', 'cadb'))
print(is_permutation_method1('ne', 'alaka'))
print(is_permutation_method1('',''))


'''
Uses a dictionary to lookup letter counts.
Time Complexity O(n+m), Space Complexity O(n)
'''
def is_permutation_method2(str1, str2):
    letter_counts = {i:str1.count(i) for i in str1}
    for j in str2:
        if j not in letter_counts or letter_counts[j] != str2.count(j):
            return False
    
    #alternatively, one could make a letter_count dict for str2 and check if two dicts are equal. This saves space and time through interruption.

    return True

print(is_permutation_method2('abcd', 'cadb'))
print(is_permutation_method2('ne', 'alaka'))
print(is_permutation_method2('',''))


'''
Sort the strings and check if they are equal - trivial.
Time Complexity O(nlogn + mlogm), Space Complexity O(n+m)
'''

def is_permutation_method3(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_permutation_method2('abcd', 'cadb'))
print(is_permutation_method2('ne', 'alaka'))
print(is_permutation_method2('',''))


