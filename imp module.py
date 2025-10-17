#import complete module file
# import mymodule

# a=mymodule.greet("JOHN")
# print(a)

#import specefic function or any esc
# from mymodule import greet2

# b=greet2("ALICE")
# print(b)

#give a nick name or else to imported module
#aliace 

# import mymodule as mod

# c=mod.greet3("ANSHIF")
# print(c)

# import math

# a=math.factorial(5)
# b=math.sqrt(25)
# print(a,b)

#datetime
# from datetime import datetime

# a=datetime.now()
# print(a)

#########  import sys
# import sys

# print(sys.version)

# import json
# d='{"name":"anshif","age":"18"}'
# j_data=json.loads(d)
# print(j_data)




#numpy
# import numpy as np

# array=np.array([1,2,5,8,4,9])
# print(array)

# sq_array=array**2
# print(sq_array)

# arr_sum=np.sum(array)
# print(arr_sum)

#pandas
# import pandas as pd 
# data={'name':['alice','bob','john'],'age':['20','30','48']}
# df=pd.DataFrame(data)
# print(df)

#matplotlib
# import matplotlib.pyplot as plt 
# x = [1, 2, 3, 4] 
# y = [10, 20, 25, 40] 
# plt.plot(x, y) 
# plt.show() 

#request
# import requests 
# response = requests.get('https://api.github.com') 
# print(response.status_code)


# from bs4 import BeautifulSoup 
# import requests 
# page = requests.get("https://whatsapp.com") 
# soup = BeautifulSoup(page.content, 'html.parser') 
# print(soup.title.text) 