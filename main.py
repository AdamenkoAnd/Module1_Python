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
            print('❌ Сконтролируйте наличие 12 чисел в номере телефоне!.')
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
        file.write(f'{contact['name']}/{contact['phone']}/{contact['email']}\n')
  
        
def load_contacts():
    contacts = []
    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            name, phone, email = line.strip().split("/")
            contact = {"name": name, "phone": phone, "email": email}
            contacts.append(contact)
        return contacts  
    contacts = load_contacts()
    print(contacts)


def search_contact():
    search = input('Введите имя контакта или номер телефона: ')
    contacts = load_contacts()
    for contact in contacts:
        if search in contacts['name'].lower() or search in contacts['phone']:
            print(f'Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}')

def delete_contact():
    contacts = load_contacts()
    search = input('Введите имя контакта для удаления: ')
    for i, contact in enumerate(contacts):
        if search in contact['name'].lower() or search in contact['phone']:
            print(f'{contact['name']}/{contact['phone']}/{contact['email']}\n')
            confirm = input('Удалить контакт? - да/нет: ')
            if confirm.lower() == 'да':
                contact.pop(i)
                with open('contacts.txt', 'w', encoding='utf-8') as file:
                    for matches in contacts:
                        file.write(f'{matches["name"]}/{matches["phone"]}/{matches["email"]}\n')
                print("Контакт удален")


def update_contact():
    contacts = load_contacts()
    search = input('Введите имя или телефон контакта для обновления: ')
    for i, contact in enumerate(contacts):
        if search in contact['name'].lower() or search in contact['phone']:
            print(f'Текущие данные: Имя: {contact["name"]}, Телефон: {contact["phone"]}, Email: {contact["email"]}')
            name = check_name_contact()
            phone = check_phone_contact()
            email = check_email_contact()
            contacts[i] = {"name": name, "phone": phone, "email": email}
            with open('contacts.txt', 'w', encoding='utf-8') as file:
                for matches in contacts:
                    file.write(f'{matches["name"]}/{matches["phone"]}/{matches["email"]}\n')
            print("Контакт обновлен")
        

def show_all_contacts():
    contacts = load_contacts()
    for contact in contacts:
            print(f'Имя: {contact["name"]}, Телефон: {contact["phone"]}, Email: {contact["email"]}')

def main_contact():
    while True:
        print('1.Добавить контакт')
        print('2.Найти контакт')
        print('3.Удалить контакт')
        print('4. Обновить контакт')
        print('5. Просмотреть контакты')
        print('6. Выйти')
        
        choice = input("Выберите действие (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            show_all_contacts()
        elif choice == '6':
            print("До свидания!")
        else:
            print("Неверный выбор. Попробуйте снова.")



def add_contact():
    while True:
        name = check_name_contact()
        phone = check_phone_contact()
        email = check_email_contact()
        contacts = [name, str(phone), email]
        save_to_file(contacts)
        


main_contakt()
add_contact()
    
