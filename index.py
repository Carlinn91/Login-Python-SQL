from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import databaser

#Criando janela

jan = Tk()
jan.title("CG Impressos - Painel de Controle")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.85)
jan.iconbitmap(default="icons/logoico.ico")


#adicionando Imagens
logo = PhotoImage(file="icons/logo.png")

#   Widgets  ---  frames
LeftFrame = Frame(jan, width=170, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=420, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=25, y=100)

UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=20, y=100)

UserEntry = ttk.Entry(RightFrame, width=40)
UserEntry.place(x=100, y=104)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=20, y=130)

PassEntry = ttk.Entry(RightFrame, width=40, show="*")
PassEntry.place(x=100, y=134)

def Login():
    databaser.cursor.execute; ("""
    SELECT * FROM User
    WHERE (User = ? AND Password = ?)
    """)
    print("Selecionou")
    VerifyLogin = databaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Informação de Login", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Informação de Login", message=" Acesso Negado. Verifique se este Cadastro no sistema!")

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=103, y=165)


def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=50000)
    RegisterButton.place(x=50000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=20, y=35)

    NomeEntry = ttk.Entry(RightFrame, width=40)
    NomeEntry.place(x=100, y=40)

    emailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
    emailLabel.place(x=20, y=65)

    emailEntry = ttk.Entry(RightFrame, width=40)
    emailEntry.place(x=100, y=70)

    def Registertodatabaser():
        Nome = NomeEntry.get()
        Email = emailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Nome == "" and Email == "" and User == "" and Pass == "" or Nome == "" and Email == ""):
            messagebox.showerror(title="Erro de Registro", message="Não Deixe Nenhum Campo Vazio. Preencha Todos os Campos")
        else:
            databaser.cursor.execute; ("""
            INSERT INTO Usuariosok(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Nome, Email, User, Pass))
            databaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada com Sucesso")

    Register = ttk.Button(RightFrame, text="Cadastrar", width=30, command=Registertodatabaser)
    Register.place(x=102, y=165)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeLabel.place(x=50000)
        NomeEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Voltando com widgets de Login
        LoginButton.place(x=103)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=200)

RegisterButton = ttk.Button(RightFrame, text="Cadastrar", width=20, command=Register)
RegisterButton.place(x=125, y=200)

jan.mainloop()
