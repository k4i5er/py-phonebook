from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, X, N, W, E, S, NW, StringVar, Toplevel
from tkinter.ttk import Frame, Button, Entry, Label, Style

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


def show_records():


def open_new_window():
    save_data()
    # print(addressbook)
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')
    newWindow.title('Consulta de registros - Agenda v.1.0')
    frm_name = Frame(newWindow)
    txt_showname = StringVar()
    txt_showname.set('Nombre: ')
    lbl_name = Label(frm_name, text=txt_showname.get())
    lbl_name.pack(side=LEFT, expand=1, fill=X)
    frm_name.pack(fill=X)

    frm_lastname = Frame(newWindow)
    txt_showlastname = StringVar()
    txt_showlastname.set('Apellidos: ')
    lbl_lastname = Label(frm_lastname, text=txt_showlastname.get())
    lbl_lastname.pack(side=LEFT, expand=1, fill=X)
    frm_lastname.pack(fill=X)

    frm_organization = Frame(newWindow)
    txt_showorganization = StringVar()
    txt_showorganization.set('Organización: ')
    lbl_organization = Label(frm_organization, text=txt_showorganization.get())
    lbl_organization.pack(side=LEFT, expand=1, fill=X)
    frm_organization.pack(fill=X)

    frm_phones = Frame(newWindow)
    Label(frm_phones, text='Teléfonos').pack(side=LEFT, expand=1, fill=X)
    frm_phones.pack(fill=X)

    frm_phonehome = Frame(newWindow)
    txt_showhomephone = StringVar()
    txt_showhomephone.set('Casa: ')
    lbl_homephone = Label(frm_homephone, text=txt_showhomephone.get())
    lbl_homephone.pack(side=LEFT, expand=1, fill=X)
    frm_phonehome.pack(fill=X)

    frm_cellphone = Frame(newWindow)
    txt_showcellphone = StringVar()
    txt_showcellphone.set('Celular: ')
    Label(frm_cellphone, text=txt_showcellphone.get()).pack(
        side=LEFT, expand=1, fill=X)
    frm_cellphone.pack(fill=X)

    frm_workphone = Frame(newWindow)
    txt_showworkphone = StringVar()
    txt_showworkphone.set('Laboral: ')
    Label(frm_workphone, text=txt_showworkphone.get()).pack(
        side=LEFT, expand=1, fill=X)
    frm_workphone.pack(fill=X)

    frm_emails = Frame(newWindow)
    Label(frm_emails, text='Correos electrónicos').pack(
        side=LEFT, expand=1, fill=X)
    frm_emails.pack(fill=X)

    frm_personal_email = Frame(newWindow)
    txt_show_personal_email = StringVar()
    txt_show_personal_email.set('Personal: ')
    Label(frm_personal_email, text=txt_show_personal_email.get()).pack(
        side=LEFT, expand=1, fill=X)
    frm_personal_email.pack(fill=X)

    frm_work_email = Frame(newWindow)
    txt_show_work_email = StringVar()
    txt_show_work_email.set('Laboral: ')
    Label(frm_work_email, text=txt_show_work_email.get()).pack(
        side=LEFT, expand=1, fill=X)
    frm_work_email.pack(fill=X)

    show_records()

    frm_navigation_buttons = Frame(newWindow)
    Button(frm_navigation_buttons, text='<',
           command=move_backward).pack(side=LEFT)
    Button(frm_navigation_buttons, text='>',
           command=move_forward).pack(side=LEFT)
    frm_navigation_buttons.pack()

    frm_back_button = Frame(newWindow)
    Button(frm_back_button, text='Regresar...',
           command=newWindow.destroy).pack()
    frm_back_button.pack(fill=X)


def move_backward():
    print('Pa\'tras!')


def move_forward():
    print('Pa\'delante')


root = Tk()
root.geometry('400x400')
root.title('Agenda v.1.0')

myStyle = Style()
myStyle.configure('lbl.TLabel', width=10)
myStyle.configure('TLabel', foreground='#0000ff')

frm_name = Frame(root)
Label(frm_name, text="Nombre", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_name = StringVar()
Entry(frm_name, textvariable=entry_name).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_name.pack(fill=X, ipady=10)

frm_lastname = Frame(root)
Label(frm_lastname, text="Apellidos",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_lastname = StringVar()
Entry(frm_lastname, textvariable=entry_lastname).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_lastname.pack(fill=X, ipady=10)

frm_organization = Frame(root)
Label(frm_organization, text="Organización",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_organization = StringVar()
Entry(frm_organization, textvariable=entry_organization).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_organization.pack(fill=X, ipady=10)

frm_phones = Frame(root)
Label(frm_phones, text="Teléfonos").pack(side=LEFT, padx=10)
frm_phones.pack(fill=X, ipady=10)

frm_homephone = Frame(root)
Label(frm_homephone, text="Casa", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_homephone = StringVar()
Entry(frm_homephone, textvariable=entry_homephone).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_homephone.pack(fill=X, ipady=10)

frm_cellphone = Frame(root)
Label(frm_cellphone, text="Celular", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_cellphone = StringVar()
Entry(frm_cellphone, textvariable=entry_cellphone).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_cellphone.pack(fill=X, ipady=10)

frm_workphone = Frame(root)
Label(frm_workphone, text="Laboral", style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_workphone = StringVar()
Entry(frm_workphone, textvariable=entry_workphone).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_workphone.pack(fill=X, ipady=10)

frm_emails = Frame(root)
Label(frm_emails, text="Correos electrónicos").pack(side=LEFT, padx=10)
frm_emails.pack(fill=X, ipady=10)

frm_personal_email = Frame(root)
Label(frm_personal_email, text="Personal",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_personal_email = StringVar()
Entry(frm_personal_email, textvariable=entry_personal_email).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_personal_email.pack(fill=X, ipady=10)

frm_work_email = Frame(root)
Label(frm_work_email, text="Laboral",
      style='lbl.TLabel').pack(side=LEFT, padx=10)
entry_work_email = StringVar()
Entry(frm_work_email, textvariable=entry_work_email).pack(
    side=LEFT, expand=1, fill=X, padx=10)
frm_work_email.pack(fill=X, ipady=10)

Button(root, text='Registrar datos', command=open_new_window).pack()

root.mainloop()
