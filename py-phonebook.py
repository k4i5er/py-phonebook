from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, X, N, W, E, S, NW, StringVar, Toplevel, END
from tkinter.ttk import Frame, Button, Entry, Label, Style

# CRUD = Create, Read, Update, Delete

# addressbook = [
#   {
#     'name': 'César',
#     'lastname': 'López',
#     'organization': 'UAGro',
#     'phones':{
#         'home': '7444444444',
#         'cell': '7111111111',
#         'work': '7222222222'
#       },
#     'emails': {
#       'personal': 'cesar.lpz@gmail.com',
#       'work': '13565@uagro.mx'
#     }
#   },
# ]
addressbook = []
i = 0


def save_data():
    addressbook.append(
        {
            'name': entry_name.get(),
            'lastname': entry_lastname.get(),
            'organization': entry_organization.get(),
            'phones': {
                'home': entry_homephone.get(),
                'cell': entry_cellphone.get(),
                'work': entry_workphone.get()
            },
            'emails': {
                'personal': entry_personal_email.get(),
                'work': entry_work_email.get()
            }
        },
    )


def save_record():
    addressbook[i] = {
        'name': e_name.get(),
        'lastname': e_lastname.get(),
        'organization': e_organization.get(),
        'phones': {
            'home': e_homephone.get(),
            'cell': e_cellphone.get(),
            'work': e_workphone.get()
        },
        'emails': {
            'personal': e_personal_email.get(),
            'work': e_work_email.get()
        }
    }
    disable_entrys()
    btn_modify.configure(text='Modificar registro', command=modify_record)


def delete_entry_main_window():
    entry_name.delete(0, END)
    entry_lastname.delete(0, END)
    entry_organization.delete(0, END)
    entry_homephone.delete(0, END)
    entry_cellphone.delete(0, END)
    entry_workphone.delete(0, END)
    entry_personal_email.delete(0, END)
    entry_work_email.delete(0, END)


def delete_entry_second_window():
    e_name.delete(0, END)
    e_lastname.delete(0, END)
    e_organization.delete(0, END)
    e_cellphone.delete(0, END)
    e_homephone.delete(0, END)
    e_workphone.delete(0, END)
    e_personal_email.delete(0, END)
    e_work_email.delete(0, END)


def enable_entrys():
    e_name.state(['!readonly'])
    e_lastname.state(['!readonly'])
    e_organization.state(['!readonly'])
    e_cellphone.state(['!readonly'])
    e_homephone.state(['!readonly'])
    e_workphone.state(['!readonly'])
    e_personal_email.state(['!readonly'])
    e_work_email.state(['!readonly'])


def disable_entrys():
    e_name.state(['readonly'])
    e_lastname.state(['readonly'])
    e_organization.state(['readonly'])
    e_cellphone.state(['readonly'])
    e_homephone.state(['readonly'])
    e_workphone.state(['readonly'])
    e_personal_email.state(['readonly'])
    e_work_email.state(['readonly'])


def show_records():
    enable_entrys()
    delete_entry_second_window()
    e_name.insert(0, addressbook[i]["name"])
    e_lastname.insert(0, addressbook[i]["lastname"])
    e_organization.insert(0, addressbook[i]["organization"])
    e_homephone.insert(0, addressbook[i]["phones"]["home"])
    e_cellphone.insert(0, addressbook[i]["phones"]["cell"])
    e_workphone.insert(0, addressbook[i]["phones"]["work"])
    e_personal_email.insert(0, addressbook[i]["emails"]["personal"])
    e_work_email.insert(0, addressbook[i]["emails"]["work"])
    disable_entrys()


def modify_record():
    enable_entrys()
    btn_modify.configure(text='Guardar registro', command=save_record)


def delete_record():
    global i
    addressbook.pop(i)
    # addressbook[0]
    # addressbook[1] <-- me posiciono aquí para eliminar
    # i -> 1
    # Doy click a Eliminar
    # addressbook[0]
    # i -> 0
    if i > len(addressbook) - 1:
        i = len(addressbook) - 1

    if len(addressbook) > 0:
        show_records()
    else:
        newWindow.destroy()

    if i == len(addressbook) - 1:
        btn_forward.pack_forget()
    if len(addressbook) == 1:
        btn_back.pack_forget()


def validate_entrys():
    validate = True

    if len(entry_name.get()) == 0:
        lbl_name.configure(style='error.TLabel')
        validate = False
    else:
        lbl_name.configure(style='lbl.TLabel')

    if len(entry_lastname.get()) == 0:
        lbl_lastname.configure(style='error.TLabel')
        validate = False
    else:
        lbl_lastname.configure(style='lbl.TLabel')

    if len(entry_cellphone.get()) == 0:
        lbl_cellphone.configure(style='error.TLabel')
        validate = False
    else:
        lbl_cellphone.configure(style='lbl.TLabel')

    if len(entry_personal_email.get()) == 0:
        lbl_personal_email.configure(style='error.TLabel')
        validate = False
    else:
        lbl_personal_email.configure(style='lbl.TLabel')

    return validate


def open_new_window():
    is_valid = validate_entrys()
    if is_valid:
        global e_name
        global e_lastname
        global e_organization
        global e_homephone
        global e_workphone
        global e_cellphone
        global e_personal_email
        global e_work_email
        global newWindow
        global btn_back
        global btn_forward
        global btn_modify
        global i

        i = 0
        save_data()
        delete_entry_main_window()
        newWindow = Toplevel(root)
        newWindow.geometry('400x400')
        newWindow.title('Consulta de registros - Agenda v.1.0')
        frm_name = Frame(newWindow)
        Label(frm_name, text="Nombre").pack(side=LEFT)
        e_name = Entry(frm_name)
        e_name.pack(side=LEFT, fill=X, expand=1)
        frm_name.pack(fill=X)

        frm_lastname = Frame(newWindow)
        lbl_lastname = Label(frm_lastname, text="Apellidos")
        lbl_lastname.pack(side=LEFT, expand=1, fill=X)
        e_lastname = Entry(frm_lastname)
        e_lastname.pack(side=LEFT, fill=X, expand=1)
        frm_lastname.pack(fill=X)

        frm_organization = Frame(newWindow)
        txt_showorganization = StringVar()
        txt_showorganization.set('Organización: ')
        lbl_organization = Label(
            frm_organization, text=txt_showorganization.get())
        lbl_organization.pack(side=LEFT)
        e_organization = Entry(frm_organization)
        e_organization.pack(side=LEFT, fill=X, expand=1)
        frm_organization.pack(fill=X)

        frm_phones = Frame(newWindow)
        Label(frm_phones, text='Teléfonos').pack(side=LEFT, expand=1, fill=X)
        frm_phones.pack(fill=X)

        frm_homephone = Frame(newWindow)
        txt_showhomephone = StringVar()
        txt_showhomephone.set('Casa: ')
        lbl_homephone = Label(frm_homephone, text=txt_showhomephone.get())
        lbl_homephone.pack(side=LEFT)
        e_homephone = Entry(frm_homephone)
        e_homephone.pack(side=LEFT, fill=X, expand=1)
        frm_homephone.pack(fill=X)

        frm_cellphone = Frame(newWindow)
        txt_showcellphone = StringVar()
        txt_showcellphone.set('Celular: ')
        lbl_cellphone = Label(frm_cellphone, text=txt_showcellphone.get())
        lbl_cellphone.pack(side=LEFT)
        e_cellphone = Entry(frm_cellphone)
        e_cellphone.pack(side=LEFT, fill=X, expand=1)
        frm_cellphone.pack(fill=X)

        frm_workphone = Frame(newWindow)
        txt_showworkphone = StringVar()
        txt_showworkphone.set('Laboral: ')
        lbl_workphone = Label(frm_workphone, text=txt_showworkphone.get())
        lbl_workphone.pack(side=LEFT)
        e_workphone = Entry(frm_workphone)
        e_workphone.pack(side=LEFT, fill=X, expand=1)
        frm_workphone.pack(fill=X)

        frm_emails = Frame(newWindow)
        Label(frm_emails, text='Correos electrónicos').pack(
            side=LEFT, expand=1, fill=X)
        frm_emails.pack(fill=X)

        frm_personal_email = Frame(newWindow)
        txt_show_personal_email = StringVar()
        txt_show_personal_email.set('Personal: ')
        lbl_personal_email = Label(
            frm_personal_email, text=txt_show_personal_email.get())
        lbl_personal_email.pack(side=LEFT)
        e_personal_email = Entry(frm_personal_email)
        e_personal_email.pack(side=LEFT, fill=X, expand=1)
        frm_personal_email.pack(fill=X)

        frm_work_email = Frame(newWindow)
        txt_show_work_email = StringVar()
        txt_show_work_email.set('Laboral: ')
        lbl_work_email = Label(frm_work_email, text=txt_show_work_email.get())
        lbl_work_email.pack(side=LEFT)
        e_work_email = Entry(frm_work_email)
        e_work_email.pack(side=LEFT, fill=X, expand=1)
        frm_work_email.pack(fill=X)

        show_records()

        frm_navigation_buttons = Frame(newWindow)
        btn_back = Button(frm_navigation_buttons,
                          text='<', command=move_backward)
        if i != 0:
            btn_back.pack(side=LEFT)
        else:
            btn_back.pack_forget()

        btn_forward = Button(frm_navigation_buttons,
                             text='>', command=move_forward)
        if i < len(addressbook)-1:
            btn_forward.pack(side=LEFT)
        else:
            btn_forward.pack_forget()

        frm_navigation_buttons.pack()

        frm_back_button = Frame(newWindow)
        btn_modify = Button(
            frm_back_button, text='Modificar registro', command=modify_record)
        btn_modify.pack(side=LEFT, expand=1)
        btn_delete = Button(frm_back_button, text='Eliminar',
                            command=delete_record)
        btn_delete.pack(side=LEFT, expand=1)
        Button(frm_back_button, text='Regresar...',
               command=newWindow.destroy).pack(side=LEFT, expand=1)
        frm_back_button.pack(fill=X)


def move_backward():
    global i
    global btn_back
    global btn_forward
    if i != 0:
        i -= 1
        show_records()
        btn_forward.pack()
        if i == 0:
            btn_back.pack_forget()


def move_forward():
    global i
    global btn_back
    global btn_forward
    if i < len(addressbook)-1:
        i += 1
        show_records()
        btn_back.pack(before=btn_forward, side=LEFT)
        if i == len(addressbook) - 1:
            btn_forward.pack_forget()


root = Tk()
root.geometry('400x400')
root.title('Agenda v.1.0')

myStyle = Style()
myStyle.configure('lbl.TLabel', width=10, foreground='#0000ff')
myStyle.configure('error.TLabel', width=10, foreground='red')
myStyle.configure('TLabel', foreground='#0000ff')

frm_name = Frame(root)
lbl_name = Label(frm_name, text="Nombre", style='lbl.TLabel')
lbl_name.pack(side=LEFT, padx=10)
entry_name = Entry(frm_name)
entry_name.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_name.pack(fill=X, ipady=10)

frm_lastname = Frame(root)
lbl_lastname = Label(frm_lastname, text="Apellidos", style='lbl.TLabel')
lbl_lastname.pack(side=LEFT, padx=10)
entry_lastname = Entry(frm_lastname)
entry_lastname.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_lastname.pack(fill=X, ipady=10)

frm_organization = Frame(root)
Label(frm_organization, text="Organización",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_organization = Entry(frm_organization)
entry_organization.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_organization.pack(fill=X, ipady=10)

frm_phones = Frame(root)
Label(frm_phones, text="Teléfonos").pack(side=LEFT, padx=10)
frm_phones.pack(fill=X, ipady=10)

frm_homephone = Frame(root)
Label(frm_homephone, text="Casa", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_homephone = Entry(frm_homephone)
entry_homephone.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_homephone.pack(fill=X, ipady=10)

frm_cellphone = Frame(root)
lbl_cellphone = Label(frm_cellphone, text="Celular", style='lbl.TLabel')
lbl_cellphone.pack(side=LEFT, padx=10)
entry_cellphone = Entry(frm_cellphone)
entry_cellphone.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_cellphone.pack(fill=X, ipady=10)

frm_workphone = Frame(root)
Label(frm_workphone, text="Laboral", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_workphone = Entry(frm_workphone)
entry_workphone.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_workphone.pack(fill=X, ipady=10)

frm_emails = Frame(root)
Label(frm_emails, text="Correos electrónicos").pack(side=LEFT, padx=10)
frm_emails.pack(fill=X, ipady=10)

frm_personal_email = Frame(root)
lbl_personal_email = Label(
    frm_personal_email, text="Personal", style='lbl.TLabel')
lbl_personal_email.pack(side=LEFT, padx=10)
entry_personal_email = Entry(frm_personal_email)
entry_personal_email.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_personal_email.pack(fill=X, ipady=10)

frm_work_email = Frame(root)
Label(frm_work_email, text="Laboral",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_work_email = Entry(frm_work_email)
entry_work_email.pack(side=LEFT, expand=1, fill=X, padx=10)
frm_work_email.pack(fill=X, ipady=10)

Button(root, text='Registrar datos',
       command=open_new_window).pack(side=LEFT, expand=1)
Button(root, text='Salir', command=root.destroy).pack(side=LEFT, expand=1)

root.mainloop()
