from aiogram.filters import Command
from aiogram.enums import InlineQueryResultType
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton, ChosenInlineResult, Message, InlineQueryResultArticle

from loguru import logger
from aiogram import Router
from aiogram.methods import EditMessageText
from business_card.loader import bot

from deep_translator import GoogleTranslator

tg_trans = GoogleTranslator(source="auto", target="tg")
uz_trans = GoogleTranslator(source="auto", target="uz")

def get_translations(text: str) -> dict:
    response = {}
    response['tg'] = tg_trans.translate(text=text)
    response['uz'] = uz_trans.translate(text=text)
    return response



translation_router = Router()

@translation_router.inline_query()
async def inline_echo(inline_query: InlineQuery):
    if not inline_query.query:
        return
    input_content = InputTextMessageContent(message_text=inline_query.query)
    keyboard = InlineKeyboardMarkup(inline_keyboard=
        [
            [
                InlineKeyboardButton(text="🔄", callback_data=inline_query.query)
            ]
        ]
    )
    item = InlineQueryResultArticle(id='1', title='Перевести',
                                    type=InlineQueryResultType.ARTICLE,
                                    input_message_content=input_content,
                                    reply_markup=keyboard
                                    )
    # button = InlineQueryResultsButton(text="~~Регистрация~~", start_parameter="_")
    await inline_query.answer(results=[item], cache_time=0)

@translation_router.chosen_inline_result()
async def chosen_inline_result_handler(r: ChosenInlineResult):
    if not r.query:
        return
    origin = f"{r.query}"
    translations = get_translations(r.query)
    ru_trans = f"ru:\n{r.query}"
    tg_trans = f"tg:\n{translations['tg']}"
    uz_trans = f"uz:\n{translations['uz']}"
    await bot(EditMessageText(inline_message_id=r.inline_message_id, text="\n".join([ru_trans, tg_trans, uz_trans])))
    # logger.info("\n".join([ru_trans, tg_trans, uz_trans]))

# @translate_dialog.message(Command("start"))
# async def command_start_handler(m: Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=
#         [
#             [
#                 InlineKeyboardButton(text="Попробовать", switch_inline_query="Привет")
#             ]
#         ]
#     )
#     await m.answer("OK", reply_markup=markup)
