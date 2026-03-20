# Question (1) You have a list of messy user inputs. Some are strings, some are None,
# and some are empty strings.Use filter and map to return a list of clean, lowercase names.
print("-----------------Map+Filter------------------")
user_input=["BOB","  ","alice"," charlie  ", "",None]

#here strip() will convert " " (True) to "" (False)

filtered=filter(lambda x:x is not None and x.strip(),user_input)

cleaned_user_input=list(map(lambda x:x.lower().strip(),filtered))
print(cleaned_user_input)

# Question(2) You have a list of product names, a list of their prices, and a list of the quantities purchased.
# Calculate the total cost of the entire shopping cart in one line (excluding the functools import).

import functools
print("-----------------Zip+Map+Reduce---------------------")

products = ["Apple", "Orange", "Banana"]

prices = [1.2, 0.8, 0.5]

counts = [5, 10, 2]

cost=functools.reduce(lambda x,y:x+y,map(lambda x:x[0]*x[1],zip(prices,counts)))
print(cost)