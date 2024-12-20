import customtkinter as ctk
from jednorazowe import one_time_tickets_window
from okresowe import periodic_tickets_window
from doladowanie import top_up_card_window
from pomoc import help_window

# Ustawienie trybu (opcjonalnie: "light" lub "dark")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # Możesz zmienić na inny kolor

# Funkcja do zmiany widoku w ramce
def switch_to_view(frame, content_function, back_to_menu):
    # Usuwamy wszystkie widżety z obecnego widoku
    for widget in frame.winfo_children():
        widget.destroy()

    # Wywołujemy odpowiednią funkcję, przekazując istniejącą ramkę
    content_function(frame,back_to_menu)

# Tworzenie głównego okna
def main_window():
    root = ctk.CTk()
    root.title("Biletomat ZKM Gdynia")
    root.geometry("800x600")
    root.configure(fg_color="#f0f0f0")

    # Główna ramka, w której zmieniamy widok
    main_frame = ctk.CTkFrame(root, fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    # Funkcja wyświetlająca ekran główny w ramce
    def show_main_menu():
        # Usuwamy wszystko z ramki
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Tytuł
        title_label = ctk.CTkLabel(
            main_frame,
            text="Witaj w Biletomacie ZKM Gdynia",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)

        # Ramka na przyciski
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")  # Ustawienie przezroczystości
        button_frame.pack(pady=50)

        # Przyciski
        buttons = [
            ("Kup bilet jednorazowy", lambda: switch_to_view(main_frame, one_time_tickets_window,show_main_menu)),
            ("Kup bilet okresowy", lambda: switch_to_view(main_frame, periodic_tickets_window,show_main_menu)),
            ("Doładuj kartę miejską", lambda: switch_to_view(main_frame, top_up_card_window,show_main_menu)),
            ("Pomoc", lambda: switch_to_view(main_frame, help_window,show_main_menu))
        ]

        # Styl przycisków
        button_style = {
            "font": ctk.CTkFont(size=16),
            "width": 300,
            "height": 60,
            "corner_radius": 20  # Ustawienie zaokrąglenia rogów
        }

        for text, command in buttons:
            button = ctk.CTkButton(button_frame, text=text, command=command, **button_style)
            button.pack(pady=10)

        # Stopka
        footer_label = ctk.CTkLabel(
            main_frame, 
            text="Dziękujemy za korzystanie z usług ZKM Gdynia!", 
            font=ctk.CTkFont(size=12)
        )
        footer_label.pack(side="bottom", pady=20)

    # Powiązanie funkcji powrotu w każdej zakładce
    def back_to_main_menu():
        show_main_menu()

    one_time_tickets_window.back_to_menu = back_to_main_menu
    periodic_tickets_window.back_to_menu = back_to_main_menu
    top_up_card_window.back_to_menu = back_to_main_menu
    help_window.back_to_menu = back_to_main_menu

    # Wyświetlenie menu głównego na start
    show_main_menu()

    # Uruchomienie głównej pętli okna
    root.mainloop()

# Start aplikacji
if __name__ == "__main__":
    main_window()
