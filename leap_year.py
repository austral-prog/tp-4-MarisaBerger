def leap_year():
   year = int(input("ingrese un año: "))
    if year % 100 == 0 and year % 400 == 0 :
        print(f"El año {year} es biciesto")
    elif year % 4 == 0 and not year % 100 == 0 :
        print(f"El año {year} es biciesto")
    else :
        print(f"El año {year} no es biciesto")    
leap_year()
