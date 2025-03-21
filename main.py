import tkinter as tk
from user import Usuarios

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("700x700")
ventana.resizable(False,False)

#instancia
usuario_1 = Usuarios()

#etiquetas
titulo = tk.Label(ventana,text="LOGIN", font=("Cambria",25)).place(x=200, y=50)
nombre = tk.Label(ventana, text="Nombre", font=("Cambria",15)).place(x=50,y=150)
nickname = tk.Label(ventana, text="Nickname", font=("Cambria",15)).place(x=50,y=200)
clave = tk.Label(ventana, text="Clave", font=("Cambria",15)).place(x=50,y=250)
by = tk.Label(ventana, text="by Danilo De los rios & Sebastian Pabon", font=("Segoe script",8)).place(x=20,y=650)

#campos de texto
txtNombre = tk.Entry(ventana)
txtNombre.place(x=150,y=160)
txtNickname = tk.Entry(ventana)
txtNickname.place(x=160,y=210)
txtClave = tk.Entry(ventana)
txtClave.place(x=130,y=260)
#panel
panel = tk.Text(ventana,height=10, width=40,state=tk.DISABLED)
panel.place(x=200,y=350)

#Funciones
def save_user():
    nombre = txtNombre.get()
    nickname = txtNickname.get()
    clave = txtClave.get()
    
    if nombre and nickname and clave:
        usuario_1.saveUser(nombre, nickname, clave)
        txtNombre.delete(0, tk.END)
        txtNickname.delete(0, tk.END)
        txtClave.delete(0, tk.END)
    else:
        print("Tienes que llenar todos los campos")

def listar():
    usuarios = usuario_1.listarUsers()
    panel.config(state=tk.NORMAL)
    panel.delete("1.0",tk.END)
    
    if usuarios:
        for usuario in usuarios:
            panel.insert(tk.END, f"Nombre: {usuario['nombre']}, Nickname: {usuario['nickname']}\n")
    else:
        panel.insert(tk.END, "No hay usuarios guardados\n")
        
    panel.config(state=tk.DISABLED)
#botones
button_guardar = tk.Button(ventana,text="Guardar", command=save_user).place(x=200,y=300)
button_listar = tk.Button(ventana,text="Usuarios guardados",command=listar).place(x=290,y=300)
    
ventana.mainloop()