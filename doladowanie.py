import customtkinter as ctk
from tkinter import messagebox
# Funkcja obsługi doładowania karty
def top_up_card(card_number, amount):
    print(f"Doładowano kartę nr: {card_number} kwotą: {amount} zł")
    # Możesz dodać funkcję zapisującą do bazy danych lub przechodzącą do potwierdzenia

# Funkcja dla ekranu doładowania karty miejskiej
def top_up_card_window(frame,back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()
    window = frame
    

    # Tytuł
    title_label = ctk.CTkLabel(
        window,
        text="Doładowanie Karty Miejskiej",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color="black"
    )
    title_label.pack(pady=20)

    # Instrukcja do przyłożenia karty
    instruction_label = ctk.CTkLabel(
        window,
        text="Proszę przyłożyć kartę do czytnika.",
        font=ctk.CTkFont(size=16),
        text_color="#333333"
    )
    instruction_label.pack(pady=10)

    # Pole do wyświetlenia numeru karty po jej przyłożeniu
    card_number_var = ctk.StringVar()
    card_number_var.set("")

    card_number_label = ctk.CTkLabel(
        window,
        textvariable=card_number_var,
        font=ctk.CTkFont(size=16, weight="bold"),
        text_color="#007BFF"
    )
    card_number_label.pack(pady=10)

    # Pole do wpisania kwoty doładowania
    amount_label = ctk.CTkLabel(
        window,
        text="Kwota doładowania (zł):",
        font=ctk.CTkFont(size=14),
        text_color="black"
    )
    amount_label.pack(pady=10)

    amount_entry = ctk.CTkEntry(
        window,
        placeholder_text="Wpisz kwotę",
        font=ctk.CTkFont(size=14),
        width=300
    )
    amount_entry.pack(pady=10)

    # Przycisk doładowania
    def handle_top_up():
        card_number = card_number_var.get()
        amount = amount_entry.get()
        if card_number and amount:
            try:
                amount = float(amount)
                if amount > 0:
                    top_up_card(card_number, amount)
                    messagebox.showinfo("Sukces", f"Karta nr {card_number} została doładowana o {amount} zł.")
                else:
                    messagebox.showwarning("Błąd", "Kwota musi być większa niż 0 zł.")
            except ValueError:
                messagebox.showerror("Błąd", "Wprowadź poprawną kwotę.")
        else:
            messagebox.showerror("Błąd", "Uzupełnij wszystkie pola.")

    top_up_button = ctk.CTkButton(
        window,
        text="Doładuj",
        command=handle_top_up,
        font=ctk.CTkFont(size=16),
        width=150,
        height=40,
        corner_radius=15,
    )
    top_up_button.pack(pady=20)

    # Symulacja przyłożenia karty
    def simulate_card_reading():
        card_number_var.set("123456789")  # Wczytany numer karty (symulacja)
        instruction_label.configure(text="Karta została odczytana. Wprowadź kwotę doładowania.")

    simulate_card_button = ctk.CTkButton(
        window,
        text="Symuluj przyłożenie karty",
        command=simulate_card_reading,
        font=ctk.CTkFont(size=14),
        width=200,
        height=40,
        corner_radius=15
    )
    simulate_card_button.pack(pady=10)

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
    back_button.pack(pady=10)

    # Uruchomienie okna
    window.mainloop()

# Uruchomienie okna doładowania karty
if __name__ == "__main__":
    top_up_card_window()

