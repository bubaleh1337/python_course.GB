import text
import view
import model

my_pb = model.PhoneBook()
def start():
		while True:
				choice = view.main_menu() # вывод меню и предоставление выбора
				match choice:
						case 1: # Открыть файл
								my_pb.open_pb()
								view.print_message(text.load_successful)
						case 2: # Записать файл
								my_pb.save_pb()
								view.print_message(text.save_successful)
						case 3: # Показать контакт
								pb = my_pb.get_pb()
								view.print_contacts(pb, text.load_error)
						case 4: # Добавить контакт 
								contact = view.input_contact(text.input_new_contact, text.cancel_input)
								name = my_pb.add_contact(contact)
								view.print_message(text.new_contact_successful(name)) # type: ignore
						case 5: # Найти контакт
								word = view.input_search(text.input_search)
								result = my_pb.search_pb(word)
								view.print_contacts(result, text.empty_search(word))
						case 6: # Изменить контакт
								pb = my_pb.get_pb()
								index = view.input_index(text.input_index, pb, text.load_error)
								contact = view.input_contact(text.input_new_contact, text.cancel_input)
								result = my_pb.change_pb(contact, index)
								view.print_message(text.change_successful(contact))
						case 7: # Удалить контакт 
								pb = my_pb.get_pb()
								index = view.input_index(text.index_del_contact, pb, text.load_error)
								name = my_pb.del_contact(index)
								view.print_message(text.del_contact(name)) # type: ignore
						case 8:
								break