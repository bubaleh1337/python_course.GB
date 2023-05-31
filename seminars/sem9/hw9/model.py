phone_book: list[dict[str, str]] = []
path = 'phones.txt'

def open_pb():
	global phone_book, path
	with open(path, 'r', encoding='UTF-8') as file:
		data = file.readlines() # 'Kate:7444654:comment'
	for contact in data:
		contact = contact.strip().split(':') # .strip() - очищение начало и конец строки
		phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})

def save_pb():
	global phone_book, path
	data = []
	for contact in phone_book:
		data.append(':'.join([value for value in contact.values()]))
	with open(path, 'w', encoding='UTF-8') as file:
		file.write('\n'.join(data))

def get_pb() -> list[dict[str, str]]:
	global phone_book
	return phone_book

def add_contact(contact: dict[str, str]):
	global phone_book
	phone_book.append(contact)
	return contact.get('name')

def del_contact(index: int): 
	global phone_book
	return phone_book.pop(index-1).get('name') 

"""def change_pb(pb, index):
	for contact in phone_book:
		if index == phone_book[index - 1]:
			contact['name'] = pb.get('name', contact.get('name'))
			contact['phone'] = pb.get('phone', contact.get('phone'))
			contact['comment'] = pb.get('comment', contact.get('comment'))
			return contact.get('name')"""

"""def search_pb(command: int, id: int, name: str, phone: str):
	result: list[dict[str, str]] = []
	match command:
		case 1:
			phone_book[id]
		case 2:
			for contact in phone_book:
				for field in contact.values():
					if name.lower() in field.lower():
						result.append(contact)
						break
		case 3:
			for contact in phone_book:
				for field in contact.values():
					if phone.lower() in field.lower():
						result.append(contact)
						break"""

def search_pb(word) -> list[dict[str, str]]:
	result: list[dict[str, str]] = []
	for contact in phone_book:
		for field in contact.values():
			if word.lower() in field.lower():
				result.append(contact)
				break
	return result

"""def change_pb3(index: int, name: str, phone: str):
	global phone_book
	
	if len(name) > 0:
		phone_book[index-1]['name'] = name
	if len(phone) > 0:
		phone_book[index-1]['phone'] = phone"""

def change_pb(contact, index: int):
	global phone_book
	
	# for key, value in contact.items():
	if len(contact['name']) > 0:
		phone_book[index-1]['name'] = contact['name']
	if len(contact['phone']) > 0:
		phone_book[index-1]['phone'] = contact['phone']
	if len(contact['comment']) > 0:
		phone_book[index-1]['comment'] = contact['comment']
					
	"""contact = contact.strip().split(':') # .strip() - очищение начало и конец строки
	phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]}) """ 

