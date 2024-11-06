char="Aniket"
char = char.lower()
count = 0
for i in char:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
    
if count==0:
    print("no vowels")
else:
    print(count)