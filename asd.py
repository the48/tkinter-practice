# Nessasary lines
from tkinter import *

class LoginFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.data = StringVar(self, 'Please enter your details')
        self.data_label = Label(self, text = self.data.get())
        self.data_label.grid(row = 7, column = 1)

        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.label_name = Label(self, text = "Name")
        self.label_phone_number = Label(self, text = "Phone Number")
        self.label_address = Label(self, text = "Address")

        self.label_name.grid(row = 0, column = 0)
        self.label_phone_number.grid(row = 1, column = 0)
        self.label_address.grid(row = 2, column = 0)

        self.name = StringVar()
        self.name_box = Entry(self, textvariable=self.name)
        self.name_box.grid(row = 0, column = 1)
        self.name_box.focus()

        self.phone = StringVar()
        self.phone_box = Entry(self, textvariable = self.phone)
        self.phone_box.grid(row = 1, column = 1)

        self.address = StringVar()
        self.address_box = Entry(self, textvariable = self.address)
        self.address_box.grid(row = 2, column = 1)

        self.button = Button(self, text = "Add", command = self.add)
        self.button.grid(row = 5, column = 1)

        self.button = Button(self, text = "Reset", command = self.reset)
        self.button.grid(row = 6, column = 1)


    def add(self):
        with open("./asd.txt", "a+") as f:
            f.write(f"{self.name.get()} {self.phone.get()} {self.address.get()}\n")
            self.data_label["text"] = "Added Successfully"

        self.name_box.delete(0, END)
        self.phone_box.delete(0, END)
        self.address_box.delete(0, END)

    def reset(self):
        self.name_box.delete(0, END)
        self.phone_box.delete(0, END)
        self.address_box.delete(0, END)
        self.data_label["text"] = "Reset Successfully"


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x120")



if __name__ == "__main__":
    asd = App()
    frame = LoginFrame(asd)
    frame.mainloop()
