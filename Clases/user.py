class Usuarios:
    def __init__(self):
        self.lista_usuarios = []
        
    def saveUser(self,nombre,nickname,clave):
        usuario = {"nombre":nombre,"nickname":nickname,"clave":clave}
        self.lista_usuarios.append(usuario)
    
    def listarUsers(self):
        return self.lista_usuarios