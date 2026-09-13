# Iterativea approach
def reverse_str_ite(s):
    rev_str = ""
    for char in s :
        rev_str = char + rev_str
    return rev_str
print(reverse_str_ite("hello"))


# Recursive apporach 
def reverse_str_rec(s):
    if len(s) <= 1:
        return s
    return reverse_str_rec(s[1:]) + s[0]
print(reverse_str_rec("hello"))

