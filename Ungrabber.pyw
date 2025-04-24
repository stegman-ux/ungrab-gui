import customtkinter as ctk
import Ungrabber # Grand merci à lululepu pour cette incroyable module , qui peux etre facilement utiliser
import subprocess
import webbrowser
app = ctk.CTk()
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")



app.geometry("1000x860")
app.title("Ungrabber GUI - Made by intrable")

def ungrab():
    file = entry_ungrab.get() # cette ligne obtiens le nom du fichier que vous mettez dans l'entry
    result = Ungrabber.decompile(file)  # ca c'est la simple commande de la lib "ungrabber" que lululepy a crée , elle permet de décompiler le fichier et trouver un wehook.
    entry.delete(0, ctk.END)
    entry.insert(0, f"{result}")  # et mets les résultat dans l'entry final
    
label = ctk.CTkLabel(master=app,text="Veuillez entrer le nom du fichier .exe à analyser (Le fichier dois etre dans le dossier de ce tool) : ", text_color="red")
label.pack()

entry_ungrab = ctk.CTkEntry(master=app,width=400,height=30)
entry_ungrab.pack()



label_info = ctk.CTkLabel(master=app,text="Veuillez appuyer sur le bouton ci-dessous pour analyser le fichier .exe : ", text_color="red")
label_info.pack()

button = ctk.CTkButton(master=app,text="Ungrab",command=ungrab)
button.pack()


label2 = ctk.CTkLabel(master=app,text="Résultat de l'analyse Ungrab : ")
label2.pack()

entry = ctk.CTkEntry(master=app,width=950,height=70)
entry.pack()


def discord():
    webbrowser.open("https://discord.gg/freeforreal")
    
def github():
    webbrowser.open("https://github.com/stegman-ux")

label_pourseparer = ctk.CTkLabel(master=app,text="‎ ")
label_pourseparer.pack()

button_discord = ctk.CTkButton(master=app,text="Rejoindre le discord",command=discord)
button_discord.pack()



button_github = ctk.CTkButton(master=app,text="Lien github",command=github)
button_github.pack()






app.mainloop()