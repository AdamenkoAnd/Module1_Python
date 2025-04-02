def main_contakt():
    print('Основная функция')

def check_name_contact():
    while True:
        name = input('Введите имя контакта: ')
        if len(name) != 0:
            return name
        print('Введено неправильное имя контакта.')

def check_phone_contact():
    while True:
        try:
            phon = int(input('Введите номер телефона (12 чисел): '))
            if len(str(phon)) == 12:
                return phon
                print('❌ Сконтролируйте наличее 12 чисел в номере телефоне!.')
        except ValueError:
            print('Ошибка!! Введены не числа!!!')

def check_email_contact():
    while True:
        email = input('Введите email: ')
        if email.count('@') and ('.') in email:
            return email
        print('❌ Проверте правильность написания emale!.')

def save_to_file(contact):
    with open('contacts.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contact[0]}/{contact[1]}/{contact[2]}\n')

def add_contact():
    while True:
        name = check_name_contact()
        phone = check_phone_contact()
        email = check_email_contact()

main_contakt()
add_contact()
    
