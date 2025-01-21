import customtkinter as ctk
import random
import time
import math
from jednorazowe import one_time_tickets_window
from okresowe import periodic_tickets_window
from doladowanie import top_up_card_window
from pomoc import help_window

spin_attempted = False
# Ustawienie trybu (opcjonalnie: "light" lub "dark")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # Możesz zmienić na inny kolor

# Funkcja do zmiany widoku w ramce
def switch_to_view(frame, content_function, back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()
    content_function(frame, back_to_menu)


# Funkcja obsługująca zakładkę Koła Fortuny
def fortune_wheel_window(frame, back_to_menu):
    for widget in frame.winfo_children():
        widget.destroy()

    title_label = ctk.CTkLabel(
        frame,
        text="Koło Fortuny",
        font=ctk.CTkFont(size=24, weight="bold")
    )
    title_label.pack(pady=20)

    result_label = ctk.CTkLabel(
        frame,
        text="Zakręć kołem i sprawdź czy wygrałeś darmowy bilet!",
        font=ctk.CTkFont(size=16)
    )
    result_label.pack(pady=20)

    wheel_canvas = ctk.CTkCanvas(frame, width=200, height=200, bg="white")
    wheel_canvas.pack(pady=20)

    wheel = wheel_canvas.create_oval(30, 30, 170, 170, fill="red")
    winning_segment = wheel_canvas.create_arc(30, 30, 170, 170, start=60, extent=90, fill="green")
    pointer = wheel_canvas.create_polygon(100, 10, 90, 30, 110, 30, fill="black")

    def animate_wheel():
        global spin_attempted
        if spin_attempted:
            result_label.configure(text="Możesz zakręcić kołem tylko raz na sesję!", text_color="red")
            return
        spin_attempted = True
        spins = random.randint(30, 50)
        total_rotation = 0    
        spins = random.randint(30, 50)
        total_rotation = 0

        for _ in range(spins):
            total_rotation = (total_rotation + 15) % 360
            wheel_canvas.delete("all")

            # Rysowanie statycznego koła w tle
            wheel_canvas.create_oval(30, 30, 170, 170, fill="red")
        
            # Zawsze rysujemy wygrywający segment na tej samej pozycji
            wheel_canvas.create_arc(30, 30, 170, 170, start=60, extent=90, fill="green")

            # Obrót wskaźnika wokół koła
            angle_rad = math.radians(total_rotation)
            x = 100 + 70 * math.cos(angle_rad)
            y = 100 + 70 * math.sin(angle_rad)
            wheel_canvas.create_polygon(x, y, x - 10, y - 30, x + 10, y - 30, fill="black")

            frame.update()
            time.sleep(0.05)

        check_result(total_rotation)



    def check_result(rotation_angle):
    # Przesunięcie kąta na koło (stałe zielone pole)
        winning_start = 60
        winning_end = 150

    # Kąt wskaźnika po zakończeniu obrotu (obrót przeciwny do wskazówek zegara)
        pointer_angle = (360 - rotation_angle) % 360

        if winning_start <= pointer_angle <= winning_end:
            result_label.configure(text="Gratulacje! Wygrałeś darmowy bilet!", text_color="green")
        else:
            result_label.configure(text="Niestety, nie udało się. Spróbuj ponownie!", text_color="red")

    
    spin_button = ctk.CTkButton(
        frame,
        text="Zakręć kołem",
        font=ctk.CTkFont(size=16),
        width=300,
        height=60,
        corner_radius=20,
        command=animate_wheel
    )
    spin_button.pack(pady=20)

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

# Tworzenie głównego okna
def main_window():
    root = ctk.CTk()
    root.title("Biletomat ZKM Gdynia")
    root.geometry("800x600")
    root.configure(fg_color="#f0f0f0")

    main_frame = ctk.CTkFrame(root, fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    def show_main_menu():
        for widget in main_frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(
            main_frame,
            text="Witaj w Biletomacie ZKM Gdynia",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)

        separator = ctk.CTkFrame(main_frame, height=2, fg_color="#cccccc")
        separator.pack(fill="x", padx=20, pady=10)

        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=50)

        buttons = [
            ("Kup bilet jednorazowy", lambda: switch_to_view(main_frame, one_time_tickets_window, show_main_menu)),
            ("Kup bilet okresowy", lambda: switch_to_view(main_frame, periodic_tickets_window, show_main_menu)),
            ("Doładuj kartę miejską", lambda: switch_to_view(main_frame, top_up_card_window, show_main_menu)),
            ("Pomoc", lambda: switch_to_view(main_frame, help_window, show_main_menu)),
            ("Koło Fortuny", lambda: switch_to_view(main_frame, fortune_wheel_window, show_main_menu))
        ]

        button_style = {
            "font": ctk.CTkFont(size=16),
            "width": 300,
            "height": 60,
            "corner_radius": 20
        }

        for text, command in buttons:
            button = ctk.CTkButton(button_frame, text=text, command=command, **button_style)
            button.pack(pady=10)

        footer_label = ctk.CTkLabel(
            main_frame, 
            text="Dziękujemy za korzystanie z usług ZKM Gdynia!", 
            font=ctk.CTkFont(size=12)
        )
        footer_label.pack(side="bottom", pady=20)

    show_main_menu()
    root.mainloop()

if __name__ == "__main__":
    main_window()
