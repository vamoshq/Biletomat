def payment_screen(frame, back_to_menu, total_amount):
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

    # Ramka na opcje płatności
    payment_frame = ctk.CTkFrame(frame, fg_color="transparent")
    payment_frame.pack(pady=50, fill="x")

    # Przyciski płatności
    def on_cash_payment():
        print("Wybrano płatność gotówką.")

    def on_card_payment():
        print("Wybrano płatność kartą.")

    # Płatność gotówką
    cash_payment_button = ctk.CTkButton(
        payment_frame,
        text="Płatność gotówką",
        font=ctk.CTkFont(size=16, weight="bold"),
        width=200,
        height=200,
        corner_radius=10,
        image=ctk.CTkImage(file="path_to_cash_image.png", size=(100, 100)),  # Zamień "path_to_cash_image.png" na ścieżkę do obrazka banknotu
        compound="top",
        fg_color="#FFB347",
        hover_color="#FFA07A",
        command=on_cash_payment
    )
    cash_payment_button.grid(row=0, column=0, padx=20, pady=10)

    # Płatność kartą
    card_payment_button = ctk.CTkButton(
        payment_frame,
        text="Płatność kartą",
        font=ctk.CTkFont(size=16, weight="bold"),
        width=200,
        height=200,
        corner_radius=10,
        image=ctk.CTkImage(file="path_to_card_image.png", size=(100, 100)),  # Zamień "path_to_card_image.png" na ścieżkę do obrazka karty kredytowej
        compound="top",
        fg_color="#87CEEB",
        hover_color="#4682B4",
        command=on_card_payment
    )
    card_payment_button.grid(row=0, column=1, padx=20, pady=10)

    # Przycisk powrotu do menu głównego
    back_button = ctk.CTkButton(
        frame,
        text="Wróć do menu",
        font=ctk.CTkFont(size=16),
        width=200,
        height=40,
        corner_radius=20,
        command=back_to_menu
    )
    back_button.pack(pady=20)

