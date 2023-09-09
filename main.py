# leep year
year=int(input("enter a year:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print( year,"is a leep year")
    else:
      print(year,"is a lepp year")
  else :
    print(year,"is a leep year")
else:
  print(year,"is not a leep year")
  