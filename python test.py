
# a='LISTEN'
# b='SILENT'
# if sorted(a)==sorted(b):
#     print(' Strings are Anagrams')
# elif a!=b:
#     print(' Strings are Not Anagrams')



def d_to_b(num):
    answer=''
    while num>0:
        a=num%2
        answer=str(a)+answer
        num//=2
        
    return answer

print(d_to_b(7))
