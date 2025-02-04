from customtkinter import *
import spacy
from tkinter import messagebox
def analiz():
    try:
            nlp = spacy.load("en_core_web_sm")
            a = entr1.get().strip()
            doc = nlp(a)
            
            result_text ="Sözcük Analizi Sonuçları:\n\n" # Sonuçları bir string içinde topla
            for token in doc:
                result_text += f"{token.text} - {token.pos_} - {token.dep_}\n"

            text_box.configure(state="normal")  
            text_box.delete("1.0", "end")  
            text_box.insert("1.0", result_text) 
            text_box.configure(state="disabled")  # Düzenlemeyi kapat
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")  
spacy_window = CTk()
spacy_window.geometry("500x500")
spacy_window.resizable(0,0)
spacy_window.title("analysis of words ")
newframe = CTkFrame(master=spacy_window, fg_color="#3A3F44",height=460, width=460,corner_radius=12, border_color="#B0BEC5",border_width=1)
newframe.place(relx=0.5, rely=0.5, anchor="center")
entr1=CTkEntry(master=newframe, border_color="#B0BEC6", width=375, height=40, placeholder_text="Lütfen işlenecek metin yazınız",
font=("Arial", 15) ,
placeholder_text_color="grey",
 border_width=1,
corner_radius=20)
entr1.place(relx=0.420 ,rely=0.93, anchor="center")
entr1.bind("<Return>", lambda event: analiz()) 
button1= CTkButton(master=newframe, 
width=25, 
height=40
,text="⬆️"
,fg_color="white"
,hover_color="grey"
,text_color="black"
,corner_radius=20
,command=analiz)
button1.place(relx=0.90, rely=0.93, anchor="center")
text_box = CTkTextbox(master=newframe, width=451, height=390, fg_color="black", 
                      text_color="white", font=("Arial", 14), corner_radius=12)
text_box.place(relx=0.5, rely=0.440, anchor="center")
text_box.configure(state="disabled")


spacy_window.mainloop()