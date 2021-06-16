from random import randint
lt1 = []
index = 0
for i in range(30):
    lt1.append(randint(-100,100))
print(lt1)
for i in range(30):
    if lt1[i] == max(lt1):
        index = i
print("Max element is ",max(lt1),"with index -",index)
for i in range(29):
    if (lt1[i]<0 and lt1[i+1]<0):
        print("Find",lt1[i],lt1[i+1])
