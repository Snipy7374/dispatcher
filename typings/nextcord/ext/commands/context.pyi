"""
This type stub file was generated by pyright.
"""

import inspect
import nextcord.abc
import nextcord.utils
from typing import Any, Dict, Generic, List, Optional, TYPE_CHECKING, TypeVar, Union
from nextcord.message import Message
from typing_extensions import ParamSpec
from nextcord.abc import MessageableChannel
from nextcord.guild import Guild
from nextcord.member import Member
from nextcord.user import ClientUser, User
from nextcord.voice_client import VoiceProtocol
from .cog import Cog
from .core import Command
from .view import StringView

if TYPE_CHECKING:
    ...
__all__ = ("Context", )
MISSING: Any = ...
T = TypeVar("T")
BotT = TypeVar("BotT", bound="Union[Bot, AutoShardedBot]")
CogT = TypeVar("CogT", bound="Cog")
if TYPE_CHECKING:
    P = ParamSpec("P")
else:
    ...
class Context(nextcord.abc.Messageable, Generic[BotT]):
    r"""Represents the context in which a command is being invoked under.

    This class contains a lot of meta data to help you understand more about
    the invocation context. This class is not created manually and is instead
    passed around to commands as the first parameter.

    This class implements the :class:`~nextcord.abc.Messageable` ABC.

    Attributes
    ----------
    message: :class:`.Message`
        The message that triggered the command being executed.
    bot: :class:`.Bot`
        The bot that contains the command being executed.
    args: :class:`list`
        The list of transformed arguments that were passed into the command.
        If this is accessed during the :func:`.on_command_error` event
        then this list could be incomplete.
    kwargs: :class:`dict`
        A dictionary of transformed arguments that were passed into the command.
        Similar to :attr:`args`\, if this is accessed in the
        :func:`.on_command_error` event then this dict could be incomplete.
    current_parameter: Optional[:class:`inspect.Parameter`]
        The parameter that is currently being inspected and converted.
        This is only of use for within converters.

        .. versionadded:: 2.0
    prefix: Optional[:class:`str`]
        The prefix that was used to invoke the command.
    command: Optional[:class:`Command`]
        The command that is being invoked currently.
    invoked_with: Optional[:class:`str`]
        The command name that triggered this invocation. Useful for finding out
        which alias called the command.
    invoked_parents: List[:class:`str`]
        The command names of the parents that triggered this invocation. Useful for
        finding out which aliases called the command.

        For example in commands ``?a b c test``, the invoked parents are ``['a', 'b', 'c']``.

        .. versionadded:: 1.7

    invoked_subcommand: Optional[:class:`Command`]
        The subcommand that was invoked.
        If no valid subcommand was invoked then this is equal to ``None``.
    subcommand_passed: Optional[:class:`str`]
        The string that was attempted to call a subcommand. This does not have
        to point to a valid registered subcommand and could just point to a
        nonsense string. If nothing was passed to attempt a call to a
        subcommand then this is set to ``None``.
    command_failed: :class:`bool`
        A boolean that indicates if the command failed to be parsed, checked,
        or invoked.
    """
    def __init__(self, *, message: Message, bot: BotT, view: StringView, args: List[Any] = ..., kwargs: Dict[str, Any] = ..., prefix: Optional[str] = ..., command: Optional[Command] = ..., invoked_with: Optional[str] = ..., invoked_parents: List[str] = ..., invoked_subcommand: Optional[Command] = ..., subcommand_passed: Optional[str] = ..., command_failed: bool = ..., current_parameter: Optional[inspect.Parameter] = ...) -> None:
        ...
    
    async def invoke(self, command: Command[CogT, P, T], /, *args: P.args, **kwargs: P.kwargs) -> T:
        r"""|coro|

        Calls a command with the arguments given.

        This is useful if you want to just call the callback that a
        :class:`.Command` holds internally.

        .. note::

            This does not handle converters, checks, cooldowns, pre-invoke,
            or after-invoke hooks in any matter. It calls the internal callback
            directly as-if it was a regular function.

            You must take care in passing the proper arguments when
            using this function.

        Parameters
        ----------
        command: :class:`.Command`
            The command that is going to be called.
        \*args
            The arguments to use.
        \*\*kwargs
            The keyword arguments to use.

        Raises
        ------
        TypeError
            The command argument to invoke is missing.
        """
        ...
    
    async def reinvoke(self, *, call_hooks: bool = ..., restart: bool = ...) -> None:
        """|coro|

        Calls the command again.

        This is similar to :meth:`~.Context.invoke` except that it bypasses
        checks, cooldowns, and error handlers.

        .. note::

            If you want to bypass :exc:`.UserInputError` derived exceptions,
            it is recommended to use the regular :meth:`~.Context.invoke`
            as it will work more naturally. After all, this will end up
            using the old arguments the user has used and will thus just
            fail again.

        Parameters
        ----------
        call_hooks: :class:`bool`
            Whether to call the before and after invoke hooks.
        restart: :class:`bool`
            Whether to start the call chain from the very beginning
            or where we left off (i.e. the command that caused the error).
            The default is to start where we left off.

        Raises
        ------
        ValueError
            The context to reinvoke is not valid.
        """
        ...
    
    @property
    def valid(self) -> bool:
        """:class:`bool`: Checks if the invocation context is valid to be invoked with."""
        ...
    
    @property
    def clean_prefix(self) -> str:
        """:class:`str`: The cleaned up invoke prefix. i.e. mentions are ``@name`` instead of ``<@id>``.

        .. versionadded:: 2.0
        """
        ...
    
    @property
    def cog(self) -> Optional[Cog]:
        """Optional[:class:`.Cog`]: Returns the cog associated with this context's command. None if it does not exist."""
        ...
    
    @nextcord.utils.cached_property
    def guild(self) -> Optional[Guild]:
        """Optional[:class:`.Guild`]: Returns the guild associated with this context's command. None if not available."""
        ...
    
    @nextcord.utils.cached_property
    def channel(self) -> MessageableChannel:
        """Union[:class:`.abc.Messageable`]: Returns the channel associated with this context's command.
        Shorthand for :attr:`.Message.channel`.
        """
        ...
    
    @nextcord.utils.cached_property
    def author(self) -> Union[User, Member]:
        """Union[:class:`~nextcord.User`, :class:`.Member`]:
        Returns the author associated with this context's command. Shorthand for :attr:`.Message.author`
        """
        ...
    
    @nextcord.utils.cached_property
    def me(self) -> Union[Member, ClientUser]:
        """Union[:class:`.Member`, :class:`.ClientUser`]:
        Similar to :attr:`.Guild.me` except it may return the :class:`.ClientUser` in private message contexts.
        """
        ...
    
    @property
    def voice_client(self) -> Optional[VoiceProtocol]:
        r"""Optional[:class:`.VoiceProtocol`]: A shortcut to :attr:`.Guild.voice_client`\, if applicable."""
        ...
    
    async def send_help(self, *args: Any) -> Any:
        """send_help(entity=<bot>)

        |coro|

        Shows the help command for the specified entity if given.
        The entity can be a command or a cog.

        If no entity is given, then it'll show help for the
        entire bot.

        If the entity is a string, then it looks up whether it's a
        :class:`Cog` or a :class:`Command`.

        .. note::

            Due to the way this function works, instead of returning
            something similar to :meth:`~.commands.HelpCommand.command_not_found`
            this returns :class:`None` on bad input or no help command.

        Parameters
        ----------
        entity: Optional[Union[:class:`Command`, :class:`Cog`, :class:`str`]]
            The entity to show help for.

        Returns
        -------
        Any
            The result of the help command, if any.
        """
        ...
    
    @nextcord.utils.copy_doc(Message.reply)
    async def reply(self, content: Optional[str] = ..., **kwargs: Any) -> Message:
        ...
    


