cart = ["apples", "bananas", "cherries"]
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("bananas") # if you know value of what youre removinng use remove function, if you know index then use pop function
print(cart)
cart.pop(2)
print(cart)
cart.pop() #if u pop with nothing in parenthesis, its a stack so it will take off last item in list
print(cart)
cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort() # if i wanted to reverse order i would use cart.reverse
print(cart)

#slicing

fruit_basket = cart[2:4]
print(fruit_basket) 
count_bananas = cart.count("bananas")
print(count_bananas)
#if we want to know how many times an item is in a list we would use the .count feature (ex. cart.count(type what youre looking for))

squares = []
for i in range (1,5):
    squares.append(i*i)
print(squares)

#list comprehension
b_items=[item for item in cart if item.startswith("b")]
print(b_items)

inventory=[0] * 10 #creates a list filled with 10 zeroes
inventory[4] = 100
print(inventory)

#sets

book_genres = {"mystery","science fiction", "fantasy" } #diffrence between set and list is no duplicates and cant change value of any indexes
book_genres.add("romance")
print(book_genres) 

nums = [1,1,2,2,3,3,4,4,5,5]
unique=set(nums)
print(unique)


#Dictionaries

fav_snacks={"Ikenna":"chips" , "Mike": "Ice Cream" , "Mar": "Candy"}
i_snack = fav_snacks["Ikenna"]
print(i_snack)
fav_snacks["Mike"] = "None"

for key in fav_snacks:
    print(key, fav_snacks[key])

for person in fav_snacks:
    print(person, fav_snacks[person])

if "Jack" in fav_snacks:
    print(fav_snacks["Jack"])
else:
    fav_snacks["Jack"] = "Popcorn"