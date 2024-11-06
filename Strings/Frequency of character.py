string="Aniket Kamble"

for i in string:
    frequency1=string.count(i)
    print(str(i),":",str(frequency1),end=", ")

for j in string:
    frequency2=string.count(j)
    if frequency2==1:
        print(str(j),end=", ")