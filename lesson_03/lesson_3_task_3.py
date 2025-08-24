from Address import Address
from Mailing import Mailing

to_address = Address("123456", "Краснодар", "Мира", "15", "24")
from_address = Address("654321", "Санкт-Петербург", "Невский", "42", "7")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=250,
    track="TR123456789RU"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")