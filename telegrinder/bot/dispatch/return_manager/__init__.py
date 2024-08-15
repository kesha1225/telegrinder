from telegrinder.bot.dispatch.return_manager.abc import (
    ABCReturnManager,
    BaseReturnManager,
    Manager,
    register_manager,
)
from telegrinder.bot.dispatch.return_manager.callback_query import CallbackQueryReturnManager
from telegrinder.bot.dispatch.return_manager.inline_query import InlineQueryReturnManager
from telegrinder.bot.dispatch.return_manager.message import MessageReturnManager

__all__ = (
    "ABCReturnManager",
    "BaseReturnManager",
    "CallbackQueryReturnManager",
    "InlineQueryReturnManager",
    "Manager",
    "MessageReturnManager",
    "register_manager",
)
