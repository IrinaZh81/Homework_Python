def is_yesr_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False
    
#задание три: В этом же файле напишите код,
#который вызывает функцию и передает в нее год (выберите любой).

year_to_ch = 2022
result = is_yesr_leap(year_to_ch)

print (f"год {year_to_ch}:{result}")