import customtkinter as ctk
from PIL import Image


def cash_payment_screen(frame, total_amount, back_to_payment_screen):
    for widget in frame.winfo_children():
        widget.destroy()

    # Tytuł
    title_label = ctk.CTkLabel(
        frame,
        text="Płatność gotówką",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)
     # Pozioma kreska
    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    # Wyświetlenie należności
    amount_label = ctk.CTkLabel(
        frame,
        text=f"Należność: {total_amount:.2f} zł",
        font=ctk.CTkFont(size=20),
        text_color="black"
    )
    amount_label.pack(pady=10)

    # Pole do wprowadzenia kwoty
    paid_amount_var = ctk.DoubleVar(value=0.0)

    input_field = ctk.CTkEntry(
        frame,
        textvariable=paid_amount_var,
        font=ctk.CTkFont(size=16),
        width=200
    )
    input_field.pack(pady=10)

    # Funkcja obsługi wpłaty
    def handle_payment():
        paid_amount = paid_amount_var.get()
        if paid_amount >= total_amount:
            change = paid_amount - total_amount
            result_label.configure(text=f"Płatność przyjęta. Reszta: {change:.2f} zł Odbierz resztę oraz bilety z drukarki", text_color="green")
        else:
            remaining = total_amount - paid_amount
            result_label.configure(text=f"Niewystarczająca kwota. Brakuje: {remaining:.2f} zł", text_color="red")

    # Przycisk potwierdzenia
    confirm_button = ctk.CTkButton(
        frame,
        text="Potwierdź wpłatę",
        font=ctk.CTkFont(size=16),
        width=200,
        command=handle_payment
    )
    confirm_button.pack(pady=20)

    # Wynik płatności
    result_label = ctk.CTkLabel(
        frame,
        text="",
        font=ctk.CTkFont(size=16),
        text_color="black"
    )
    result_label.pack(pady=10)

    # Przycisk powrotu
    back_button = ctk.CTkButton(
        frame,
        text="Powrót",
        font=ctk.CTkFont(size=16),
        width=150,
        fg_color="#333333",
        command=back_to_payment_screen
    )
    back_button.pack(pady=20)


def card_payment_screen(frame, total_amount, back_to_payment_screen):
    for widget in frame.winfo_children():
        widget.destroy()

    # Tytuł
    title_label = ctk.CTkLabel(
        frame,
        text="Płatność kartą",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)
     # Pozioma kreska
    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    # Wyświetlenie należności
    amount_label = ctk.CTkLabel(
        frame,
        text=f"Należność: {total_amount:.2f} zł",
        font=ctk.CTkFont(size=20),
        text_color="black"
    )
    amount_label.pack(pady=10)

    # Instrukcja obsługi terminala
    instruction_label = ctk.CTkLabel(
        frame,
        text="Postępuj zgodnie z instrukcjami na terminalu",
        font=ctk.CTkFont(size=16),
        text_color="blue"
    )
    instruction_label.pack(pady=10)

    # Symulacja przetwarzania płatności
    processing_label = ctk.CTkLabel(
        frame,
        text="Przetwarzanie płatności...",
        font=ctk.CTkFont(size=16),
        text_color="blue"
    )

    # Funkcja obsługi płatności
    def process_payment():
        processing_label.pack(pady=10)
        frame.after(2000, lambda: success_label.pack(pady=10))  # Symulacja przetwarzania
        frame.after(2000, lambda: processing_label.pack_forget())  # Usunięcie komunikatu "Przetwarzanie"

    # Przycisk rozpoczęcia płatności
    pay_button = ctk.CTkButton(
        frame,
        text="Zapłać",
        font=ctk.CTkFont(size=16),
        width=200,
        command=process_payment
    )
    pay_button.pack(pady=20)

    # Komunikat sukcesu
    success_label = ctk.CTkLabel(
        frame,
        text="Płatność zaakceptowana! Odbierz bilety z drukarki ",
        font=ctk.CTkFont(size=16),
        text_color="green"
    )

    # Przycisk powrotu
    back_button = ctk.CTkButton(
        frame,
        text="Powrót",
        font=ctk.CTkFont(size=16),
        width=150,
        fg_color="#333333",
        command=back_to_payment_screen
    )
    back_button.pack(pady=20)


def payment_screen(frame, back_to_tickets, total_amount):
    for widget in frame.winfo_children():
        widget.destroy()

    # Tytuł ekranu
    title_label = ctk.CTkLabel(
        frame,
        text="Ekran płatności",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)
     # Pozioma kreska
    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    # Wyświetlenie kwoty do zapłaty
    amount_label = ctk.CTkLabel(
        frame,
        text=f"Kwota do zapłaty: {total_amount:.2f} zł",
        font=ctk.CTkFont(size=20),
        text_color="black"
    )
    amount_label.pack(pady=20)

    # Wczytywanie obrazków
    cash_image = ctk.CTkImage(
        light_image=Image.open("kasa.png"),
        dark_image=Image.open("kasa.png"),
        size=(100, 100)
    )
    card_image = ctk.CTkImage(
        light_image=Image.open("karta.png"),
        dark_image=Image.open("karta.png"),
        size=(100, 100)
    )

    # Ramka na opcje płatności
    payment_frame = ctk.CTkFrame(frame, fg_color="transparent")
    payment_frame.pack(pady=50)

    # Płatność gotówką
    cash_payment_button = ctk.CTkButton(
        payment_frame,
        text="Płatność gotówką",
        font=ctk.CTkFont(size=16, weight="bold"),
        width=200,
        height=200,
        corner_radius=10,
        image=cash_image,
        compound="top",
        fg_color="#FFB347",
        hover_color="#FFA07A",
        command=lambda: cash_payment_screen(frame, total_amount, lambda: payment_screen(frame, back_to_tickets, total_amount))
    )
    cash_payment_button.grid(row=0, column=0, padx=50, pady=10)

    # Płatność kartą
    card_payment_button = ctk.CTkButton(
        payment_frame,
        text="Płatność kartą",
        font=ctk.CTkFont(size=16, weight="bold"),
        width=200,
        height=200,
        corner_radius=10,
        image=card_image,
        compound="top",
        fg_color="#87CEEB",
        hover_color="#4682B4",
        command=lambda: card_payment_screen(frame, total_amount, lambda: payment_screen(frame, back_to_tickets, total_amount))
    )
    card_payment_button.grid(row=0, column=1, padx=50, pady=10)

    # Przycisk powrotu do ekranu biletów
    back_button = ctk.CTkButton(
        frame,
        text="Wróć do biletów",
        font=ctk.CTkFont(size=16),
        width=200,
        height=40,
        corner_radius=20,
        fg_color="#333333",
        command=back_to_tickets
    )
    back_button.pack(pady=20)


def periodic_tickets_window(frame, back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()

    # Słownik przechowujący liczbę i kwotę biletów
    selected_tickets = {"Normalny": 0, "Ulgowy": 0, "Suma": 0.0}

    # Funkcja przejścia do ekranu płatności
    def navigate_to_payment():
        payment_screen(frame, lambda: periodic_tickets_window(frame, back_to_menu), selected_tickets["Suma"])

    # Tytuł
    title_label = ctk.CTkLabel(
        frame,
        text="Wybierz rodzaj biletu okresowego",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)

    # Pozioma kreska
    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    # Nowe dane biletów okresowych
    tickets = [
        ("Gdynia - miesięczny zwykły", 103.00, 51.50),
        ("Gdynia - miesięczny pospieszne/nocne", 115.00, 57.50),
        ("Sopot/Rumia - miesięczny", 81.00, 40.50),
        ("Rumia, Reda, Wejherowo - ", 108.00, 54.00),
        ("Sieć komunikacyjna (wszystkie linie)", 126.00, 63.00)
    ]

    # Ramka na przyciski
    button_frame = ctk.CTkFrame(frame, fg_color="transparent")
    button_frame.pack(pady=30)

    # Styl przycisków
    normal_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 280,
        "height": 50,
        "corner_radius": 20,
        "fg_color": "#3b8ed0",
        "hover_color": "#36719f"
    }
    reduced_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 280,
        "height": 50,
        "corner_radius": 20,
        "fg_color": "#CD8200",
        "hover_color": "#FFA100"
    }

    # Kolumny dla biletów normalnych i ulgowych
    normal_column = ctk.CTkFrame(button_frame, fg_color="transparent")
    reduced_column = ctk.CTkFrame(button_frame, fg_color="transparent")

    normal_column.pack(side="left", padx=20)
    reduced_column.pack(side="right", padx=20)

    # Funkcja do obsługi liczby biletów
    def update_ticket_count(ticket_name, ticket_type, price, column, button_style):
        for widget in column.winfo_children():
            widget.destroy()

        count_var = ctk.IntVar(value=0)

        # Licznik biletów
        counter_frame = ctk.CTkFrame(column, fg_color="transparent")
        counter_frame.pack(pady=10)

        def increase_count():
            count_var.set(count_var.get() + 1)
            selected_tickets[ticket_type] += 1
            selected_tickets["Suma"] += price

        def decrease_count():
            if count_var.get() > 0:
                count_var.set(count_var.get() - 1)
                selected_tickets[ticket_type] -= 1
                selected_tickets["Suma"] -= price

        minus_button = ctk.CTkButton(
            counter_frame,
            text="-",
            font=ctk.CTkFont(size=16),
            width=50,
            fg_color=button_style["fg_color"],
            hover_color=button_style["hover_color"],
            command=decrease_count
        )
        minus_button.grid(row=0, column=0, padx=10)

        count_label = ctk.CTkLabel(
            counter_frame,
            textvariable=count_var,
            font=ctk.CTkFont(size=16),
            width=50
        )
        count_label.grid(row=0, column=1, padx=10)

        plus_button = ctk.CTkButton(
            counter_frame,
            text="+",
            font=ctk.CTkFont(size=16),
            width=50,
            fg_color=button_style["fg_color"],
            hover_color=button_style["hover_color"],
            command=increase_count
        )
        plus_button.grid(row=0, column=2, padx=10)

        # Przycisk zatwierdzenia
        confirm_button = ctk.CTkButton(
            column,
            text="Zatwierdź",
            font=ctk.CTkFont(size=16),
            width=200,
            height=40,
            corner_radius=20,
            fg_color=button_style["fg_color"],
            hover_color=button_style["hover_color"],
            command=navigate_to_payment
        )
        confirm_button.pack(pady=20)

    # Dodawanie przycisków do kolumn
    for name, price_normal, price_reduced in tickets:
        normal_button = ctk.CTkButton(
            normal_column,
            text=f"{name}\nNormalny: {price_normal} zł",
            command=lambda n=name, p=price_normal: update_ticket_count(n, "Normalny", p, normal_column, normal_button_style),
            **normal_button_style
        )
        normal_button.pack(pady=10)

        reduced_button = ctk.CTkButton(
            reduced_column,
            text=f"{name}\nUlgowy: {price_reduced} zł",
            command=lambda n=name, p=price_reduced: update_ticket_count(n, "Ulgowy", p, reduced_column, reduced_button_style),
            **reduced_button_style
        )
        reduced_button.pack(pady=10)

    # Przycisk powrotu
    back_button = ctk.CTkButton(
        frame,
        text="Wróć",
        command=back_to_menu,
        font=ctk.CTkFont(size=16),
        width=150,
        height=40,
        corner_radius=20,
        fg_color="#333333"
    )
    back_button.pack(pady=20)




