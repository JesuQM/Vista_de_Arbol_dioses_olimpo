import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style, Treeview
import xml.etree.ElementTree as ET

class Arbol:

    def __init__(self, raiz):
 
            with open("hijos_del_olimpo.xml") as arbol:#abre el archivo y lo pone en la variable 
                Leer = arbol.read()#manda a leer el archivo

            NodoRaiz = ET.fromstring(Leer)#revisa las palabras que se encuentran dentro de cada nodo 
            Style =ttk.Style()
            Style.configure("Treeview",
            background = "#F0F8FF",foreground ="black",rowheight =45, fielbackground = "green"
            )#modifica el estilo del arbol 
            Style.map("Treeview",background=[("selected","#A1E825")])
            self.tree = Treeview(raiz)#funcion para ver el arbol en la interfaz
            self.tree.pack(expand=True, fill='both')#modifica la pestaña de la interfaz
            self.recorrer(NodoRaiz)#recorre el arbol
        

    def recorrer(self, d, nivel=0, padre=""):

        for hijo in d:
            print(hijo.tag, hijo.attrib)#imprimir los hijos y sus atributos 

            Nombre_Nodo = "<" + hijo.tag + ">"

            
            item = self.tree.insert(padre, 'end', None, text=Nombre_Nodo)

            if hijo.__len__() > 0:#revisa si despues de ese hijo hay mas datos 
                self.recorrer(hijo, nivel + 1, padre=item)
            else:
                
                if(hijo.text != None):#revisa si el nodo hijo tiene algun texto o si esta vacio 
                    self.tree.insert(item, 'end', None, text=hijo.text)

    
    
gui = tk.Tk()
gui.geometry("800x800")
gui.title ("ALungos hijos de los tres principales dioses  griegos")
Arbol(gui)
gui.mainloop()
