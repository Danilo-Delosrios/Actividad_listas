package Clases;

import java.util.ArrayList;

public class Usuarios {
    
    private String nombre;
    private String nickname;
    private String clave;
    
    ArrayList<String>list_user=new ArrayList();
    
    public boolean guardarUsuarioList(String nombre,String nickname,String clave){
    list_user.add(nombre);
    list_user.add(nickname);
    list_user.add(clave);    
    return true;
    }

    public String getNombre() {
        return nombre;
    }

    public String getNickname() {
        return nickname;
    }

    public String getClave() {
        return clave;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public void setClave(String clave) {
        this.clave = clave;
    }
    
    public ArrayList<String> listarUsuario_list(){
    return list_user;
    }
    
    
}
