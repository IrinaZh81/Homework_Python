from smartphone import Smartphone

catalog = [ 
    Smartphone("samsung", "galaxy s22", '89094445566'),
    Smartphone("samsung", "galaxy s32", '89094445556'),
    Smartphone("samsung", "galaxy s42", '89033434556'),
    Smartphone("samsung", "galaxy s52", '82222444566'),
    Smartphone("samsung", "galaxy s62", '99999444566')
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} . {phone.number_tel}")
    