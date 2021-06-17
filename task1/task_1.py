import re
a = input()
nm = []
for i in range(len(a)) :
    if a[i].isdigit() == True:
        nm.append(int(a[i]))
a = re.sub("[0-9]", "", a)
print(a)
print(nm)
a = ' '.join(map(lambda s: s[:-1]+s[-1].upper(), a.title().split()))
print(a)
print("Max is ",max(nm))
new_nm = []
for i in range(len(nm)):
    if nm[i]!= max(nm):
        new_nm.append(pow(nm[i],i))
print(new_nm)

