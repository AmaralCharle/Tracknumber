from tkinter import *
import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

# Configurações da janela principal
root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False, False)
root.configure(bg='#96BFFF')

# Chave da API OpenCage
key = "9392dcc447db45728df3a82cbe639e50"

def track():
    enter_nb = entry.get()
    number = phonenumbers.parse(enter_nb)

    location = geocoder.description_for_number(number, 'en')
    country.config(text=location)

    service = carrier.name_for_number(number, 'en')
    sim.config(text=service)

    query = str(location)

    try:
        results = OpenCageGeocode(key).geocode(query)
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
        else:
            raise ValueError("No results found")

        myMap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(myMap)
        myMap.save("myLocation.html")
    except Exception as e:
        print(f"Error: {e}")
        country.config(text="Error fetching location")
        sim.config(text="")

def open_map():
    webbrowser.open("myLocation.html")

# Carregando imagens
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#96BFFF").place(x=135, y=40)

search = PhotoImage(file="search.png")
Label(root, image=search, bg="#96BFFF").place(x=14, y=244)

# Título
heading = Label(root, text="Track Number", font='arial 20 bold', fg="#39281E", bg="#96BFFF")
heading.place(x=90, y=190)

# Campo de entrada
entry = StringVar()
enter_nb = Entry(root, textvariable=entry, width=17, justify='center', bd=0,
                 font='arial 20', bg="#2C3541", fg="white")
enter_nb.place(x=54, y=258)

# Botão de busca
search_button = PhotoImage(file='search_icon.png')
btn = Button(root, image=search_button, cursor='hand2', bg="#96BFFF", bd=0,
             command=track, activebackground='#ED8051')
btn.place(x=155, y=308)

# Labels para exibir resultados
country = Label(root, text="Country", bg='#96BFFF', fg='black', font='arial 14 bold')
country.place(x=55, y=370)

sim = Label(root, text="SIM", bg='#96BFFF', fg='black', font='arial 14 bold')
sim.place(x=255, y=370)

# Botão para abrir o mapa
open_map_btn = Button(root, text="Location", width=10, cursor='hand2', bg="#EE8C62", bd=0,
                      command=open_map, activebackground='#ED8051', font='arial 14 bold')
open_map_btn.place(x=125, y=430)

# Instagram
insta_page = Label(root, text="@pythonagham", bg='#96BFFF', fg='black', font='arial 10 bold italic')
insta_page.place(x=135, y=550)

# Loop principal da interface
root.mainloop()
