import smtplib
from tkinter import *


def send_message():
    
    address_info = address.get()
    
    email_body_info = email_body.get()
    
    print(address_info,email_body_info)
    
    sender_email = "evolverobotics.001@gmail.com"
    
    sender_password = "Evolverobo123@"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    
    print("Login successful")
    
    server.sendmail(sender_email,address_info,email_body_info)
    
    print("Message sent")
    
    address_entry.delete(0,END)
    email_body_entry.delete(0,END)
    
    
    

app = Tk()

app.geometry("350x350")

app.title("Python Mail Send App")

app.configure(bg='black')


heading = Label(text="Email Application",bg="Powder Blue",fg="gray",font=('arial',"15",'bold'),width="500",height="3",)

heading.pack()

address_field = Label(text="Recipient Address :",fg="white",font=('arial',"8",'bold'),bg="black")
email_body_field = Label(text="Message :",fg="white",font=('arial',"8",'bold'),bg="black")

address_field.place(x=15,y=85)
email_body_field.place(x=15,y=165)

address = StringVar()
email_body = StringVar()


address_entry = Entry(textvariable=address,width="50")
email_body_entry = Entry(textvariable=email_body,width="50")

address_entry.place(x=15,y=120)
email_body_entry.place(x=15,y=200)

button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="Powder Blue",font=('arial',"10",'bold'),fg="gray")

button.place(x=15,y=250)


mainloop()
