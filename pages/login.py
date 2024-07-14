from utils.ui import font_title, font_text
from utils.ui import Colors

from customtkinter import *
from PIL import Image

class ConnexionBox(CTkFrame):
    def __init__(self, window):
        super().__init__(window, width=341, height=310, fg_color=Colors.TERTIARY)
        self.view()

    def view(self):
        conn_text = CTkLabel(
            self, text="Connexion", font=font_title(28), text_color=Colors.SECONDARY_LIGHT
        )
        email_entry = CTkEntry(
            self,
            placeholder_text="Email",
            fg_color=Colors.TERTIARY,
            corner_radius=5,
            font=font_text(14),
            placeholder_text_color=Colors.SECONDARY_LIGHT,
            border_width=0,
            width=280,
            height=34
        )
        buttom_border_email = CTkFrame(email_entry, border_color=Colors.PRIMARY, height=2, border_width=2, fg_color=Colors.PRIMARY)
        buttom_border_email.place(relwidth=1, rely=0.9)

        password_entry = CTkEntry(
            self,
            placeholder_text="Mot de passe",
            fg_color=Colors.TERTIARY,
            corner_radius=5,
            font=font_text(14),
            placeholder_text_color=Colors.SECONDARY_LIGHT,
            border_width=0,
            width=280,
            height=34
        )
        buttom_border_password = CTkFrame(password_entry, border_color=Colors.PRIMARY, height=2, border_width=2, fg_color=Colors.PRIMARY)
        buttom_border_password.place(relwidth=1, rely=0.9)

        stay_connected = CTkCheckBox(
            self,
            text="Rester connecté",
            corner_radius=3,
            font=font_title(12),
            text_color=Colors.SECONDARY_LIGHT,
            checkbox_width=19,
            checkbox_height=19,
            border_width=2,
            border_color=Colors.LIGHT_GRAY,
            fg_color=Colors.WHITE,
            hover_color=Colors.PRIMARY
        )
        connect_button = CTkButton(
            self,
            text="Se Connecter",
            text_color=Colors.TERTIARY,
            fg_color=Colors.PRIMARY,
            font=font_title(14),
            width=280,
            height=42,
            corner_radius=5
        )

        conn_text.place(relx=0.5, rely=0.05, anchor=CENTER)
        email_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
        password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        stay_connected.place(relx=0.1, rely=0.61)
        connect_button.place(relx=0.5, rely=0.88, anchor=CENTER)



class LoginPage(CTkFrame):
    def __init__(self, window: CTk, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)
        self.window = window

        self.view()

    def view(self):
        logo_text = CTkLabel(
            self, text="SoigneMoi", font=font_title(32), text_color=Colors.PRIMARY
        )
        logo_text.place(relx=0.5, y=80, anchor=CENTER)
        connexion_box = ConnexionBox(self.window)
        connexion_box.place(relx=0.5, rely=0.5, anchor=CENTER)
