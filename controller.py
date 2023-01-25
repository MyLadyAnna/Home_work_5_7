import view
import model

def start():
    value = ''
    while value != '8':
        value = view.menu()

        match value:
            case '1':
                model.open_file()
            case '2':
                model.save_file()
                view.text_save()
            case '3':
                pb = model.get_phone_book()
                view.show_contacts(pb)
            case '4':
                new_contact = list(view.creat_new_contact())
                model.add_new_del_contact(new_contact)
            case '5':
                contact_for_delet = view.del_contact()
                contact = model.get_contact(contact_for_delet)
                if contact:
                    confirm = view.delete_conform(contact[0][0])
                    if confirm:
                        model.delet_contact(contact[0])
                        view.successfull_deleted()
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case '6':
                contact_for_change = view.change_contact()
                contact = model.get_contact(contact_for_change)
                if contact:
                    changet_cont = view.new_data_for_cont()
                    model.change_cont (contact[1], list(changet_cont))
                    view.successfull_change()
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case '7':
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case '8':
                view.exit()   
            case _:
                view.input_error()