import random
import csv
import logger as lg

file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,email\n"
file.writelines(newrecord)

ls_name = ['Anna', 'Irina', 'Anton', 'Inna', 'Sasha', 'Ivan', 'Kirill', 'Ben', 'Kris', 'Djo']
ls_surname = ['Kovalchuk', 'Putin', 'Novach','Baiden','Klark','Star', 'Kozak', 'Pretser', 'Galich']
ls_e_mail = ['@gmail.com','@mail.ru', '@yahoo.com']

def list_of_numbers():
    randomListPhone = random.randint(79000000000, 80000000000)
    return str(randomListPhone)

def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers() + ',' + random.choice(ls_surname) + random.choice(ls_e_mail)
    return s

def start():
    for i in range(100):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()