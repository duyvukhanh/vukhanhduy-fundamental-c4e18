prices ={}
stock = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3
stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

for k,i in prices.items():
    print(k)
    print('price :',prices[k])
    print('stock :',stock[k])

total = 0
for k in prices:
    total = total + prices[k]*stock[k]

print()
print("You can earn total",total,"$")
print()