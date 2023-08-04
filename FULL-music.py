#import statements
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk
import tkinter as tk


#database connection
con = pymysql.connect(host="localhost",user="root",password="your_password",database="your_database")
cur = con.cursor()

#global declarations
global root,screen

#add songs starts
def addS():
    
    
    root = Toplevel(screen)
    root.title("Add Music Record")
    root.geometry("1280x720+150+80")
    root.configure(bg="#d7dae2")
                   
    
    def songadd():

        title = songInfo1.get()
        artist = songInfo2.get()
        album = songInfo3.get()
        genre = songInfo4.get()
        rlsyr = songInfo5.get()
                
        try:  
            cur.execute('insert ignore into artist(artist_name) values(%s)',(artist))
            cur.execute("select id from artist where artist_name = '"+artist+"';")
            artist_id = cur.fetchone()[0]
            cur.execute('insert ignore into album(album_name, artist_id) values(%s,%s)',(album, artist_id))
            cur.execute("select id from album where album_name = '"+album+"';")
            album_id = cur.fetchone()[0]
            cur.execute('insert ignore into genre(genre_name) values(%s)',(genre))
            cur.execute("select id from genre where genre_name = '"+genre+"';")
            genre_id = cur.fetchone()[0]
            cur.execute('insert ignore into track(title, album_id, genre_id, artist_id, rlsyr) values(%s,%s,%s,%s,%s)',(title, album_id, genre_id, artist_id, rlsyr))
            con.commit()
            messagebox.showinfo('Success',"Song Added Successfully")
        except:
            messagebox.showinfo("Error","Can't Add Song Into Database")

        root.destroy()

    
    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,con,cur

        

    img =Image.open("images/add.jpg")
    img = img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
                
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                
    canvas = Canvas(root,width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.create_image(0,0,image = img, anchor="nw")
    canvas.config(bg="white",width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.pack()

    
     


    headingFrame1 = Frame(root,bg="#2f2e2e",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Song Record",font=("roboto",40,'bold'), bg= "blue", fg='white')
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #textframe
    labelFrame = Frame(root, bg="grey")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    #label and textbox
    lb1 =Label(labelFrame, text="Title:", font='Helvetica 13 bold',bg="white", fg='black')
    lb1.place(relx=0.05,rely=0.16, relheight=0.08,)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.16, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="Artist:", font='Helvetica 13 bold',bg="white", fg='black')
    lb2.place(relx=0.05,rely=0.32, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3,rely=0.32, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="Album:", font='Helvetica 13 bold',bg="white", fg='black')
    lb3.place(relx=0.05,rely=0.48, relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3,rely=0.48, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Genre:", font='Helvetica 13 bold',bg="white", fg='black')
    lb4.place(relx=0.05,rely=0.64, relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3,rely=0.64, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame,text="Release Year:", font='Helvetica 13 bold',bg="white", fg='black')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
    #button
    SubmitBtn = Button(root,text="Submit",font='Helvetica 12 bold',bg='white', fg='black',command=songadd)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Home",font='Helvetica 12 bold',bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

#add songs ends

#delete songs starts
def deleteS():
    global root
    
    root = Toplevel(screen)
    root.title("Delete Music Record")
    root.geometry("1280x720+150+80")
    root.configure(bg="#d7dae2")

    def deletesong():

        title = songInfo1.get()
        
        try:
            cur.execute("delete from track, album, artist using track join album join artist on track.artist_id=artist.id and track.album_id=album.id where track.title = '"+title+"';")
            con.commit()
            messagebox.showinfo('Success',"Song Record Deleted Successfully")
        except:
            messagebox.showinfo("Please Check Song Title")

        songInfo1.delete(0, END)
        root.destroy()


    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,con,cur

    img =Image.open("images/delete.jpg")
    img = img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
                
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                
    canvas = Canvas(root,width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.create_image(0,0,image = img, anchor="nw")
    canvas.config(bg="white",width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.pack()
                 

    headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Song Record",font='Helvetica 14 bold', bg="white", fg='black')
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg="#010103")
    labelFrame.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.2)

    lb2 = Label(labelFrame,text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05,rely=0.5)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Submit",font='Helvetica 11 bold',bg="#010103", fg='white',command=deletesong)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",font='Helvetica 11 bold',bg="#010103", fg='white', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

    root.mainloop()
#delete songs ends

#view starts    
def view(): 

    root = Toplevel(screen)
    root.title("View Songs")
    root.geometry("1280x720+150+80")
    root.configure(bg="#d7dae2")
    
    
    img =Image.open("images/view.jpg")
    img = img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
                
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                
    canvas = Canvas(root,width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.create_image(0,0,image = img, anchor="nw")
    canvas.config(bg="white",width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.pack()

            
    headingFrame1 = Frame(root,bg="#d4b890",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Songs",font='Helvetica 14 bold', bg="#090a0c", fg='white', )
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="All Songs",font='Helvetica 10 bold',bg='black', fg='white', command=viewallsongs)
    btn1.place(relx=0.28,rely=0.42, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="View Playlists",font='Helvetica 10 bold',bg='black', fg='white', command=viewplaylists)
    btn2.place(relx=0.28,rely=0.52, relwidth=0.45,relheight=0.1)

    quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

#view ends

#view all songs starts
def viewallsongs(): 
    root = Toplevel(screen)
    root.title("View All Songs")
    root.geometry("1280x720+150+80")
    root.configure(bg="#d7dae2")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    try:
        cur.execute("select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id order by track.title;")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view all songs ends

#view playlists starts
def viewplaylists(): 

    root = Toplevel(screen)
    root.title("View Playlists")
    root.geometry("1280x720+150+80")
    root.configure(bg="#d7dae2")
    
    
    img =Image.open("images/viewplaylists.jpg")
    img = img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
                
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                
    canvas = Canvas(root,width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.create_image(0,0,image = img, anchor="nw")
    canvas.config(bg="white",width = root.winfo_screenwidth(), height = root.winfo_screenheight())
    canvas.pack()
            
    headingFrame1 = Frame(root,bg="#dbd1c6",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Playlists",font='Helvetica 14 bold', bg="#6b4c38", fg='white',)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Rock",font='Helvetica 10 bold',bg='black', fg='white', command=viewrock)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Pop",font='Helvetica 10 bold',bg='black', fg='white', command=viewpop)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="Hip-Hop",font='Helvetica 10 bold',bg='black', fg='white', command=viewhiphop)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Classical",font='Helvetica 10 bold',bg='black', fg='white', command=viewclassical)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view playlists ends


#view playlist1 starts
def viewrock(): 
    
    root = Tk()
    root.title("View Rock Music")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    genre = "Rock"
    try:
        cur.execute("select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id where genre.genre_name= '"+genre+"';")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view playlist1 ends



#view playlist2 starts
def viewpop(): 
    
    root = Tk()
    root.title("View Pop Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    genre = "Pop"
    try:
        cur.execute("select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id where genre.genre_name= '"+genre+"';")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view playlist2 ends



#view playlist3 starts
def viewhiphop(): 
    
    root = Tk()
    root.title("View Hip-Hop Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    genre = "Hip-Hop"
    try:
        cur.execute("select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id where genre.genre_name= '"+genre+"';")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)    
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view playlist3 ends



#view playlist4 starts
def viewclassical(): 
    
    root = Tk()
    root.title("View Classical Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    genre = "Classical"
    try:
        cur.execute("select track.title, artist.artist_name, album.album_name, genre.genre_name, track.rlsyr from track join album join artist join genre on track.artist_id=artist.id and track.album_id=album.id and track.genre_id=genre.id where genre.genre_name= '"+genre+"';")
        rows = cur.fetchall()
        con.commit()
        for i in rows:
            tree.insert("", tk.END, values=i)
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#view playlist4 ends


def main_screen():

    global screen
    global root
    
    screen=Tk()
    screen.title("Music Collection Manager")
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    img =Image.open("images/main.jpg")
    img = img.resize((screen.winfo_screenwidth(),screen.winfo_screenheight()))
    img = ImageTk.PhotoImage(img)
        

    background_label = tk.Label(screen, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    lblTitle = Label(text="Music Collection Manager",font=("roboto",40,'bold'),fg="orange",bg="black")
    lblTitle.pack(pady=30)
    """
    bordercolor=Frame(screen,bg="black", width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="white",width=800,height=400)
    mainframe.pack(padx=20,pady=20)
    """

    

    Button(screen,text="Add Song",height="3", width=30,bg="white",fg="black",bd=5,command=addS).pack(pady=20)
    Button(screen,text="Delete Song",height="3", width=30,bg="white",fg="black",bd=5,command=deleteS).pack(pady=20)
    Button(screen,text="View Songs",height="3", width=30,bg="white",fg="black",bd=5,command=view).pack(pady=20)


    Button(screen,text="Quit",height="3", width=30,bg="white",fg="black",bd=5,command=screen.destroy).pack(pady=120)

    
    screen.mainloop()

main_screen()
