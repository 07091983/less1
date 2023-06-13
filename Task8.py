# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и 
# удаления данных

def write_contacts(filename): 
    with open(filename, 'a', encoding='utf-8') as file: file.write('\n' + input(f'Введите имя фамилию и отчество и номер телефона: ')) 
    return file 
def read_contacts(filename): 
    contacts = [] 
    with open(filename, 'r') as file: 
        for line in file: 
            name, surname, patronymic, phone = line.strip().split(',') 
            contact = { 'name': name, 
                        'surname': surname, 
                        'patronymic': patronymic, 
                        'phone': phone } 
            contacts.append(contact) 
            return contacts

def edit_data(filename):
   print('\nПП | ФИО | Телефон')
with open(filename, 'r', encoding= 'utf-8') as file:
    contact = file.read()
print(contact)
print('')
index_delete_file = int (input('Введите номер строки для редактирования: '))-1
tel_book_lines = contact.split('\n')
edit_tel_book_lines = tel_book_lines[index_delete_file]
elements = edit_tel_book_lines.split(' | ')
fio = input('Введите ФИО: ')
phone = input('Введите номер телефона: ')
num = elements[0]
if len(fio) == 0:
    fio = elements[1]
if len(phone) == 0:
    phone = elements[2]
edited_line = f'{num} | {fio} | {phone}'
tel_book_lines[index_delete_file] = edited_line
print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
with open (filename, 'w', encoding = 'utf-8') as f:
    f.write('\n'.join(tel_book_lines))

filename = r'Sprav.txt'
a = int(input('1 - для ввода, 2 - для вывода \n')) 
if a == 1: add_contact = write_contacts(filename) 
elif a == 2: contact = read_contacts(filename) 
print(f'{contact}') 
print('Нет такой функции!')




