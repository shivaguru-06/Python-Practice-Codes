from collections import Counter
def palindrome_permutation(s):
    s=s.replace(" ","").lower()
    count=Counter(s)
    odd_count=sum(1 for freq in count.values() if freq % 2 != 0)
    return odd_count<=1
a="TACO CAT"
b=palindrome_permutation(a)
print(b)

