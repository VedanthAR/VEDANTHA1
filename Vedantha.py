
a=int(input('enter the value of A'))
b=int(input('enter the value of B'))
c=a+b
print(c)
print("naveen")
d=int(input('enter the value of D'))
e=int(input('enter the value of E'))
f=d*e
print(f)
s="hello world"
sub="world"
print(sub in s)
s="hi"
s=s.lower()
vowels="aeiou"
v1=s[0] in vowels
v2=s[1] in vowels
vowels_count=2-vowels_count
print("vowels:",vowels_count)
print("consonants:",consonants_count)
s1="listen"
s2="silent"
s1=".join(sorted(s1.replace("","").lower()))
s2=".join(sorted(s2.replace("","").lower()))
print(s1==s2)
s="aabbcc"
result=s[0]
if s[1]!=result:
    result+=s[1]
    if s[2] not in result:
        result+=s[2]
        if s[3] not in result:
            result+=s[3]
            if s[4] not in result:
                result+=s[4]
                if s[5] not in result:
                    result+=s[5]
                    print(result)
                    s="madam"
                    print(s==s[::-1])
                    s="babad"
                    print("bab")
                    a1=["eat,"tea","ate"]
                    a2=["tan","Nat"]
                    a3=["bat"]
                    print([a1,a2,a3])
                    s="abcabcbb"
                    print(3)
                    print(hi)
                    print(hello)
                    print(github)
