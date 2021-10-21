s=["sora","casa","mama","andreea","tokyo","arenda","caciula","album"]
#a)
count=0
for i in s:
    for i in i:
        if i=="a":
            count=count+1
print(count)
#b)
for i in s:
    for i in i:
            print(s.replaced("a","*"))