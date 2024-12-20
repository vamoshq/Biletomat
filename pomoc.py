import customtkinter as ctk

# Funkcja dla ekranu Pomoc
def help_window(frame,back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()
    window = frame
    

    # Tytuł
    title_label = ctk.CTkLabel(
        window,
        text="Pomoc i Wskazówki",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color="black"
    )

    # Lista podpunktów z pomocnymi informacjami
    help_items = [
        {
            "title": "Zakup biletów jednorazowych:",
            "content": "Wybierz odpowiedni rodzaj biletu (normalny/ulgowy).\n"
                       "Postępuj zgodnie z instrukcjami na ekranie."
        },
        {
            "title": "Zakup biletów okresowych:",
            "content": "Wybierz miesięczny lub semestralny bilet.\n"
                       "Określ taryfę (Gdynia lub Metropolitalny)."
        },
        {
            "title": "Doładowanie karty miejskiej:",
            "content": "Przyłóż kartę do czytnika, aby ją zidentyfikować.\n"
                       "Wprowadź kwotę doładowania i potwierdź."
        },
        {
            "title": "Metody płatności:",
            "content": "Płatność gotówką, kartą płatniczą lub zbliżeniowo.\n"
                       "Postępuj zgodnie z instrukcjami na ekranie płatności."
        },
        {
            "title": "W razie problemów:",
            "content": "Sprawdź komunikaty błędów na ekranie.\n"
                       "Skontaktuj się z obsługą klienta ZKM Gdynia pod numerem: 123-456-789.\n"
                       "E-mail: pomoc@zkm.gdynia.pl."
        }
    ]

    # Tworzenie ramek dla każdego podpunktu
    for item in help_items:
        frame = ctk.CTkFrame(window, fg_color="#ffffff", corner_radius=10)
        frame.pack(pady=5, padx=20, fill="x", expand=False)

        title_label = ctk.CTkLabel(
            frame,
            text=item["title"],
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#007BFF",
            anchor="w"
        )
        title_label.pack(pady=(10, 0), padx=10, anchor="w")

        content_label = ctk.CTkLabel(
            frame,
            text=item["content"],
            font=ctk.CTkFont(size=14),
            text_color="#333333",
            justify="left",
            wraplength=700
        )
        content_label.pack(pady=10, padx=10, anchor="w")

    # Przycisk powrotu
   

    back_button = ctk.CTkButton(
        window,
        text="Wróć",
        command=back_to_menu,
        font=ctk.CTkFont(size=16),
        width=100,
        height=40,
        corner_radius=15,
    )
    back_button.pack(pady=20)

    # Uruchomienie okna
    window.mainloop()

    if __name__ == "__main__":
        help_window()

