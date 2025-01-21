import customtkinter as ctk
from PIL import Image
from tkinter import messagebox


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

    selected_tickets = {"Normalny": 0, "Ulgowy": 0, "Suma": 0.0}
    selected_type = {"type": None}
    selected_zone = {"zone": None}
    selected_period = {"period": None}
    prices = {
        "Gdynia": {
            "monthly":{ 
                "Imienny": [
                ("Imienny-Gdynia linie zwykłe/nocne", 103.00, 51.50),
                ("Imienny-Gdynia pospieszne ", 115.00, 57.50),
                ("Imienny-Sopot/Rumia", 81.00, 40.50),
                ("Imienny-Rumia,Reda,Wejherowo", 108.00, 54.00)
                ],
                "Na okaziciela":[
                ("Okaziciel-Gdynia linie zwykłe/nocne", 103.00, 51.50),
                ("Okaziciel-Gdynia linie pospieszne", 115.00, 57.50),
                ("Okaziciel-Sopot/Rumia", 81.00, 40.50),
                ("Okaziciel-Rumia,Reda,Wejherowo", 108.00, 54.00)
                ],
            },
            "semestral": {
                "4-miesięczny" :[
                ("4msc Gdynia linie zwykłe/nocne", None, 194.00),
                ("4msc Gdynia linie pospieszne", None, 217.00),
                ("4msc-Sopot/Rumia", None, 152.00),
                ("4msc-Rumia,Reda,Wejherowo", None, 205.00)
                ],
                "5-miesięczny":[
                ("5msc-Gdynia linie zwykłe/nocne", None, 242.00),
                ("5msc Gdynia linie pospieszne", None, 271.00),
                ("5msc Sopot/Rumia)", None, 190.00),
                ("5msc Rumia,Reda,Wejherowo", None, 257.00)
                ],
            },
        },
        "Metropolitalny": {
            "monthly": [
                ("Komunalny", 156.00, 78.00),
                ("Miesięczny-Gdańsk-Sopot albo Gdynia-Sopot", 80.00, 40.00),
                ("Miesięczny-sieciowy", 86.00, 43.00),
                ("Miesięczny-cały obszar MZKZG", 106.00, 53.00)
                ],
            "semestral": []
        }
    }
    

    def navigate_to_payment():
        payment_screen(frame, lambda: periodic_tickets_window(frame, back_to_menu), selected_tickets["Suma"])

    def show_period_selection():
        for widget in frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(
            frame,
            text="Wybierz rodzaj biletu",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="black"
        )
        title_label.pack(pady=20)

        period_frame = ctk.CTkFrame(frame, fg_color="transparent")
        period_frame.pack(pady=30)

        def select_period(period):
            selected_period["period"] = period
            show_zone_selection()

        monthly_button = ctk.CTkButton(
            period_frame,
            text="Bilet miesięczny",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=250,
            height=100,
            corner_radius=20,
            fg_color="#3b8ed0",
            hover_color="#36719f",
            command=lambda: select_period("monthly")
        )
        monthly_button.pack(pady=20)

        semestral_button = ctk.CTkButton(
            period_frame,
            text="Bilet semestralny",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=250,
            height=100,
            corner_radius=20,
            fg_color="#CD8200",
            hover_color="#FFA100",
            command=lambda: select_period("semestral")
        )
        semestral_button.pack(pady=20)

        back_button = ctk.CTkButton(
            frame,
            text="Wróć",
            font=ctk.CTkFont(size=16),
            width=150,
            height=40,
            corner_radius=20,
            fg_color="#333333",
            command=lambda: periodic_tickets_window(frame, back_to_menu)
        )
        back_button.pack(pady=20)

    def show_zone_selection():
        for widget in frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(
            frame,
            text="Wybierz strefę biletową",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="black"
        )
        title_label.pack(pady=20)

        zone_frame = ctk.CTkFrame(frame, fg_color="transparent")
        zone_frame.pack(pady=30)

        def select_zone(zone):
            selected_zone["zone"] = zone
            show_tickets(selected_zone["zone"], selected_type["type"], selected_period["period"])

        gdynia_button = ctk.CTkButton(
            zone_frame,
            text="Gdynia",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=250,
            height=100,
            corner_radius=20,
            fg_color="#3b8ed0",
            hover_color="#36719f",
            command=lambda: select_zone("Gdynia")
        )
        gdynia_button.pack(pady=20)

        metro_button = ctk.CTkButton(
            zone_frame,
            text="Metropolitalny",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=250,
            height=100,
            corner_radius=20,
            fg_color="#3b8ed0",
            hover_color="#36719f",
            command=lambda: select_zone("Metropolitalny")
        )
        metro_button.pack(pady=20)

        back_button = ctk.CTkButton(
            frame,
            text="Wróć",
            font=ctk.CTkFont(size=16),
            width=150,
            height=40,
            corner_radius=20,
            fg_color="#333333",
            command=lambda: show_period_selection()
        )
        back_button.pack(pady=20)

    def show_tickets(zone, ticket_type, period):
        for widget in frame.winfo_children():
            widget.destroy()

        if zone == "Metropolitalny" and period == "semestral":
            messagebox.showerror("Błąd", "Brak możliwości zakupu biletów semestralnych w strefie Metropolitalnej")
            show_zone_selection()
            return

        title_label = ctk.CTkLabel(
            frame,
            text=f"Bilety {ticket_type} - Strefa {zone}",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="black"
        )
        title_label.pack(pady=20)

        separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
        separator.pack(fill="x", padx=20, pady=10)

        main_container = ctk.CTkScrollableFrame(
            frame,
            width=800,
            height=400,
            fg_color="transparent"
        )
        main_container.pack(pady=20, padx=20, fill="both", expand=True)

        columns_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        columns_frame.pack(expand=True, fill="both")

        left_column = ctk.CTkFrame(columns_frame, fg_color="transparent",width=380)
        left_column.grid(row=0, column=0, padx=5)
        if zone == "Gdynia":
            left_label_text = "Imienny" if period == "monthly" else "4-miesięczny"
            right_label_text = "Na okaziciela" if period == "monthly" else "5-miesięczny"
        else:
            left_label_text = "Bilety miesięczne"
            right_label_text = ""

        left_label = ctk.CTkLabel(
            left_column,
            text=left_label_text,
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="black"
        )
        left_label.pack(pady=(0, 10))

        right_column = ctk.CTkFrame(columns_frame, fg_color="transparent",width=380)
        right_column.grid(row=0, column=1, padx=5)

        right_label = ctk.CTkLabel(
            right_column,
            text=right_label_text,
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="black"
        )
        right_label.pack(pady=(0, 10))

        counter_container = ctk.CTkFrame(frame, fg_color="transparent",height=30)
        counter_container.place(relx=0.2, rely=0.9, anchor="center")

        def update_ticket_count(name, price):
            for widget in counter_container.winfo_children():
                widget.destroy()

            count_var = ctk.IntVar(value=0)
            selection_label = ctk.CTkLabel(
                counter_container,
                text="Wybierz liczbę biletów",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="black"
            )
            selection_label.pack(pady=(10, 5))

            counter_frame = ctk.CTkFrame(counter_container, fg_color="transparent")
            counter_frame.pack(pady=10)

            def increase_count():
                if count_var.get() < 1:
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
                fg_color="#3b8ed0",
                hover_color="#36719f",
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
                fg_color="#3b8ed0",
                hover_color="#36719f",
                command=increase_count
            )
            plus_button.grid(row=0, column=2, padx=10)

            confirm_button = ctk.CTkButton(
                counter_container,
                text="Zatwierdź",
                font=ctk.CTkFont(size=16),
                width=200,
                height=20,
                corner_radius=20,
                fg_color="#3b8ed0",
                hover_color="#36719f",
                command=navigate_to_payment
            )
            confirm_button.pack(pady=20)

        button_width = 350

        # Wyświetlanie biletów miesięcznych
        ticket_list = prices[zone][period]
        for category, tickets in ticket_list.items() if isinstance(ticket_list, dict) else [(None, ticket_list)]:
            column = left_column if category in ["Imienny", "4-miesięczny"] else right_column
            for ticket_name, normal_price, ulgowy_price in tickets:
                price = normal_price if ticket_type == "Normalny" else ulgowy_price
                if price:
                    display_name = f"{ticket_name}\nCena: {price} zł"
                    ticket_button = ctk.CTkButton(
                        column,
                        text=display_name,
                        font=ctk.CTkFont(size=16),
                        width=350,
                        height=60,
                        corner_radius=20,
                        fg_color="#3b8ed0" if ticket_type == "Normalny" else "#CD8200",
                        hover_color="#36719f" if ticket_type == "Normalny" else "#FFA100",
                        command=lambda n=ticket_name, p=price: update_ticket_count(n, p)
                    )
                    ticket_button.pack(pady=10)
        back_button = ctk.CTkButton(
            frame,
            text="Wróć",
            font=ctk.CTkFont(size=16),
            width=150,
            height=60,
            corner_radius=20,
            fg_color="#333333",
            command=lambda: show_zone_selection()
         )
        back_button.pack(side="bottom",pady=10)
    # Początkowy wybór typu biletu
    title_label = ctk.CTkLabel(
        frame,
        text="Wybierz rodzaj biletu",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)

    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    type_frame = ctk.CTkFrame(frame, fg_color="transparent")
    type_frame.pack(pady=30)

    def select_ticket_type(ticket_type):
        selected_type["type"] = ticket_type
        show_zone_selection()
        show_period_selection()

    normal_button = ctk.CTkButton(
        type_frame,
        text="Normalny",
        font=ctk.CTkFont(size=20, weight="bold"),
        width=250,
        height=100,
        corner_radius=20,
        fg_color="#3b8ed0",
        hover_color="#36719f",
        command=lambda: select_ticket_type("Normalny")
    )
    normal_button.pack(pady=20)

    reduced_button = ctk.CTkButton(
        type_frame,
        text="Ulgowy",
        font=ctk.CTkFont(size=20, weight="bold"),
        width=250,
        height=100,
        corner_radius=20,
        fg_color="#CD8200",
        hover_color="#FFA100",
        command=lambda: select_ticket_type("Ulgowy")
    )
    reduced_button.pack(pady=20)

    back_button = ctk.CTkButton(
        frame,
        text="Wróć",
        font=ctk.CTkFont(size=16),
        width=150,
        height=40,
        corner_radius=20,
        fg_color="#333333",
        command=back_to_menu
    )
    back_button.pack(pady=20)