import re
#Given aaaaabbcccccdd -> Convert it to 5a2b5c2d
a='aaaaabbcccccdd'
a1 = []

newstring1 = ''
newstring2 = ''
n=0
def count_of_char(a):
    a2 = ''
    for char in a:
        if char not in a2:

            print(char,',',a.count(char))
            a2=a2+char

print (count_of_char(a))


'''   print(a1)
    for item in a1:
        if a1[len(a1)-1] == a1[len(a1)-2]:
            n=+1
            newstring1 = str(n)+ a[len(a1)-1]
        else:
            n=+1
            newstring2 = str(n) + item
    newstring = newstring1+newstring2
    return newstring '''


s1 = 'pythonpypypypython'
s2 = 'py'
l1 =[]
l2 = []
def find_index (s1,s2):
    
    s3 =re.findall(s2,s1)
    return len(s3)

print(find_index(s1,s2))


