def month_to_season(month):
    if month in [1, 2, 12]:
        return ("Зима")
    if month in [3, 4, 5]:
        return ("Весна")
    if month in [6, 7, 8]:
        return ("Лето")
    if month in [9,10,11]:
        return ("Осень")
    else: 
        return "такого месяца не существует" 

print(month_to_season(6))    