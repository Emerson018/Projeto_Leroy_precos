import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

window = ctk.CTk()
window.title('Preços Leroy Merlin')
window.geometry('800x500')


def fecha_programa():
    window.destroy()

frame = ctk.CTkFrame(master=window)
frame.pack(
    pady=20,
    padx= 60,
    fill= 'both',
    expand=True
    )

font_label = ctk.CTkFont(
    family='Calibri',
    size=24,
    weight='bold'
    )

label = ctk.CTkLabel(
    master=frame,
    text= 'Procura LM',
    font=font_label,
    )
label.pack(
    pady=12,
    padx=10
    )

entry1 = ctk.CTkEntry(
    master=frame,
    placeholder_text='Insira o LM aqui'
    )
entry1.pack(
    pady=12,
    padx=10
    )

search_lm_button = ctk.CTkButton(
    master=frame,
    text='Validar preço',
    #command= find_price()
    )
search_lm_button.pack(
    pady=12,
    padx=10
    )

button_exit = ctk.CTkButton(
    master=window,
    text ='Fechar programa',
    command=window.destroy
    )
button_exit.pack(
    side='bottom',
    padx=10,
    pady=10,
    anchor='se'
    )




window.mainloop()


#NO VÍDEO DE ESTUDOS, EU PAREI EM 6:20:00
#9:45 mostra como colocar em dark mode e trocar as cores qndo troca os modos
#10:17 aparece como botar pop up    

'''
>>> pra add no programa:
-pop up com nom max 8 numeros.
-avisar que nao é possível letras
-daark mode e light mode
-texto mostrando o que foi adicionado, e caso ja exista, mostrar os valores
-index q mostra a qntd de lms na planilha
-texto mostrando que o valor já existe na planilha
-botao para mostrar os itens do excel(se possivel)
- 
'''