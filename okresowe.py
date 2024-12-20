import customtkinter as ctk

# Funkcja obsługi wyboru biletu
def ticket_selected(ticket_name, ticket_type, price):
    print(f"Wybrano bilet: {ticket_name} ({ticket_type}) - {price} zł")
    # Możesz tutaj przejść do kolejnego kroku, np. ekran płatności

# Funkcja dla okna wyboru biletów okresowych
def periodic_tickets_window(frame,back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()
    window = frame
   

    # Tytuł
    title_label = ctk.CTkLabel(
        window,
        text="Wybierz rodzaj biletu okresowego",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)

    # Dane biletów okresowych
    tickets = [
        ("Miesięczny Gdynia", 90.00, 45.00),
        ("Miesięczny Metropolitalny", 150.00, 75.00),
        ("Semestralny Gdynia", 450.00, 225.00),
        ("Semestralny Metropolitalny", 750.00, 375.00)
    ]

    # Ramka na przyciski
    button_frame = ctk.CTkFrame(window, fg_color="transparent")
    button_frame.pack(pady=30)

    # Styl przycisków
    normal_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 300,
        "height": 60,
        "corner_radius": 20,
        
    }
    reduced_button_style = {
        "font": ctk.CTkFont(size=14),
        "width": 300,
        "height": 60,
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
 # Dodanie legendy
    legend_frame = ctk.CTkFrame(window, fg_color="transparent")
    legend_frame.pack(pady=10)

    legend_label = ctk.CTkLabel(
        legend_frame,
        text=(
            "Legenda:\n"
            "- Metropolitalny: Gdynia, Sopot, Gdańsk.\n"
            "- Semestralny: Ważny przez 5 miesięcy."
        ),
        font=ctk.CTkFont(size=10),
        text_color="#333333",  # Stonowany kolor tekstu
        justify="center"
    )
    legend_label.pack()
    # Uruchomienie okna
    window.mainloop()
    if __name__ == "__main__":
        periodic_tickets_window()

