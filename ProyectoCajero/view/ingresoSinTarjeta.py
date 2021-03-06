from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import menuPrincipal, menuTransaccion


class MenuAccesoSinTarjeta:
    def __init__(self,window):
        self.window= window
        self.window.geometry("1250x580")
        self.window.resizable(0,0)
        self.window.iconbitmap('view/imagenes/LogoBancolombia.ico')
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        #self.window.state("zoomed")
        #cargar imagen
        fondoIngresoTarjetaContraseña= Image.open("VIEW/imagenes/IngresoTarjetaContraseña.png")
        resizeImagef=fondoIngresoTarjetaContraseña.resize((1250,580))
        fondoIngresoTarjetaContraseña= ImageTk.PhotoImage(resizeImagef)
        #iconos
        contraseñaIcon= Image.open("VIEW/imagenes/4.png")
        resizeImageC=contraseñaIcon.resize((300,50))
        contraseñaIcon=ImageTk.PhotoImage(resizeImageC)

        #IngresoTarjetaContraseña---------------------------------------------------------------------------------

        ingresoTarjetaContraseñafondo=Label(self.window, image=fondoIngresoTarjetaContraseña)
        ingresoTarjetaContraseñafondo.image=fondoIngresoTarjetaContraseña
        ingresoTarjetaContraseñafondo.place(x=0,y=0)

        ingresoTarjetaContraseñaLb=Label(self.window,image=contraseñaIcon,border=0)
        ingresoTarjetaContraseñaLb.image=contraseñaIcon
        ingresoTarjetaContraseñaLb.place(x=510,y=200)

        #Comando para la validación del entry(que sean 4 digitos y que sean numeros)
        def validate_entry(text, new_text):
        # Primero chequear que el contenido total no exceda los diez caracteres.
            if len(new_text) > 4:
                return False
        # Luego, si la validación anterior no falló, chequear que el texto solo
        # contenga números.
            return text.isdecimal()

        #Comando para eliminar espacio de texto
        #Entry para el ingreso de la contraseña
        ingresoTarjetaContraseñaTx = Entry(self.window, show="*",width=6,font=("Helvetica",24),border=0)
        ingresoTarjetaContraseñaTx.place(x=630,y=204)
        ingresoTarjetaContraseñaTx.focus_set()
        ingresoTarjetaContraseñaTx.config(validate='key',validatecommand=(self.window.register(validate_entry), "%S", "%P"))

        #botones IngresoTarjeta
        ingresoTarjetaBtIngresar= Button(self.window, padx=25,border=0, pady=15, bg="#7ed957",command=self.go_MenuTransacciones)
        ingresoTarjetaBtIngresar.place(x=100,y=345)

        ingresoTarjetaBtFinalizar= Button(self.window, padx=25,border=0, pady=15, bg="#e61717",command=self.go_MainMenu)
        ingresoTarjetaBtFinalizar.place(x=100,y=445)

    def go_MenuTransacciones(self):
        win=Toplevel()
        menuTransaccion.MenuTransaccion(win)
        self.window.withdraw()
        win.deiconify()

    def go_MainMenu(self):
        win=Toplevel()
        menuPrincipal.MenuPrincipal(win)
        self.window.withdraw()
        win.deiconify()

def page():
    window= Tk()
    MenuAccesoSinTarjeta(window)
    window.mainloop()

if __name__ == "__main__":
    page()