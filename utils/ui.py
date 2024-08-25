from customtkinter import CTkFont, CTkFrame
from PIL import ImageFont

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
