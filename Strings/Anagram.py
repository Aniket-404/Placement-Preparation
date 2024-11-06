string1="silent"
string2="listen"

string1=sorted(string1.lower())
string2=sorted(string2.lower())

print(string1)
print(string2)

if string1==string2:
    print("Anagram")
else:
    print("Not an anagram")