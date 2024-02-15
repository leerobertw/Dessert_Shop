from Order import Order
from MenuItems import *
from update_dialog import *

def candy(event):
    dialog = UpdateDialog(window, "Add Candy")
    # Add Candy to your order here
    order.add_item(Candy(dialog.amount))
    update_order_list()

def cookies(event):
    dialog = UpdateDialog(window, "Add Cookies")
    # Add Cookies to your order here
    order.add_item(Cookies(dialog.amount))
    update_order_list()

def ice_cream(event):
    dialog = UpdateDialog(window, "Add Ice Cream")
    # Add IceCream to your order here
    order.add_item(IceCream(dialog.amount, IceCreamFlavors.vanilla, IceCreamConeType.cone))
    update_order_list()

def sundae(event):
    sundae_item = Sundae()
    fudge = UpdateDialog(window, "Add Fudge")
    for f in range(fudge.amount):
        sundae_item.add_topping(SundaeToppings.hot_fudge)

    strawberry = UpdateDialog(window, "Add Strawberry")
    for s in range(strawberry.amount):
        sundae_item.add_topping(SundaeToppings.strawberry_syrup)

    caramel = UpdateDialog(window, "Add caramel")
    for c in range(caramel.amount):
        sundae_item.add_topping(SundaeToppings.carmel_syrup)

    peanuts = UpdateDialog(window, "Add Peanuts")
    for p in range(peanuts.amount):
        sundae_item.add_topping(SundaeToppings.peanuts)

    coconut = UpdateDialog(window, "Add Coconut")
    for c in range(coconut.amount):
        sundae_item.add_topping(SundaeToppings.coconut)
    order.add_item(sundae_item)
    update_order_list()

def update_order_list():
    listbox_data.set(order.get_items())

def show_total(event):
    global order
    total, tax = order.get_total_and_tax()
    total_label = TotalLabel(window, "Total", total, tax)
    if total_label.was_ok_pressed:
        order = Order()
        update_order_list()


# You will need to create your order
order = Order()
window = tk.Tk()
window.title(f"Dessert Ordering Tool")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

listbox_data = tk.StringVar(window, order.get_items())
listbox = tk.Listbox(window, selectmode='SINGLE', listvariable=listbox_data)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_add = tk.Button(frm_buttons, text="Candy")
btn_add.bind("<ButtonRelease>", candy)
btn_update = tk.Button(frm_buttons, text="Cookies")
btn_update.bind("<ButtonRelease>", cookies)
btn_remove = tk.Button(frm_buttons, text="Ice Cream")
btn_remove.bind("<ButtonRelease>", ice_cream)
btn_Sundae = tk.Button(frm_buttons, text="Sundae")
btn_Sundae.bind("<ButtonRelease>", sundae)
btn_Total = tk.Button(frm_buttons, text="Total")
btn_Total.bind("<ButtonRelease>", show_total)

btn_add.grid(row=0, column=0, sticky="ew", padx=5)
btn_update.grid(row=1, column=0, sticky="ew", padx=5)
btn_remove.grid(row=2, column=0, sticky="ew", padx=5)
btn_Sundae.grid(row=3, column=0, sticky="ew", padx=5)
btn_Total.grid(row=4, column=0, sticky="ew", padx=5, pady=15)
frm_buttons.grid(row=0, column=0, sticky="ns")
listbox.grid(row=0, column=1, sticky="nsew")

window.mainloop()
