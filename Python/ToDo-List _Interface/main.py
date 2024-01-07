from tkinter import *
import tkinter as tk


""" Início Tkinter """

logo =  "                     ",  "_____                   _             _ \n", \
      "     /////|           " + "|_   _|__ _ __ _ __ ___ (_)_ __   __ _| |\n" , \
      "    ///// |    (\       " + "| |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |\n" , \
      "   |~~~|  |    \ \      " + "| |  __/ |  | | | | | | | | | | (_| | |\n" ,  \
      "   |===|  |     \ \     " + "|_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\n" , \
      "   |T  |  |     / '|   " + "         _____     ____   ___  _     ___    _____\n" + \
      "   | D |  |     \ '/  " + "         |_   _|__ |  _ \ / _ \| |   |_ _|__|_   _|\n" + \
      "   |  L| /        \      " + "        | |/ _ \| | | | | | | |    | |/ __|| |  \n" + \
      "   |===|/         ==).   " + "        | | (_) | |_| | |_| | |___ | |\__ \| | \n" + \
      "   '---'         (__)   " +  "         |_|\___/|____/ \___/|_____|___|___/|_| \n"

print(logo)


comprimeto_tela = 1000
largura_tela = 600

root = tk.Tk()
root.geometry(f"{comprimeto_tela}x{largura_tela}")
root.config(bg="#040404")
root.title("ToDO-List Terminal")

# Logo_livro
logo_livro_l1 = Label(root,  text="                    ", bg="#040404")
logo_livro_l2 = Label(root,  text="  /////|            ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l3 = Label(root,  text=" ///// |    (\      ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l4 = Label(root,  text="|~~~|  |    \ \     ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l5 = Label(root,  text="|===|  |     \ \    ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l6 = Label(root,  text="|T  |  |     / '|   ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l7 = Label(root,  text="| D |  |     \ '/   ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l8 = Label(root,  text="|  L| /        \    ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l9 = Label(root,  text="|===|/         ==)p ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")
logo_livro_l10 = Label(root, text="'---'         (__)  ", font=("Courier", 13 , "bold"), fg="brown", bg="#040404")

logo_livro_l1.grid(row=0, column=0, padx=10, pady=0)
logo_livro_l2.grid(row=2, column=0, padx=10, pady=0)
logo_livro_l3.grid(row=3, column=0, padx=10, pady=0)
logo_livro_l4.grid(row=4, column=0, padx=10, pady=0)
logo_livro_l5.grid(row=5, column=0, padx=10, pady=0)
logo_livro_l6.grid(row=6, column=0, padx=10, pady=0)
logo_livro_l7.grid(row=7, column=0, padx=10, pady=0)
logo_livro_l8.grid(row=8, column=0, padx=10, pady=0)
logo_livro_l9.grid(row=9, column=0, padx=10, pady=0)
logo_livro_l10.grid(row=10, column=0, padx=10, pady=0)

# Logo_texto

logo_texto_l1 = Label(root,  text=" _____                   _             _ ", font=("Courier", 13 , "bold"), fg="green", bg="#040404")
logo_texto_l2 = Label(root,  text="|_   _|__ _ __ _ __ ___ (_)_ __   __ _| |", font=("Courier", 13 , "bold"), fg="green", bg="#040404")
logo_texto_l3 = Label(root,  text="  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |", font=("Courier", 13 , "bold"), fg="green", bg="#040404")
logo_texto_l4 = Label(root,  text="  | |  __/ |  | | | | | | | | | | (_| | |", font=("Courier", 13 , "bold"), fg="green", bg="#040404")
logo_texto_l5 = Label(root,  text="  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|", font=("Courier", 13 , "bold"), fg="green", bg="#040404")
logo_texto_l6 = Label(root,  text="   _____     ____   ___  _     ___    _____ ", font=("Courier", 13 , "bold"), fg="magenta", bg="#040404")
logo_texto_l7 = Label(root,  text="  |_   _|__ |  _ \ / _ \| |   |_ _|__|_   _|", font=("Courier", 13 , "bold"), fg="magenta", bg="#040404")
logo_texto_l8 = Label(root,  text="    | |/ _ \| | | | | | | |    | |/ __|| |  ", font=("Courier", 13 , "bold"), fg="magenta", bg="#040404")
logo_texto_l9 = Label(root,  text="    | | (_) | |_| | |_| | |___ | |\__ \| |  ", font=("Courier", 13 , "bold"), fg="magenta", bg="#040404")
logo_texto_l10 = Label(root, text="    |_|\___/|____/ \___/|_____|___|___/|_|  ", font=("Courier", 13 , "bold"), fg="magenta", bg="#040404")

logo_texto_l1.grid(row=1, column=1, padx=0, pady=0)
logo_texto_l2.grid(row=2, column=1, padx=0, pady=0)
logo_texto_l3.grid(row=3, column=1, padx=0, pady=0)
logo_texto_l4.grid(row=4, column=1, padx=0, pady=0)
logo_texto_l5.grid(row=5, column=1, padx=0, pady=0)
logo_texto_l6.grid(row=6, column=1, padx=0, pady=0)
logo_texto_l7.grid(row=7, column=1, padx=0, pady=0)
logo_texto_l8.grid(row=8, column=1, padx=0, pady=0)
logo_texto_l9.grid(row=9, column=1, padx=0, pady=0)
logo_texto_l10.grid(row=10, column=1, padx=0, pady=0)






root.mainloop()
