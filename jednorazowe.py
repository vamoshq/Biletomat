import customtkinter as ctk

# Funkcja obsługi wyboru biletu
def ticket_selected(ticket_name, ticket_type, price):
    print(f"Wybrano bilet: {ticket_name} ({ticket_type}) - {price} zł")
    # Możesz tutaj przejść do kolejnego kroku, np. ekran płatności

# Funkcja dla okna wyboru biletów jednorazowych
def one_time_tickets_window(frame,back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()
    window = frame
   

    # Tytuł
    title_label = ctk.CTkLabel(
        window,
        text="Wybierz rodzaj biletu jednorazowego",
        font=ctk.CTkFont(size=24, weight="bold" ),
        text_color="black"
    )
    title_label.pack(pady=20)

    # Dane biletów
    tickets = [
        ("1-przejazdowy", 4.80, 2.40),
        ("75-minutowy", 6.00, 3.00),
        ("24-godzinny", 22.00, 11.00)
    ]

    # Ramka na przyciski
    button_frame = ctk.CTkFrame(window, fg_color="transparent")
    button_frame.pack(pady=30)

    # Styl przycisków
    normal_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 300,
        "height": 100,
        "corner_radius": 20
    }
    reduced_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 300,
        "height": 100,
        "corner_radius": 20,
        "fg_color": "#CD8200",
        "hover_color": "#FFA100"
    }


    # Kolumny dla biletów normalnych i ulgowych
    normal_column = ctk.CTkFrame(button_frame, fg_color="transparent")
    reduced_column = ctk.CTkFrame(button_frame, fg_color="transparent")

    normal_column.pack(side="left", padx=20)
    reduced_column.pack(side="right", padx=20)

    # Dodawanie przycisków do kolumn
    for name, price_normal, price_reduced in tickets:
        # Przyciski dla biletów normalnych
        normal_button = ctk.CTkButton(
            normal_column,
            text=f"{name}\nNormalny: {price_normal} zł",
            command=lambda n=name, p=price_normal: ticket_selected(n, "Normalny", p),
            **normal_button_style
        )
        normal_button.pack(pady=10)

        # Przyciski dla biletów ulgowych
        reduced_button = ctk.CTkButton(
            reduced_column,
            text=f"{name}\nUlgowy: {price_reduced} zł",
            command=lambda n=name, p=price_reduced: ticket_selected(n, "Ulgowy", p),
            **reduced_button_style
        )
        reduced_button.pack(pady=10)

    # Przycisk powrotu
    

    back_button = ctk.CTkButton(
        window,
        text="Wróć",
        command=back_to_menu,
        font=ctk.CTkFont(size=16),
        width=150,
        height=40,
        corner_radius=20,
    )
    back_button.pack(pady=20)

    # Uruchomienie okna
    window.mainloop()
    if __name__ == "__main__":
        one_time_tickets_window()
