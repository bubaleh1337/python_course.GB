from contextlib import suppress

class PhoneBook:

	def __init__(self, path: str = 'phones.txt'):
		self._phone_book: list[dict[str, str]] = []
		self._path = path

	def open_pb(self):
		with open(self._path, 'r', encoding='UTF-8') as file:
			data = file.readlines() # 'Kate:7444654:comment'
		for contact in data:
			contact = contact.strip().split(':') # .strip() - очищение начало и конец строки
			self._phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})

	def save_pb(self):
		data = []
		for contact in self._phone_book:
			data.append(':'.join([value for value in contact.values()]))
		with open(self._path, 'w', encoding='UTF-8') as file:
			file.write('\n'.join(data))

	def get_pb(self) -> list[dict[str, str]]:
		return self._phone_book

	def add_contact(self, contact: dict[str, str]):
		self._phone_book.append(contact)
		return contact.get('name')

	def del_contact(self, index: int): 
		return self._phone_book.pop(index-1).get('name') 

	def search_pb(self, word: str) -> list[dict[str, str]]:
		result: list[dict[str, str]] = []
		for contact in self._phone_book:
			for field in contact.values():
				if word.lower().strip() in field.lower().strip():
					result.append(contact)
					break
		return result

	def change_pb(self, contact: dict, index: int):

		with suppress(Exception):
			if len(contact['name']) > 0:
				self._phone_book[index-1]['name'] = contact['name']
		with suppress(Exception):
			if len(contact['phone']) > 0:
				self._phone_book[index-1]['phone'] = contact['phone']
		with suppress(Exception):
			if len(contact['comment']) > 0:
				self._phone_book[index-1]['comment'] = contact['comment']
