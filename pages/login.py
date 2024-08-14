from pages.home import HomePage
from utils.ui import font_title, font_text
from utils.ui import Colors, focus_event
from utils.auth import login_verif, update_token

from customtkinter import *
from PIL import Image

class ConnexionBox(CTkFrame):
    def __init__(self, window, master : CTkFrame):
        super().__init__(master=master, width=341, height=310, fg_color=Colors.TERTIARY)
        self.window = window
        self.view()

    def view(self):
        conn_text = CTkLabel(
            self, text="Connexion", font=font_title(28), text_color=Colors.SECONDARY_LIGHT
        )
        self.email_entry = CTkEntry(
            self,
            placeholder_text="Email",
            fg_color=Colors.TERTIARY,
            corner_radius=5,
            font=font_text(14),
            placeholder_text_color=Colors.SECONDARY_LIGHT,
            text_color=Colors.SECONDARY,
            border_width=0,
            width=280,
            height=34
        )
        buttom_border_email = CTkFrame(self.email_entry, border_color=Colors.PRIMARY, height=2, border_width=2, fg_color=Colors.PRIMARY)
        buttom_border_email.place(relwidth=1, rely=0.9)

        self.password_entry = CTkEntry(
            self,
            placeholder_text="Mot de passe",
            fg_color=Colors.TERTIARY,
            text_color=Colors.SECONDARY,
            corner_radius=5,
            font=font_text(14),
            placeholder_text_color=Colors.SECONDARY_LIGHT,
            border_width=0,
            width=280,
            height=34,
            show="*"
        )
        buttom_border_password = CTkFrame(self.password_entry, border_color=Colors.PRIMARY, height=2, border_width=2, fg_color=Colors.PRIMARY)
        buttom_border_password.place(relwidth=1, rely=0.9)

        self.stay_connected = CTkCheckBox(
            self,
            text="Rester connecté",
            corner_radius=3,
            font=font_title(12),
            text_color=Colors.SECONDARY_LIGHT,
            checkbox_width=16,
            checkbox_height=16,
            border_width=2,
            border_color=Colors.SECONDARY_LIGHT,
            fg_color=Colors.PRIMARY,
            hover_color=Colors.PRIMARY_HOVER
        )
        connect_button = CTkButton(
            self,
            text="Se Connecter",
            text_color=Colors.TERTIARY,
            fg_color=Colors.PRIMARY,
            font=font_title(14),
            width=280,
            height=42,
            corner_radius=5,
            command=self.handle_login
        )

        self.error_label = None

        conn_text.place(relx=0.5, rely=0.05, anchor=CENTER)
        self.email_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.stay_connected.place(relx=0.1, rely=0.61)
        connect_button.place(relx=0.5, rely=0.88, anchor=CENTER)
    
    def handle_login(self):
        self.entered_password = self.password_entry.get()
        self.entered_email = self.email_entry.get()

        request_info = login_verif(
            email=self.entered_email, 
            password=self.entered_password
        )
        token = request_info["token"]

        if token:
            if self.stay_connected.get():
                update_token(token)

            HomePage(
                window=self.window,
                token=token,
                past_page=self.master
            )

        else:
            error_text = request_info["error_text"]
            print(error_text)
            if isinstance(error_text, list):

                error_text = error_text[0]

            if self.error_label:
                self.error_label.destroy()

            self.error_label = CTkLabel(self, font=font_text(14), text_color=Colors.RED, text=error_text)

            self.error_label.place(relx=0.5, rely=0.2, anchor=CENTER)



class LoginPage(CTkFrame):
    def __init__(self, window: CTk, past_page: CTkFrame = None) -> None:
        if past_page:
            past_page.destroy()

        super().__init__(window, corner_radius=0, fg_color=Colors.TERTIARY)
        self.pack(fill="both", expand=True)
        self.window = window

        self.view()
        focus_event(self.window)

    def view(self):
        logo_text = CTkLabel(
            self, text="SoigneMoi", font=font_title(32), text_color=Colors.PRIMARY
        )
        self.connexion_box = ConnexionBox(self.window, self)

        deco_up = CTkLabel(
            self, 
            text="", 
            image=CTkImage(light_image=Image.open("assets/images/Deco up.png"), size=(600, 400)),
        )
        deco_down = CTkLabel(
            self,
            text="",
            image=CTkImage(light_image=Image.open("assets/images/Deco down.png"), size=(600, 400))
        )
        logo_text.lift(deco_up)
        self.connexion_box.lift(deco_up)
        self.connexion_box.lift(deco_down)

        logo_text.place(relx=0.5, y=80, anchor=CENTER)
        self.connexion_box.place(relx=0.5, rely=0.5, anchor=CENTER)
        deco_up.place(relx=-0.05, rely=-0.05)
        deco_down.place(relx=0.55, rely=0.48)

