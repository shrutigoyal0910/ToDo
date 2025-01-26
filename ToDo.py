import tkinter
from tkinter import *
from tkinter import messagebox
task = []
counter = 1

def inputError():
    if(enterTaskField.get() == ""):
        messagebox.showerror("Input error!")
        return 0
    
    return 1

def clear_taskNumberField():
    taskToDeleteField.delete(0.0,END)

def clear_taskField():
    enterTaskField.delete(0,END)

def delete():
    global counter
    if(len(task) == 0):
        messagebox.showerror("No tasks :(")
        return
    
    num = taskToDeleteField.get(1.0, "end")

    if(num == ""):
        messagebox.showerror("Invalid input!")
        return
    else:
        task_no = int(num)

    clear_taskNumberField()

    task.pop(task_no - 1)
    counter -= 1

    TextArea.delete(1.0,END)

    for i in range(len(task)):
        TextArea.insert('end', "[ " + str(i + 1) + "] " + task[i])

def insertTask():
    global counter
    value = inputError()
    if(value == 0):
        return
    
    entry = enterTaskField.get() + "\n"

    task.append(entry)

    TextArea.insert('end -1 chars', "[" +str(counter)+ "]" + entry)

    counter += 1

    clear_taskField()


def exit():
    #win.destroy()
    root.quit()

if __name__ == "__main__":

    root = tkinter.Tk()

    root.configure (background = "light pink")
    root.title("To Do App")
    
    root.geometry("250x300")
    
    enterTask = Label(root, text = "Enter your task:", bg = "light pink", fg = "Black")
    enterTask.grid(row = 0, column = 2)
    
    enterTaskField = tkinter.Entry(root)
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    
    submit = Button (root, text = "Submit", fg = "Black", bg = "White", command = insertTask)
    submit.grid(row = 2, column = 2)
    
    TextArea = Text(root, height = 5, width = 25, font = "lucida 13", fg="black")
    TextArea.grid(row = 3, column = 2)

    taskToDelete = Label(root, text = "Task number to be deleted:", bg = "light blue")
    taskToDelete.grid(row = 4, column = 2)
    
    taskToDeleteField = Text(root, height = 1, width=2, bg = "White")
    taskToDeleteField.grid(row = 5, column = 2)
    delete = Button(root, text = "Delete", fg= "black", bg = "red", command = delete)
    delete.grid(row = 6, column = 2, pady = 5)
    Exit = Button(root, text = "Exit app", fg = "black", bg = "light green", command = exit)
    Exit.grid(row = 7, column = 2)
    
    root.mainloop()
