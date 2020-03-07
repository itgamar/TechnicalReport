import tkinter as tk

window = tk.Tk()
# insert window dimension here
window.geometry("1200x800")
# ability to modify the size in terms of height and width
window.resizable(False, False)
window.configure(background="white")


# insert title here
window.title("Rapporto tecnico")
text_o_customer = "Cliente"
text_o_address = "Luogo intervento / indirizzo"


def press_button_create():
    text = "ciaone"
    #text_out = tk.Label(window, text=text, fg="black", font=("Lucida Console", 12))
    #text_out.grid(row=0, column=1)


# CUSTOMER
text_o_customer = tk.Label(window, background="white", text=text_o_customer, fg="black", font=("Lucida Console", 12))
text_o_customer.grid(row=1, column=0, sticky="W", padx=0, pady=0)
text_i_customer = tk.Entry(width=180)
text_i_customer.grid(row=2, column=0, sticky="WE", padx=10, pady=0)
#text_i_customer.insert(0, "a default value")

# ADDRESS
text_o_address = tk.Label(window, background="white", text=text_o_address, fg="black", font=("Lucida Console", 12))
text_o_address.grid(row=3, column=0, sticky="W", padx=0, pady=0)
text_i_address = tk.Entry()
text_i_address.grid(row=4, column=0, sticky="WE", padx=10, pady=0)

#button_create = tk.Button(text="button 1", command=press_button_create)
#button_create.grid(row=0, column=0)



if __name__ == "__main__":
    window.mainloop()