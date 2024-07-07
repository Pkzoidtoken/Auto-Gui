from tkinter import *
import threading
root = Tk()

def write_file(name:str,code:str,new:bool):
    if new == False:
        with open(name,"a") as f:
            f.write(f"{code}")
    else:
        with open(name,"w") as f:
            f.write(f"{code}")

user_choice = int(input("1:Custom Frame 2:Default"))

DEFAULT_CODE = (
    """
from tkinter import *
root = Tk()
root.wm_attributes("-transparentcolor", "grey")
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')
    """,
    """
root.mainloop()
    """
)

def add_assets():
    ask_user,amount = input("button etc.?").split()
    if ask_user == "Button":
        for i in range(0,int(amount)):
            ask_text = input("Button Text: ")
            ask_x,ask_y = input("X,Y").split()
            Button(root,text=ask_text).place(x=ask_x,y=ask_y)
            CODE = f"""
{ask_user}{i} = Button(root,text="{ask_text}")\n
{ask_user}{i}.place(x={ask_x},y="{ask_y}")
            """
            write_file(name="modern.py",code=CODE,new=False)
    
    elif ask_user == "Label":
        for i in range(0,int(amount)):
            ask_text = input("Label Text: ")
            ask_x,ask_y = input("X,Y").split()
            Label(root,text=ask_text).place(x=ask_x,y=ask_y)
            CODE = f"""
{ask_user}{i} = Label(root,text="{ask_text}")\n
{ask_user}{i}.place(x={ask_x},y="{ask_y}")
            """
            write_file(name="modern.py",code=CODE,new=False)
    elif ask_user == "Entry":
        for i in range(0,int(amount)):
            ask_Width = input("Width: ")
            ask_x,ask_y = input("X,Y").split()
            Entry(root,text=ask_Width).place(x=ask_x,y=ask_y)
            CODE = f"""
{ask_user}{i} = Entry(root,width="{ask_Width}")\n
{ask_user}{i}.place(x={ask_x},y="{ask_y}")
            """
            write_file(name="modern.py",code=CODE,new=False)

    elif ask_user == "image":
        for i in range(0,int(amount)):
            ask_image = input("Image: ")
            ask_x,ask_y = input("X,Y").split()
            lab_image = PhotoImage(file=ask_image)
            Label(root,image=lab_image,border=0).place(x=ask_x,y=ask_y)
            
            CODE = f"""
{ask_image.split(".")[0]}{i} = PhotoImage(file="{ask_image}")
{ask_user}{i} = Label(root,image={ask_image.split(".")[0]}{i},border=0,width=0,height=0)\n
{ask_user}{i}.place(x={ask_x},y="{ask_y}")
            """
            write_file(name="modern.py",code=CODE,new=False)

def background_while():
    while True:
        add_assets()

if user_choice == 1:
    def move_app(e):
        root.geometry(f'+{e.x_root}+{e.y_root}')
    frame_ask = input("Enter Frame Image Name: ")
    x,y = input("Geometry Size x,y: ").split()
    HALF_CODE = f"""
frame_photo = PhotoImage(file={frame_ask})
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.pack(fill=BOTH,expand=True)
frame_label.bind("<B1-Motion>", move_app)
"""
    write_file("modern.py",f"{DEFAULT_CODE[0]}\nroot.geometry('{x}x{y}')\n{HALF_CODE}",new=True)
    root.overrideredirect(1)
    root.wm_attributes("-transparentcolor", "grey")
    frame_photo = PhotoImage(file=frame_ask)
    frame_label = Label(root,border=0,bg='grey',image=frame_photo)
    frame_label.pack(fill=BOTH,expand=True)
    root.geometry(f"{x}x{y}")
    frame_label.bind("<B1-Motion>", move_app)
    add_assets()
else:
    pass
    
if __name__ == "__main__":
    task = threading.Thread(target=background_while)
    task.start()
    root.mainloop()
