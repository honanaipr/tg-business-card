from aiogram import Dispatcher, Router
from aiogram_dialog import Dialog
from urllib.parse import quote
from loguru import logger
import logging

def get_placehold_image_url(text=None, size=(600,200), font="playfair-display", format="jpg"):
    return f"https://placehold.co/{size[0]}x{size[1]}.{format}?text={quote(text)}&font={font}"

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())