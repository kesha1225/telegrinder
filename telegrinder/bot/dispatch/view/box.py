import dataclasses

import typing_extensions as typing

from .abc import ABCView
from .callback_query import CallbackQueryView
from .composition import CompositionView
from .inline_query import InlineQueryView
from .message import MessageView

CallbackQueryViewT = typing.TypeVar(
    "CallbackQueryViewT", bound=ABCView, default=CallbackQueryView
)
CompositionViewT = typing.TypeVar("CompositionViewT", bound=ABCView, default=CompositionView)
InlineQueryViewT = typing.TypeVar(
    "InlineQueryViewT", bound=ABCView, default=InlineQueryView
)
MessageViewT = typing.TypeVar("MessageViewT", bound=ABCView, default=MessageView)


@dataclasses.dataclass(frozen=True, kw_only=True)
class ViewBox(typing.Generic[CallbackQueryViewT, InlineQueryViewT, MessageViewT, CompositionViewT]):
    callback_query: CallbackQueryViewT = dataclasses.field(  # type: ignore
        default_factory=lambda: CallbackQueryView(),
    )
    composition: CompositionViewT = dataclasses.field(  # type: ignore
        default_factory=lambda: CompositionView(),
    )
    inline_query: InlineQueryViewT = dataclasses.field(  # type: ignore
        default_factory=lambda: InlineQueryView(),
    )
    message: MessageViewT = dataclasses.field(  # type: ignore
        default_factory=lambda: MessageView(),
    )

    def get_views(self) -> dict[str, ABCView]:
        return {
            name: view for name, view in self.__dict__.items()
            if isinstance(view, ABCView)
        }
    