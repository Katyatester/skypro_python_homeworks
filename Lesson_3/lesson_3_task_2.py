from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Samsung", "Galaxy A35", "+79279278877")
phone2 = Smartphone("Realme", "C21", "+79278887654")
phone3 = Smartphone("Xiaomi", "Redmi 9", "+79174659911")
phone4 = Smartphone("Apple", "iPhone 6s", "+79879828515")
phone5 = Smartphone("HONOR", "90 LITE", "+79879828516")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} . {phone.phone_number}")