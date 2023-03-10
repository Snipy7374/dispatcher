"""
This type stub file was generated by pyright.
"""

import inspect
import nextcord
from typing import Any, Dict, List, Protocol, TYPE_CHECKING, Tuple, Type, TypeVar, Union, runtime_checkable
from .errors import *
from nextcord.member import Member
from nextcord.user import User
from .context import Context

if TYPE_CHECKING:
    ...
__all__ = ("Converter", "ObjectConverter", "MemberConverter", "UserConverter", "MessageConverter", "PartialMessageConverter", "TextChannelConverter", "InviteConverter", "GuildConverter", "RoleConverter", "GameConverter", "ColourConverter", "ColorConverter", "VoiceChannelConverter", "StageChannelConverter", "EmojiConverter", "PartialEmojiConverter", "CategoryChannelConverter", "IDConverter", "ThreadConverter", "GuildChannelConverter", "GuildStickerConverter", "ScheduledEventConverter", "clean_content", "Greedy", "run_converters")
_utils_get = ...
T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
CT = TypeVar("CT", bound=nextcord.abc.GuildChannel)
TT = TypeVar("TT", bound=nextcord.Thread)
@runtime_checkable
class Converter(Protocol[T_co]):
    """The base class of custom converters that require the :class:`.Context`
    to be passed to be useful.

    This allows you to implement converters that function similar to the
    special cased ``discord`` classes.

    Classes that derive from this should override the :meth:`~.Converter.convert`
    method to do its conversion logic. This method must be a :ref:`coroutine <coroutine>`.
    """
    async def convert(self, ctx: Context, argument: str) -> T_co:
        """|coro|

        The method to override to do conversion logic.

        If an error is found while converting, it is recommended to
        raise a :exc:`.CommandError` derived exception as it will
        properly propagate to the error handlers.

        Parameters
        ----------
        ctx: :class:`.Context`
            The invocation context that the argument is being used in.
        argument: :class:`str`
            The argument that is being converted.

        Raises
        ------
        :exc:`.CommandError`
            A generic exception occurred when converting the argument.
        :exc:`.BadArgument`
            The converter failed to convert the argument.
        """
        ...
    


_ID_REGEX = ...
class IDConverter(Converter[T_co]):
    ...


class ObjectConverter(IDConverter[nextcord.Object]):
    """Converts to a :class:`~nextcord.Object`.

    The argument must follow the valid ID or mention formats (e.g. ``<@80088516616269824>``).

    .. versionadded:: 2.0

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by member, role, or channel mention.
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Object:
        ...
    


class MemberConverter(IDConverter[nextcord.Member]):
    """Converts to a :class:`~nextcord.Member`.

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name#discrim
    4. Lookup by name
    5. Lookup by nickname

    .. versionchanged:: 1.5
         Raise :exc:`.MemberNotFound` instead of generic :exc:`.BadArgument`

    .. versionchanged:: 1.5.1
        This converter now lazily fetches members from the gateway and HTTP APIs,
        optionally caching the result if :attr:`.MemberCacheFlags.joined` is enabled.
    """
    async def query_member_named(self, guild, argument: str): # -> Member | None:
        ...
    
    async def query_member_by_id(self, bot, guild, user_id): # -> None:
        ...
    
    async def convert(self, ctx: Context, argument: str) -> nextcord.Member:
        ...
    


class UserConverter(IDConverter[nextcord.User]):
    """Converts to a :class:`~nextcord.User`.

    All lookups are via the global user cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name#discrim
    4. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.UserNotFound` instead of generic :exc:`.BadArgument`

    .. versionchanged:: 1.6
        This converter now lazily fetches users from the HTTP APIs if an ID is passed
        and it's not available in cache.
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.User:
        ...
    


class PartialMessageConverter(Converter[nextcord.PartialMessage]):
    """Converts to a :class:`nextcord.PartialMessage`.

    .. versionadded:: 1.7

    The creation strategy is as follows (in order):

    1. By "{channel ID}-{message ID}" (retrieved by shift-clicking on "Copy ID")
    2. By message ID (The message is assumed to be in the context channel.)
    3. By message URL
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.PartialMessage:
        ...
    


class MessageConverter(IDConverter[nextcord.Message]):
    """Converts to a :class:`nextcord.Message`.

    .. versionadded:: 1.1

    The lookup strategy is as follows (in order):

    1. Lookup by "{channel ID}-{message ID}" (retrieved by shift-clicking on "Copy ID")
    2. Lookup by message ID (the message **must** be in the context channel)
    3. Lookup by message URL

    .. versionchanged:: 1.5
         Raise :exc:`.ChannelNotFound`, :exc:`.MessageNotFound` or :exc:`.ChannelNotReadable` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Message:
        ...
    


class GuildChannelConverter(IDConverter[nextcord.abc.GuildChannel]):
    """Converts to a :class:`~nextcord.abc.GuildChannel`.

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name.

    .. versionadded:: 2.0
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.abc.GuildChannel:
        ...
    


class TextChannelConverter(IDConverter[nextcord.TextChannel]):
    """Converts to a :class:`~nextcord.TextChannel`.

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.ChannelNotFound` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.TextChannel:
        ...
    


class VoiceChannelConverter(IDConverter[nextcord.VoiceChannel]):
    """Converts to a :class:`~nextcord.VoiceChannel`.

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.ChannelNotFound` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.VoiceChannel:
        ...
    


class StageChannelConverter(IDConverter[nextcord.StageChannel]):
    """Converts to a :class:`~nextcord.StageChannel`.

    .. versionadded:: 1.7

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.StageChannel:
        ...
    


class CategoryChannelConverter(IDConverter[nextcord.CategoryChannel]):
    """Converts to a :class:`~nextcord.CategoryChannel`.

    All lookups are via the local guild. If in a DM context, then the lookup
    is done by the global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.ChannelNotFound` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.CategoryChannel:
        ...
    


class ThreadConverter(IDConverter[nextcord.Thread]):
    """Coverts to a :class:`~nextcord.Thread`.

    All lookups are via the local guild.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name.

    .. versionadded: 2.0
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Thread:
        ...
    


class ColourConverter(Converter[nextcord.Colour]):
    """Converts to a :class:`~nextcord.Colour`.

    .. versionchanged:: 1.5
        Add an alias named ColorConverter

    The following formats are accepted:

    - ``0x<hex>``
    - ``#<hex>``
    - ``0x#<hex>``
    - ``rgb(<number>, <number>, <number>)``
    - Any of the ``classmethod`` in :class:`~nextcord.Colour`

        - The ``_`` in the name can be optionally replaced with spaces.

    Like CSS, ``<number>`` can be either 0-255 or 0-100% and ``<hex>`` can be
    either a 6 digit hex number or a 3 digit hex shortcut (e.g. #fff).

    .. versionchanged:: 1.5
         Raise :exc:`.BadColourArgument` instead of generic :exc:`.BadArgument`

    .. versionchanged:: 1.7
        Added support for ``rgb`` function and 3-digit hex shortcuts
    """
    RGB_REGEX = ...
    def parse_hex_number(self, argument): # -> Color:
        ...
    
    def parse_rgb_number(self, argument, number): # -> int:
        ...
    
    def parse_rgb(self, argument, *, regex=...): # -> Color:
        ...
    
    async def convert(self, ctx: Context, argument: str) -> nextcord.Colour:
        ...
    


ColorConverter = ColourConverter
class RoleConverter(IDConverter[nextcord.Role]):
    """Converts to a :class:`~nextcord.Role`.

    All lookups are via the local guild. If in a DM context, the converter raises
    :exc:`.NoPrivateMessage` exception.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by mention.
    3. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.RoleNotFound` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Role:
        ...
    


class GameConverter(Converter[nextcord.Game]):
    """Converts to :class:`~nextcord.Game`."""
    async def convert(self, ctx: Context, argument: str) -> nextcord.Game:
        ...
    


class InviteConverter(Converter[nextcord.Invite]):
    """Converts to a :class:`~nextcord.Invite`.

    This is done via an HTTP request using :meth:`.Bot.fetch_invite`.

    .. versionchanged:: 1.5
         Raise :exc:`.BadInviteArgument` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Invite:
        ...
    


class GuildConverter(IDConverter[nextcord.Guild]):
    """Converts to a :class:`~nextcord.Guild`.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).

    .. versionadded:: 1.7
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Guild:
        ...
    


class EmojiConverter(IDConverter[nextcord.Emoji]):
    """Converts to a :class:`~nextcord.Emoji`.

    All lookups are done for the local guild first, if available. If that lookup
    fails, then it checks the client's global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    2. Lookup by extracting ID from the emoji.
    3. Lookup by name

    .. versionchanged:: 1.5
         Raise :exc:`.EmojiNotFound` instead of generic :exc:`.BadArgument`
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.Emoji:
        ...
    


class PartialEmojiConverter(Converter[nextcord.PartialEmoji]):
    """Converts to a :class:`~nextcord.PartialEmoji`.

    This is done by extracting the animated flag, name and ID from the emoji.

    If the emoji is a unicode emoji, then the name is the unicode character.

    .. versionchanged:: 1.5
         Raise :exc:`.PartialEmojiConversionFailure` instead of generic :exc:`.BadArgument`

    .. versionchanged:: 2.1
        Add support for converting unicode emojis
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.PartialEmoji:
        ...
    


class GuildStickerConverter(IDConverter[nextcord.GuildSticker]):
    """Converts to a :class:`~nextcord.GuildSticker`.

    All lookups are done for the local guild first, if available. If that lookup
    fails, then it checks the client's global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    3. Lookup by name

    .. versionadded:: 2.0
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.GuildSticker:
        ...
    


_EVENT_INVITE_RE = ...
_EVENT_API_RE = ...
class ScheduledEventConverter(IDConverter[nextcord.ScheduledEvent]):
    """Converts to a :class:`~nextcord.ScheduledEvent`.

    All lookups are done for the local guild first, if available. If that lookup
    fails, then it checks the client's global cache.

    The lookup strategy is as follows (in order):

    1. Lookup by ID.
    3. Lookup by name
    3. Lookup by url (invite?event=id and /guildid/eventid)

    .. versionadded:: 2.0
    """
    async def convert(self, ctx: Context, argument: str) -> nextcord.ScheduledEvent:
        ...
    


class clean_content(Converter[str]):
    """Converts the argument to mention scrubbed version of
    said content.

    This behaves similarly to :attr:`~nextcord.Message.clean_content`.

    Attributes
    ----------
    fix_channel_mentions: :class:`bool`
        Whether to clean channel mentions.
    use_nicknames: :class:`bool`
        Whether to use nicknames when transforming mentions.
    escape_markdown: :class:`bool`
        Whether to also escape special markdown characters.
    remove_markdown: :class:`bool`
        Whether to also remove special markdown characters. This option is not supported with ``escape_markdown``

        .. versionadded:: 1.7
    """
    def __init__(self, *, fix_channel_mentions: bool = ..., use_nicknames: bool = ..., escape_markdown: bool = ..., remove_markdown: bool = ...) -> None:
        ...
    
    async def convert(self, ctx: Context, argument: str) -> str:
        ...
    


class Greedy(List[T]):
    r"""A special converter that greedily consumes arguments until it can't.
    As a consequence of this behaviour, most input errors are silently discarded,
    since it is used as an indicator of when to stop parsing.

    When a parser error is met the greedy converter stops converting, undoes the
    internal string parsing routine, and continues parsing regularly.

    For example, in the following code:

    .. code-block:: python3

        @commands.command()
        async def test(ctx, numbers: Greedy[int], reason: str):
            await ctx.send("numbers: {}, reason: {}".format(numbers, reason))

    An invocation of ``[p]test 1 2 3 4 5 6 hello`` would pass ``numbers`` with
    ``[1, 2, 3, 4, 5, 6]`` and ``reason`` with ``hello``\.

    For more information, check :ref:`ext_commands_special_converters`.
    """
    __slots__ = ...
    def __init__(self, *, converter: T) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __class_getitem__(cls, params: Union[Tuple[T], T]) -> Greedy[T]:
        ...
    


def get_converter(param: inspect.Parameter) -> Any:
    ...

_GenericAlias = ...
def is_generic_type(tp: Any, *, _GenericAlias: Type = ...) -> bool:
    ...

CONVERTER_MAPPING: Dict[Type[Any], Any] = ...
async def run_converters(ctx: Context, converter, argument: str, param: inspect.Parameter): # -> Any | bool | None:
    """|coro|

    Runs converters for a given converter, argument, and parameter.

    This function does the same work that the library does under the hood.

    .. versionadded:: 2.0

    Parameters
    ----------
    ctx: :class:`Context`
        The invocation context to run the converters under.
    converter: Any
        The converter to run, this corresponds to the annotation in the function.
    argument: :class:`str`
        The argument to convert to.
    param: :class:`inspect.Parameter`
        The parameter being converted. This is mainly for error reporting.

    Raises
    ------
    CommandError
        The converter failed to convert.

    Returns
    -------
    Any
        The resulting conversion.
    """
    ...
