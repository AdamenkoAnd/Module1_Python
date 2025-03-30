def main_contact():
    print('Основная функция')

main_contact();
name = input('Введите имя контакта: ')
phon = input('Введите номер телефона 12 чисел: ')
mail = input('Введите email: ' )

file = open('contacts.txt', 'a')
file.write(name)
file.write(' / ')
if len(phon) == 12:
    file.write(phon)
    file.write(' / ')
if mail.count('@') == 1:
    file.write(mail)
    file.write(' / ')
    file.write('\n')
    file.close
    print('✅ Контакт успешно добавлен!')
else:
    print('❌ Неверный выбор. Попробуйте снова.')

    
