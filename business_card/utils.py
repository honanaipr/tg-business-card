from aiogram import Dispatcher, Router
from aiogram_dialog import Dialog, DialogRegistry
from urllib.parse import quote

def get_placehold_image_url(text=None, size=(600,400), font="playfair-display", format="jpg"):
    return f"https://placehold.co/{size[0]}x{size[1]}.{format}?text={quote(text)}&font={font}"