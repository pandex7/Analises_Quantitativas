x = 10
x
x = 5+5
x
a,b,c,d = [10, 20, 30, 40]
b
d
x1 = 5
type (x1)
x2 = 4.75
type (x2)
int(x2)
float(x1)
x3 = True
type(x3)
y = 10
str(y) + " Dollars"
"Friday"[3]

if 5 == 15 / 3:
    print ("hooray!")

def plus_ten(a):
    return a + 10
plus_ten(2)
plus_ten(5)

def plus_five(x):
    return x + 5
def p_dex_3(x):
    return plus_five(x) * 3
p_dex_3(5)

Menu = {"meal_1":"Spaghetti", "meal_2":"Fries", "meal_3": "Hamburger", "meal_4":"Lasagna"}
Menu["meal_2"]
print (Menu["meal_2"])
Menu["meal_5"] = "Sopa"
Menu
Menu["meal_3"] = "cheesburger"
Menu
Dessert = ["Panquecas", "Sovertes", "Bolo"]
Menu["meal_6"] = "Dessert"
Menu
Price_list = {}
Price_list["Spaghetti"] = 10
Price_list["Fries"] = 5
Price_list["Chessburger"] = 8
Price_list["Lasagna"] = 12
Price_list["Sopa"] = 5

Price_list = {}
Price_list[Menu["meal_1"]] = 10
Price_list[Menu["meal_2"]] = 5
Price_list[Menu["meal_3"]] = 8
Price_list[Menu["meal_4"]] = 12
Price_list[Menu["meal_5"]] = 5
Price_list
Price_list.get("Lasagna")
Price_list.get(Menu["meal_4"])
Price_list.get("Fries") + Price_list.get(Menu["meal_3"])

even = [0,2,4,6,8,10,12,14,16,18,20]
for n in even:
    print (n)

x = 0
while x <= 20:
    print (x,)
    x = x + 2
    

for x in range(0,51,1):
    print(x)

for n in range(10):
    print(2**n,)

for x in range(20):
    if x % 2 ==0:
        print(x)
    else:
        print("ODD")
    
x = [1,2,3,4,5]
for item in x:
    print(item)

for item in range(len(x)):
    print(x[item])

for n in range(1,11):
    print(n)

for y in range(20):
    print(y)
for p in range(0,31,2):
    print(p)
def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total
list_1 = [1,3,4,20,25,40,80,14,13]
count(list_1)

prices = {
    "box_of_spaghetti" : 4,
    "lasagna" : 5,
    "hamburger" : 2,
}
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna" : 10,
    "hamburger" : 0,
}
money_spent = 0
for n in quantity:
    if prices[n]>=5:
        money_spent += prices[n]*quantity[n]
        else:
            money_spent = money_spent
print(money_spent)

money_spent = 0
for n in quantity:
    if prices[n]<5:
        money_spent += prices[n]*quantity[n]
    else:
        money_spent = money_spent
print(money_spent)
