import folium
from tkinter import *
from tkinter import messagebox

# 18.513704622113835, -70.10808234381392
# a = input("Ingresa la logitud \n")
# b = input("Ingresa la latitud \n")
# c = input("Ingresa el tipo de mapa \n")

# Gmap = folium.Map(location=[a, b], tiles=c, zoom_start=10, control_scale=True)
# Gmap.save('index.html')

ventana = Tk()
ventana.geometry("600x500+400+125")
ventana.title("GMap")
# ventana.iconbitmap("mini-goo.ico")
ventana.config(background="#000000")
Titulo = Label(text="GMap", font=("Cambria", 20), bg="#24b43c", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(text="Creador: N05TR4  Version: 1.0", font=("Cambria", 10), bg="#24b43c", fg="white", width="500",
                height="1")
Titulo1.pack()
Titulo1 = Label(text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500", height="1")
Titulo1.place(x=0, y=475)

# Variables principales
longitud = StringVar()
latitud = StringVar()
tipoMapa = StringVar()

# barra de captura de los datos
label = Label(text="Longitud", font=("Cambria", 12), fg="white", bg="black")
label.place(x=40, y=100)
longitud_entry = Entry(textvariable=longitud, width=25)
longitud_entry.place(x=180, y=100)

label = Label(text="Latitud", font=("Cambria", 12), fg="white", bg="black")
label.place(x=40, y=150)
latitud_entry = Entry(textvariable=latitud, width=25)
latitud_entry.place(x=180, y=150)

label = Label(text="Tipo de Mapa", font=("Cambria", 12), fg="white", bg="black")
label.place(x=40, y=200)
tipoMapa_entry = Entry(textvariable=tipoMapa, width=25)
tipoMapa_entry.place(x=180, y=200)

label = Label(text="Tipos de Mapas Disponibles", font=("Cambria", 16), fg="white", bg="black")
label.place(x=40, y=250)

label = Label(text="OpenStreetMap", font=("Cambria", 10), fg="white", bg="black")
label.place(x=40, y=290)

label = Label(text="Stamen Toner", font=("Cambria", 10), fg="white", bg="black")
label.place(x=40, y=310)

label = Label(text="Stamen Terrain", font=("Cambria", 10), fg="white", bg="black")
label.place(x=40, y=330)


# Funcion para realizar la busqueda con los parametros
def Map():
    try:
        longitud_data = longitud.get()
        latitud_data = latitud.get()
        tipoMapa_data = tipoMapa.get()
        Gmap = folium.Map(location=[longitud_data, latitud_data], tiles=tipoMapa_data, zoom_start=30,
                          control_scale=True)
        Gmap.save('index.html')
        messagebox.Dialog(title="Listo", message="Se ha buscado la ubicacion")
    except:
        messagebox.showerror(title="ERROR!", message="ERROR! de los parametros")



# Creacion del boton
btnGenerar = Button(ventana, text="Buscar", font=("Cambria", 12), command=Map, width="20", fg="white",
                    height="1", bg="#24b43c")
btnGenerar.place(x=180, y=400)


def acercaDe():
    messagebox.showinfo(title="Acerca De",
                        message="Creador:N05TR4 "
                                "Fecha: 08/04/2021 "
                                " Descripcion: Con las coordenadas genera un archivo index.html"
                                " donde contiene el mapa con la ubicacion")




# Creando barra de menu
menubarra = Menu(ventana)
ventana.config(menu=menubarra)
filemenu = Menu(menubarra)
filemenu = Menu(menubarra, tearoff=0)
menubarra.add_cascade(label="Opcion", menu=filemenu)
filemenu.add_command(label="Acerca de", command=acercaDe)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=ventana.quit)


if __name__ == '__main__':
    ventana.mainloop()
