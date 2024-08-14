from customtkinter import CTkFont, CTkFrame
from PIL import ImageFont

class Colors:
    PRIMARY = "#3E7CB1"
    PRIMARY_HOVER = "#336B9B"

    SECONDARY = "#2D2D2A"
    SECONDARY_LIGHT = "#4F4F49"

    TERTIARY = "#F9F7F3"
    TERTIARY_LIGHT = "#F9F7F3"

    WHITE = "#FFFFFF"
    LIGHT_GRAY = "#E5E7EB"

    RED = "#b51d18"

def font_title(size: int) -> CTkFont:
    return CTkFont(family="Helvetica", size=size, weight="bold")

def font_text(size: int) -> CTkFont:
    return CTkFont(family="Roboto", size=size, weight="bold")

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
