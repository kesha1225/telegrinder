from telegrinder import API, Checkbox, Message, Telegrinder, Token, WaiterMachine
from telegrinder.modules import logger
from telegrinder.rules import Text

api = API(token=Token.from_env())
bot = Telegrinder(api)
wm = WaiterMachine(bot.dispatch)
logger.set_level("INFO")


@bot.on.message(Text("/checkbox"))
async def action(m: Message):
    picked, m_id = await (
        Checkbox(wm, m.chat.id, "Check your checkbox", max_in_row=2)
        .add_option("apple", "Apple", "Apple 🍏")
        .add_option("banana", "Banana", "Banana 🍌", is_picked=True)
        .add_option("pear", "Pear", "Pear 🍐")
        .wait(m.ctx_api, bot.dispatch.callback_query)
    )
    await m.edit(
        text="You picked: {}".format(", ".join(c for c in picked if picked[c])),
        chat_id=m.chat.id,
        message_id=m_id,
    )


bot.run_forever()
