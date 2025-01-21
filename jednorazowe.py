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

    # Symulacja przetwarzania płatności
    processing_label = ctk.CTkLabel(
        frame,
        text="Przetwarzanie płatności...",
        font=ctk.CTkFont(size=16),
        text_color="blue"
    )

    # Wynik płatności
    result_label = ctk.CTkLabel(
        frame,
        text="",
        font=ctk.CTkFont(size=16),
        text_color="black"
    )
    result_label.pack(pady=10)

    # Funkcja obsługi wpłaty z latencją
    def handle_payment():
        processing_label.pack(pady=10)  # Wyświetlenie komunikatu o przetwarzaniu
        frame.after(2000, process_payment)  # Opóźnienie o 2 sekundy

    def process_payment():
        processing_label.pack_forget()  # Usunięcie komunikatu "Przetwarzanie"
        paid_amount = paid_amount_var.get()
        if paid_amount >= total_amount:
            change = paid_amount - total_amount
            result_label.configure(text=f"Płatność przyjęta. Reszta: {change:.2f} zł. Odbierz resztę oraz bilety z drukarki", text_color="green")
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

def one_time_tickets_window(frame, back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()

    # Słownik przechowujący liczbę i kwotę biletów
    selected_tickets = {"Normalny": 0, "Ulgowy": 0, "Suma": 0.0}
    
    # Zmienne do przechowywania wyborów
    selected_type = {"type": None}
    selected_zone = {"zone": None}

    def show_zone_selection():
        for widget in frame.winfo_children():
            widget.destroy()

        # Tytuł
        title_label = ctk.CTkLabel(
            frame,
            text="Wybierz strefę biletową",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="black"
        )
        title_label.pack(pady=20)

        # Separator
        separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
        separator.pack(fill="x", padx=20, pady=10)

        # Ramka na przyciski stref
        zone_frame = ctk.CTkFrame(frame, fg_color="transparent")
        zone_frame.pack(pady=30)

        def select_zone(zone):
            selected_zone["zone"] = zone
            show_tickets(selected_type["type"], zone)

        # Przycisk dla Gdyni
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

        # Przycisk dla Metropolitan
        metro_button = ctk.CTkButton(
            zone_frame,
            text="Metropolitalny",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=250,
            height=100,
            corner_radius=20,
            fg_color="#3b8ed0",
            hover_color="#36719f",
            command=lambda: select_zone("Metro")
        )
        metro_button.pack(pady=20)

        # Przycisk powrotu
        back_button = ctk.CTkButton(
            frame,
            text="Wróć",
            font=ctk.CTkFont(size=16),
            width=150,
            height=40,
            corner_radius=20,
            fg_color="#333333",
            command=lambda: one_time_tickets_window(frame, back_to_menu)
        )
        back_button.pack(pady=20)

    def show_tickets(ticket_type, zone):
        for widget in frame.winfo_children():
            widget.destroy()

        # Funkcja przejścia do ekranu płatności
        def navigate_to_payment():
            payment_screen(frame, lambda: one_time_tickets_window(frame, back_to_menu), selected_tickets["Suma"])

        # Tytuł
        title_label = ctk.CTkLabel(
            frame,
            text=f"Bilety {ticket_type} - Strefa {zone}",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="black"
        )
        title_label.pack(pady=20)

        # Separator
        separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
        separator.pack(fill="x", padx=20, pady=10)

        # Ceny biletów zależne od strefy
        tickets = {
            "Gdynia": {
                "short_term": [
                    ("1-przejazdowy", 4.80, 2.40),
                    ("75-minutowy", 6.00, 3.00),
                ],
                "long_term": [
                    ("24-godzinny", 22.00, 11.00),
                ]
            },
            "Metro": {
                "short_term": [
                    ("1-przejazdowy", 5.20, 2.60),
                    ("75-minutowy", 6.00, 3.00),
                ],
                "long_term": [
                    ("24-godzinny-komunalny", 24.00, 12.00),
                    ("24-godzinny-kolejowo-komunalny 2", 30.00, 15.00),
                    ("24-godzinny-kolejowo-komunalny wszyscy", 34.00, 17.00),
                    ("72-godzinny-komunalny", 48.00, 24.00),
                    ("72-godzinny-kolejowo-komunalny", 68.00, 34.00),
                ]
            }
        }

        main_container=ctk.CTkScrollableFrame(
            frame,
            width=800,  # Zwiększona szerokość dla dwóch kolumn
            height=400,
            fg_color="transparent"
        )
        main_container.pack(pady=20, padx=20, fill="both", expand=True)

        columns_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        columns_frame.pack(expand=True, fill="both")

        left_column = ctk.CTkFrame(columns_frame, fg_color="transparent")
        left_column.grid(row=0, column=0, padx=10)
    
    # Etykieta dla lewej kolumny
        left_label = ctk.CTkLabel(
            left_column,
            text="Bilety krótkoterminowe",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="black"
        )
        left_label.pack(pady=(0, 10))

        right_column = ctk.CTkFrame(columns_frame, fg_color="transparent")
        right_column.grid(row=0, column=1, padx=10)
    
    # Etykieta dla prawej kolumny
        right_label = ctk.CTkLabel(
            right_column,
            text="Bilety długoterminowe",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="black"
        )
        right_label.pack(pady=(0, 10))

        counter_container = ctk.CTkFrame(frame, fg_color="transparent")
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
            # Licznik biletów
            counter_frame = ctk.CTkFrame(counter_container, fg_color="transparent")
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

            
            # Przycisk zatwierdzenia
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

        # Wyświetlanie przycisków biletów
        
        button_width=350
        

        for name, price_normal, price_reduced in tickets[zone]["short_term"]:
            price = price_normal if ticket_type == "Normalny" else price_reduced
            
            display_name = f"{name}\nCena: {price} zł" if len(name) <= 20 else f"{name}\nCena: {price} zł"
            ticket_button = ctk.CTkButton(
                left_column,
                text=display_name,
                font=ctk.CTkFont(size=16),
                width=button_width,
                height=60,
                corner_radius=20,
                fg_color="#3b8ed0" if ticket_type == "Normalny" else "#CD8200",
                hover_color="#36719f" if ticket_type == "Normalny" else "#FFA100",
                command=lambda n=name, p=price: update_ticket_count(n, p)
            )
            ticket_button.pack(pady=10)
        for name, price_normal, price_reduced in tickets[zone]["long_term"]:
            price = price_normal if ticket_type == "Normalny" else price_reduced
            
    
            display_name = f"{name}\nCena: {price} zł" if len(name) <= 20 else f"{name}\nCena: {price} zł"

            ticket_button = ctk.CTkButton(
                right_column,
                text=display_name,
                font=ctk.CTkFont(size=16),
                width=button_width,
                height=55,
                corner_radius=20,
                fg_color="#3b8ed0" if ticket_type == "Normalny" else "#CD8200",
                hover_color="#36719f" if ticket_type == "Normalny" else "#FFA100",
                command=lambda n=name, p=price: update_ticket_count(n, p)
            )
            ticket_button.pack(pady=10, padx=10)
        # Przycisk powrotu
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

    # Separator
    separator = ctk.CTkFrame(frame, height=2, fg_color="#cccccc")
    separator.pack(fill="x", padx=20, pady=10)

    # Ramka na przyciski wyboru typu
    type_frame = ctk.CTkFrame(frame, fg_color="transparent")
    type_frame.pack(pady=30)

    def select_ticket_type(ticket_type):
        selected_type["type"] = ticket_type
        show_zone_selection()

    # Przycisk dla biletu normalnego
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

    # Przycisk dla biletu ulgowego
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

    # Przycisk powrotu do menu głównego
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



