from .abc import ABCMessageRule
from .markup import Markup, Message
import typing


class StartCommand(
    ABCMessageRule,
    require=[Markup(["/start <param>", "/start"])]
):
    def __init__(
        self, 
        validator: typing.Callable[str, typing.Any | None] | None = None,
        param_required: bool = False,
    ) -> None:
        self.param_required = param_required
        self.validator = validator

    async def check(self, message: Message, ctx: dict) -> bool:
        param: str | None = ctx.get("param")
        validated_param = (
            self.validator(param) 
            if self.validator and param is not None 
            else param
        )

        if self.param_required and validated_param is None:
            return False
        
        ctx["param"] = validated_param
        return True
