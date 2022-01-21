import os
from tkinter import *
from tkinter import filedialog,messagebox
root=Tk()
root.title("Searching File")
root.geometry('680x470')
root['background']='#68eddb'

# **--------------Searching operation-----------------------------------------------------------------------**
# print(os.__file__)
'''**--------------Searching any File in this computer--------*--Default search is Desktop if you enter wrong path--**'''
def show_files():
    filename=filedialog.askdirectory(initialdir=os.getcwd(),title="Select directory")
    location=filename
    print(location)
    try:
        os.chdir(location)
    except Exception as e:
        messagebox.showwarning("Warning","Please select Directory from where you want to search file")
    path = Label(root, text=location, font=('italic', 12, 'normal'), borderwidth=2, state=DISABLED)
    path.grid(row=0, column=1, sticky=W + E, ipadx=5, ipady=8, pady=10)

print("You Current Location is : ",os.getcwd())

path_button=Button(root,text='Browse',padx=50,pady=5,font=('arial',10,'bold'),bd=5,command=show_files)
path_button.grid(row=0,column=0,padx=50)

flabel = Label(root, text="File/Folder Name", font=('italic', 12, 'normal'), borderwidth=2)
flabel.grid(row=1, column=0, ipadx=5, ipady=8, pady=10)
search_item = Entry(root, font=('arial', 15, 'normal'))
search_item.grid(row=1, column=1, sticky=E + W, padx=5, pady=10, ipady=5)



def searching(item):
    global row
    fname=search_item.get()
    try:
        if "." in fname:           # If search item have ext. then else part not excute and match properly
            pass
        else:
            item_nex = item.split(".")[0]

        if fname == item_nex:
            print(fname)
            result = Label(root, text=f'''Directory path \n{dirpath}/{item}''', font=('italic', 12, 'normal'), borderwidth=2)
            result.grid(row=row, column=0,columnspan=3,sticky=W + E, ipadx=15, ipady=8, pady=5,padx=20)
            row +=1

            print("**----------------------------------------------------------**\n")
    except Exception as e:
        print(e)

row = 2
def start_search():
    global dirpath,dirname,dirfile
    for dirpath, dirname, dirfile in os.walk(os.getcwd()):
        for folder in dirname:
            searching(folder)
        for file in dirfile:
            searching(file)

search_button = Button(root, text='Search', padx=50, pady=5, font=('arial', 10, 'bold'), bd=5, command=start_search)
search_button.grid(row=1, column=2, padx=10)

root.mainloop()


