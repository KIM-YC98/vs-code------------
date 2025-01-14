class Phone:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def __str__(self):
        return f'이름: {self.name}, 전화번호: {self.tel}'
    
class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_tel(self, name):
        
        tel = input(f'{name}의 전화번호를 입력하세요: ')
        self.phone_book.append(Phone(name, tel))

    def search_tel(self, name):
       
        for i in self.phone_book:
            if i.name == name:
                return i
        return None
    
    def all_tel(self):
        
        for i in self.phone_book:
            print(i)


phone_book = PhoneBook()


while True:
    name = input('이름을 입력하세요: (종료: exit) ')
    if name == 'exit':
        break
    phone_book.add_tel(name)


print('\n전화번호부:')
phone_book.all_tel()


search_name = input('\n검색할 이름을 입력하세요: ')
contact = phone_book.search_tel(search_name)

if contact:
    print(f'{search_name}의 전화번호는 {contact.tel}입니다.')
else:
    print(f'{search_name}의 전화번호를 찾을 수 없습니다.')