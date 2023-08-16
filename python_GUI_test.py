import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime


class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Primer shopping korpe")

        self.tasks = []

        self.task_name_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Task Name Label and Entry
        tk.Label(self.root, text="Dodajte proizvod:").grid(row=0, column=0, sticky="w")
        task_name_entry = tk.Entry(self.root, textvariable=self.task_name_var)
        task_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Priority Label and Dropdown

        tk.Label(self.root, text="Kolicina:").grid(row=1, column=0, sticky="w")
        #priority_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

  
        #priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=spin_box)

        #priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=priority_values)
        ##priority_dropdown = tk.Entry(self.root, validate='all', validatecommand=(vcmd, '%P')textvariable=self.priority_var)
        #priority_dropdown = tk.Entry(self.root, textvariable=self.priority_var)

        priority_dropdown = tk.Entry(self.root, textvariable=self.priority_var, validate="key")
        priority_dropdown['validatecommand'] = (priority_dropdown.register(test_Val),'%P','%d')
        #priority_dropdown.pack()



        #kolicina= int(self.priority_var.get())

        priority_dropdown.grid(row=1, column=1, padx=10, pady=5)


        # Due Date Label and Calendar
        #tk.Label(self.root, text="Due Date:").grid(row=2, column=0, sticky="w")
        due_date_entry = DateEntry(self.root, textvariable=self.due_date_var, date_pattern="yyyy-mm-dd")
        #due_date_entry.grid(row=2, column=1, padx=10, pady=5)

        

        # Add Task Button
        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=3, column=0, padx=10, pady=5)
        
        # Pregled ponude
        check_task_button = tk.Button(self.root, text="Prikazi ponudu", command=onClick)
        check_task_button.grid(row=3, column=1, padx=10, pady=5)

        # Task List Treeview
        self.task_list_treeview = ttk.Treeview(self.root, columns=("Priority", "Due Date"))
        self.task_list_treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.task_list_treeview.heading("#0", text="Proizvod")
        self.task_list_treeview.heading("Priority", text="Kolicina")
        self.task_list_treeview.heading("Due Date", text="Cena")

        # Delete Task Button
        delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_task_button.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Clear Task Button
        clear_task_button = tk.Button(self.root, text="Clear Task", command=self.clear_task)
        clear_task_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")
        
        # Checkout Button
        checkout_button = tk.Button(self.root, text="Platite", command=self.ispisi)
        checkout_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        # Exit Button
        exit_button = tk.Button(self.root, text="Izlaz", command=root.destroy)
        exit_button.grid(row=6, column=1, padx=10, pady=5, sticky="e")
        



    def add_task(self):
        name = self.task_name_var.get()
        priority = self.priority_var.get()
        #due_date = self.due_date_var.get()

        

        #if name and priority and due_date:
        if name and priority:
            if name in asortiman:
                
                cena=asortiman[name]
                task = Task(name, priority, cena)
                self.tasks.append(task)    

                
                if self.task_list_treeview.get_children()==():
                    self.task_list_treeview.insert("", tk.END, text=task.name, values=(task.priority, task.due_date))
                    self.task_name_var.set("")
                    self.priority_var.set("")
                    self.due_date_var.set("")
                else:
                    for child in self.task_list_treeview.get_children():
                        if self.task_list_treeview.item(child, 'text') == name:
                            broj=int(self.task_list_treeview.item(child, 'values')[0])+int(task.priority)
                            pris=self.task_list_treeview.item(child, 'values')[1]
                            self.task_list_treeview.item(child, text=name, values=(broj, pris))
                            self.task_name_var.set("")
                            self.priority_var.set("")
                            self.due_date_var.set("")
                            messagebox.showinfo("Obavestenje", "Proizvod vec postoji")
                            break
                        else:
                            self.task_list_treeview.insert("", tk.END, text=task.name, values=(task.priority, task.due_date))
                            self.task_name_var.set("")
                            self.priority_var.set("")
                            self.due_date_var.set("")
            else:
                messagebox.showerror("Error", "Molimo unesti proizvod iz ponude.")    
        else:
            messagebox.showerror("Error", "Molimo, popunite sva polja.")



    def delete_task(self):
        selected_item = self.task_list_treeview.selection()
        if selected_item:
            task_name = self.task_list_treeview.item(selected_item)["text"]
            for task in self.tasks:
                if task.name == task_name:
                    self.tasks.remove(task)
                    self.task_list_treeview.delete(selected_item)
                    break

    def clear_task(self):
        self.task_name_var.set("")
        self.priority_var.set("")
        self.due_date_var.set("")

    def ispisi(self):
        selected_item = self.task_list_treeview.selection()
        #messagebox.showinfo("Ovo je u korpi",  self.task_list_treeview.item(selected_item))
        #messagebox.showinfo("Ovo je u korpi",  self.task_list_treeview.set(I001,"Priority"))

        total = 0.0

        for child in self.task_list_treeview.get_children():
            total += float(self.task_list_treeview.item(child, 'values')[0])*float(self.task_list_treeview.item(child, 'values')[1])
        messagebox.showinfo("Ukupno za platiti", total)    

def test_Val(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

def ucitaj_datoteku(ulazna):
    with open(ulazna, encoding="UTF-8") as ulaz:
        asortiman = dict()
        for linija in ulaz:
            ime, cena = linija.split(",")
            asortiman[ime] = int(cena)
        return asortiman

def onClick():
    messagebox.showinfo("Ovo je ponuda proizvoda",  list(asortiman.keys()))



if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    asortiman = ucitaj_datoteku("cene.txt")
    root.mainloop()