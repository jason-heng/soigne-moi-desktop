from pages import home

from customtkinter import CTkFont, CTkFrame, RIGHT, CTkLabel, CENTER, CTkImage, CTkButton, CTk
from PIL import Image

class Colors:
    PRIMARY = "#2563EB"
    PRIMARY_HOVER = "#063A9B"
    OLD_PRIMARY = "#25567f"

    SECONDARY = "#2D2D2A"
    SECONDARY_LIGHT = "#4F4F49"

    TERTIARY = "#FFFDFD"
    TERTIARY_LIGHT = "#F9F7F3"

    WHITE = "#FFFFFF"
    LIGHT_GRAY = "#E5E7EB"
    SILVER_LIGHT = "#b5b5b5"

    RED = "#b51d18"
    SILVER = "#878686"

def font_title(size: int) -> CTkFont:
    return CTkFont(family="Helvetica", size=size, weight="bold")

def font_text(size: int) -> CTkFont:
    return CTkFont(family="Roboto", size=size)

def focus_event(widget):
    for sub_widget in widget.winfo_children():
        sub_widget.bind("<ButtonPress>", lambda _:widget.focus())
        if widget.winfo_children():
            focus_event(sub_widget)

def clear(frame) -> None:
    for widget in frame.winfo_children():
        widget.destroy()


def center(w, h, frame) -> None:
    ws = frame.winfo_screenwidth()
    hs = frame.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    frame.geometry(f"{w}x{h}+{x}+{y}")
    clear(frame)

def change_button_text_color(widget_str: str, button_paths : dict, color):
    for button_str in list(button_paths):
        if widget_str.startswith(button_str):
            widget_str = button_str
    button_paths[widget_str].configure(text_color=color)


def place_loading_frame(page_content : CTkFrame):
    clear(page_content)

    logo_image = CTkImage(light_image=Image.open("assets/images/logo.png"), size=(47, 40))
    logo_label = CTkLabel(page_content, image=logo_image, text=None)

    loading_label = CTkLabel(
        page_content, 
        text="Chargement...", 
        text_color=Colors.PRIMARY, 
        font=font_title(32),
    )
    loading_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    logo_label.place(relx=0.3, rely=0.502, anchor=CENTER)



def place_page_top(title: str, page_content: CTkFrame, disconnect, handle_place_homepage, place_home_button):

    title = title if len(title) <=32 else f"{title[:29]}..."

    title_label = CTkLabel(page_content, text=title, font=font_title(22), text_color=Colors.SECONDARY)
    title_label.place(x=(100 if place_home_button else 5), y=40)

    home_button = CTkButton(
        page_content,
        width=85,
        height=30,
        fg_color=Colors.WHITE,
        text="Acceuil",
        font=font_title(16),
        text_color=Colors.PRIMARY,
        hover_color=Colors.LIGHT_GRAY,
        border_color=Colors.PRIMARY,
        border_width=2,
        corner_radius=3,
        command=handle_place_homepage
    )

    disconnect_button = CTkButton(
        page_content,
        width=120,
        height=30,
        fg_color=Colors.RED,
        text="Déconnexion",
        font=font_title(15),
        text_color=Colors.WHITE,
        hover_color="#802020",
        corner_radius=3,
        command=disconnect
    )

    disconnect_button.place(relx=0.8, y=40)

    if place_home_button:
        home_button.place(x=0, y=40)


def place_loading_frame_fullpage(window: CTk):

    logo_image = CTkImage(light_image=Image.open("assets/images/logo.png"), size=(47, 40))
    logo_label = CTkLabel(window, image=logo_image, text=None)

    loading_label = CTkLabel(
        window, 
        text="Chargement...", 
        text_color=Colors.PRIMARY, 
        font=font_title(32),
    )

    loading_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    logo_label.place(relx=0.37, rely=0.501, anchor=CENTER)

    return [loading_label, logo_label]
