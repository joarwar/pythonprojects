fuel_price = {
     'today' : 21.45,
     'yesterday' : 22,
     'two_days_ago' : 21.7
 }
accumulator = 0
for x, y in fuel_price.items():
   print(x, y)
   accumulator += y
   print(accumulator/3)
   print("CLASS UNDER")

class fuel_prices:
  today = 21.45
  yesterday = 22
  two_days_ago = 21.7


f1 = fuel_prices()
print((f1.today + f1.yesterday + f1.two_days_ago) / 3)

