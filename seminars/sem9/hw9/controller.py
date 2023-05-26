import text
import view
import model

def start():
		while True:
				choice = view.main_menu() # вывод меню и предоставление выбора
				match choice:
						case 1:
								model.open_pb()
								view.print_message(text.load_successful)
						case 2:
								model.save_pb()
								view.print_message(text.save_successful)
						case 3:
								pb = model.get_pb()
								view.print_contact(pb, text.load_error)
						case 4:
								contact = view.input_contact(text.new_contact, text.cancel_input)
								name = model.add_contact(contact)
								view.print_message(text.new_contact_successful(name)) # type: ignore
						case 5:
								pass
						case 6:
								pb = model.get_pb()
								index = view.input_index(text.index_change_contact, pb, text.load_error)
								contact = view.input_contact(text.new_contact, text.cancel_input)
								view.print_message(text.change_contact(contact))
						case 7:
								pb = model.get_pb()
								index = view.input_index(text.index_del_contact, pb, text.load_error)
								name = model.del_contact(index)
								view.print_message(text.del_contact(name)) # type: ignore
						case 8:
								break