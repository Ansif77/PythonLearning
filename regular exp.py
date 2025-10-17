import re


#search
# text="hello world"
# print(re.search(r"hello",text))

# match only take starting word
# text="hello world"
# print(re.match(r"world",text))

# find all 
# text="i have 4 apple and 5 orange"
# print(re.findall(r'\d+',text))

#finditer
# a="i have 4 apple and 5 orange and 8 cherry"
# for match in re.finditer(r'\d',a):
#     print(match.group(),"at",match.start())

#sub 
# b="hello 123 world 456"
# print(re.sub(r"\D+","number",b))

#split
# a="apple,orange:banana,grape"
# print(re.split(r"[:,]",a))

# grouping and capturing
# data="john: 25,alice: 28,bob: 89"
# print(re.findall(r"(\w+): (\d+)",data))

#compile
# pattern=re.compile(r"\d+")
# text="ihave 3 apple and 4 mango"
# print(pattern.findall(text))
# text1="hello world"
# print(pattern.match(text1))

#nocase
# txt="hello world"
# print(re.findall(r"Hello",txt,re.IGNORECASE))

#multi line
# text="""first line
# second line
# third line"""
# print(re.findall(r"^s\w+",text,re.MULTILINE))
# #print based last letter
# print(re.findall(r"\w+e$",text,re.MULTILINE))


#dotall
text="hello/nworld"
print(re.search(r"hello.*world",text))
print(re.search(r"hello.*world",text,re.DOTALL))