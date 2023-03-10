"""
This type stub file was generated by pyright.
"""

import array
import asyncio
import datetime
from typing import Any, AsyncIterator, Awaitable, Callable, Dict, Generic, Iterable, Iterator, List, Literal, Optional, Sequence, Set, TYPE_CHECKING, Tuple, Type, TypeVar, Union, overload
from .file import File
from types import UnionType
from typing_extensions import ParamSpec, Self
from .abc import Snowflake
from .asset import Asset
from .invite import Invite
from .message import Attachment
from .permissions import Permissions
from .template import Template

HAS_ORJSON = ...
PY_310 = ...
if PY_310:
    ...
else:
    UnionType = ...
if TYPE_CHECKING:
    ...
__all__ = ("oauth_url", "snowflake_time", "time_snowflake", "find", "get", "sleep_until", "utcnow", "remove_markdown", "escape_markdown", "escape_mentions", "parse_raw_mentions", "parse_raw_role_mentions", "parse_raw_channel_mentions", "as_chunks", "format_dt")
DISCORD_EPOCH = ...
class _MissingSentinel:
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __repr__(self) -> str:
        ...
    


MISSING: Any = ...
class _cached_property:
    def __init__(self, function: Callable[..., Any]) -> None:
        ...
    
    def __get__(self, instance: Any, owner: Any): # -> Self@_cached_property | Any:
        ...
    


if TYPE_CHECKING:
    P = ParamSpec("P")
else:
    ...
T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
_Iter = Union[Iterator[T], AsyncIterator[T]]
ArrayT = TypeVar("ArrayT", int, float, str)
class CachedSlotProperty(Generic[T, T_co]):
    def __init__(self, name: str, function: Callable[[T], T_co]) -> None:
        ...
    
    @overload
    def __get__(self, instance: None, owner: Type[T]) -> CachedSlotProperty[T, T_co]:
        ...
    
    @overload
    def __get__(self, instance: T, owner: Type[T]) -> T_co:
        ...
    
    def __get__(self, instance: Optional[T], owner: Type[T]) -> Any:
        ...
    


class classproperty(Generic[T_co]):
    def __init__(self, fget: Callable[[Any], T_co]) -> None:
        ...
    
    def __get__(self, instance: Optional[Any], owner: Type[Any]) -> T_co:
        ...
    
    def __set__(self, instance: Any, value: Any) -> None:
        ...
    


def cached_slot_property(name: str) -> Callable[[Callable[[T], T_co]], CachedSlotProperty[T, T_co]]:
    ...

class SequenceProxy(Sequence[T_co], Generic[T_co]):
    """Read-only proxy of a Sequence."""
    def __init__(self, proxied: Sequence[T_co]) -> None:
        ...
    
    def __getitem__(self, idx: int) -> T_co:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, item: Any) -> bool:
        ...
    
    def __iter__(self) -> Iterator[T_co]:
        ...
    
    def __reversed__(self) -> Iterator[T_co]:
        ...
    
    def index(self, value: Any, *args: Any, **kwargs: Any) -> int:
        ...
    
    def count(self, value: Any) -> int:
        ...
    


@overload
def parse_time(timestamp: None) -> None:
    ...

@overload
def parse_time(timestamp: str) -> datetime.datetime:
    ...

@overload
def parse_time(timestamp: Optional[str]) -> Optional[datetime.datetime]:
    ...

def parse_time(timestamp: Optional[str]) -> Optional[datetime.datetime]:
    ...

def copy_doc(original: Callable[..., Any]) -> Callable[[T], T]:
    ...

def deprecated(instead: Optional[str] = ...) -> Callable[[Callable[P, T]], Callable[P, T]]:
    ...

def oauth_url(client_id: Union[int, str], *, permissions: Permissions = ..., guild: Snowflake = ..., redirect_uri: str = ..., scopes: Iterable[str] = ..., disable_guild_select: bool = ...) -> str:
    """A helper function that returns the OAuth2 URL for inviting the bot
    into guilds.

    Parameters
    ----------
    client_id: Union[:class:`int`, :class:`str`]
        The client ID for your bot.
    permissions: :class:`~nextcord.Permissions`
        The permissions you're requesting. If not given then you won't be requesting any
        permissions.
    guild: :class:`~nextcord.abc.Snowflake`
        The guild to pre-select in the authorization screen, if available.
    redirect_uri: :class:`str`
        An optional valid redirect URI.
    scopes: Iterable[:class:`str`]
        An optional valid list of scopes. Defaults to ``('bot',)``.

        .. versionadded:: 1.7
    disable_guild_select: :class:`bool`
        Whether to disallow the user from changing the guild dropdown.

        .. versionadded:: 2.0

    Returns
    -------
    :class:`str`
        The OAuth2 URL for inviting the bot into guilds.
    """
    ...

def snowflake_time(id: int) -> datetime.datetime:
    """
    Parameters
    ----------
    id: :class:`int`
        The snowflake ID.

    Returns
    -------
    :class:`datetime.datetime`
        An aware datetime in UTC representing the creation time of the snowflake.
    """
    ...

def time_snowflake(dt: datetime.datetime, high: bool = ...) -> int:
    """Returns a numeric snowflake pretending to be created at the given date.

    When using as the lower end of a range, use ``time_snowflake(high=False) - 1``
    to be inclusive, ``high=True`` to be exclusive.

    When using as the higher end of a range, use ``time_snowflake(high=True) + 1``
    to be inclusive, ``high=False`` to be exclusive

    Parameters
    ----------
    dt: :class:`datetime.datetime`
        A datetime object to convert to a snowflake.
        If naive, the timezone is assumed to be local time.
    high: :class:`bool`
        Whether or not to set the lower 22 bit to high or low.

    Returns
    -------
    :class:`int`
        The snowflake representing the time given.
    """
    ...

def find(predicate: Callable[[T], Any], seq: Iterable[T]) -> Optional[T]:
    """A helper to return the first element found in the sequence
    that meets the predicate. For example: ::

        member = nextcord.utils.find(lambda m: m.name == 'Mighty', channel.guild.members)

    would find the first :class:`~nextcord.Member` whose name is 'Mighty' and return it.
    If an entry is not found, then ``None`` is returned.

    This is different from :func:`py:filter` due to the fact it stops the moment it finds
    a valid entry.

    Parameters
    ----------
    predicate
        A function that returns a boolean-like result.
    seq: :class:`collections.abc.Iterable`
        The iterable to search through.
    """
    ...

def get(iterable: Iterable[T], **attrs: Any) -> Optional[T]:
    r"""A helper that returns the first element in the iterable that meets
    all the traits passed in ``attrs``. This is an alternative for
    :func:`~nextcord.utils.find`.

    When multiple attributes are specified, they are checked using
    logical AND, not logical OR. Meaning they have to meet every
    attribute passed in and not one of them.

    To have a nested attribute search (i.e. search by ``x.y``) then
    pass in ``x__y`` as the keyword argument.

    If nothing is found that matches the attributes passed, then
    ``None`` is returned.

    Examples
    --------

    Basic usage:

    .. code-block:: python3

        member = nextcord.utils.get(message.guild.members, name='Foo')

    Multiple attribute matching:

    .. code-block:: python3

        channel = nextcord.utils.get(guild.voice_channels, name='Foo', bitrate=64000)

    Nested attribute matching:

    .. code-block:: python3

        channel = nextcord.utils.get(client.get_all_channels(), guild__name='Cool', name='general')

    Parameters
    ----------
    iterable
        An iterable to search through.
    \*\*attrs
        Keyword arguments that denote attributes to search with.
    """
    ...

def unique(iterable: Iterable[T]) -> List[T]:
    ...

def get_as_snowflake(data: Any, key: str) -> Optional[int]:
    ...

async def obj_to_base64_data(obj: Optional[Union[bytes, Attachment, Asset, File]]) -> Optional[str]:
    ...

def parse_ratelimit_header(request: Any, *, use_clock: bool = ...) -> float:
    ...

async def maybe_coroutine(f: Callable[P, Union[T, Awaitable[T]]], *args: P.args, **kwargs: P.kwargs) -> T:
    ...

async def async_all(gen: Iterable[Awaitable[T]], *, check: Callable[[Awaitable[T]], bool] = ...) -> bool:
    ...

async def sane_wait_for(futures: Iterable[Awaitable[T]], *, timeout: Optional[float]) -> Set[asyncio.Task[T]]:
    ...

def get_slots(cls: Type[Any]) -> Iterator[str]:
    ...

def compute_timedelta(dt: datetime.datetime) -> float:
    ...

async def sleep_until(when: datetime.datetime, result: Optional[T] = ...) -> Optional[T]:
    """|coro|

    Sleep until a specified time.

    If the time supplied is in the past this function will yield instantly.

    .. versionadded:: 1.3

    Parameters
    ----------
    when: :class:`datetime.datetime`
        The timestamp in which to sleep until. If the datetime is naive then
        it is assumed to be local time.
    result: Any
        If provided is returned to the caller when the coroutine completes.
    """
    ...

def utcnow() -> datetime.datetime:
    """A helper function to return an aware UTC datetime representing the current time.

    This should be preferred to :meth:`datetime.datetime.utcnow` since it is an aware
    datetime, compared to the naive datetime in the standard library.

    .. versionadded:: 2.0

    Returns
    -------
    :class:`datetime.datetime`
        The current aware datetime in UTC.
    """
    ...

def valid_icon_size(size: int) -> bool:
    """Icons must be power of 2 within [16, 4096]."""
    ...

class SnowflakeList(array.array):
    """Internal data storage class to efficiently store a list of snowflakes.

    This should have the following characteristics:

    - Low memory usage
    - O(n) iteration (obviously)
    - O(n log n) initial creation if data is unsorted
    - O(log n) search and indexing
    - O(n) insertion
    """
    __slots__ = ...
    if TYPE_CHECKING:
        def __init__(self, data: Iterable[int], *, is_sorted: bool = ...) -> None:
            ...
        
    def __new__(cls, data: Iterable[int], *, is_sorted: bool = ...) -> Self:
        ...
    
    def add(self, element: int) -> None:
        ...
    
    def get(self, element: int) -> Optional[int]:
        ...
    
    def has(self, element: int) -> bool:
        ...
    


_IS_ASCII = ...
def string_width(string: str) -> int:
    """Returns string's width."""
    ...

def resolve_invite(invite: Union[Invite, str]) -> str:
    """
    Resolves an invite from a :class:`~nextcord.Invite`, URL or code.

    Parameters
    ----------
    invite: Union[:class:`~nextcord.Invite`, :class:`str`]
        The invite.

    Returns
    -------
    :class:`str`
        The invite code.
    """
    ...

def resolve_template(code: Union[Template, str]) -> str:
    """
    Resolves a template code from a :class:`~nextcord.Template`, URL or code.

    .. versionadded:: 1.4

    Parameters
    ----------
    code: Union[:class:`~nextcord.Template`, :class:`str`]
        The code.

    Returns
    -------
    :class:`str`
        The template code.
    """
    ...

_MARKDOWN_ESCAPE_SUBREGEX = ...
_MARKDOWN_ESCAPE_COMMON = ...
_MARKDOWN_ESCAPE_REGEX = ...
_URL_REGEX = ...
_MARKDOWN_STOCK_REGEX = ...
def remove_markdown(text: str, *, ignore_links: bool = ...) -> str:
    """A helper function that removes markdown characters.

    .. versionadded:: 1.7

    .. note::
            This function is not markdown aware and may remove meaning from the original text. For example,
            if the input contains ``10 * 5`` then it will be converted into ``10  5``.

    Parameters
    ----------
    text: :class:`str`
        The text to remove markdown from.
    ignore_links: :class:`bool`
        Whether to leave links alone when removing markdown. For example,
        if a URL in the text contains characters such as ``_`` then it will
        be left alone. Defaults to ``True``.

    Returns
    -------
    :class:`str`
        The text with the markdown special characters removed.
    """
    ...

def escape_markdown(text: str, *, as_needed: bool = ..., ignore_links: bool = ...) -> str:
    r"""A helper function that escapes Discord's markdown.

    Parameters
    ----------
    text: :class:`str`
        The text to escape markdown from.
    as_needed: :class:`bool`
        Whether to escape the markdown characters as needed. This
        means that it does not escape extraneous characters if it's
        not necessary, e.g. ``**hello**`` is escaped into ``\*\*hello**``
        instead of ``\*\*hello\*\*``. Note however that this can open
        you up to some clever syntax abuse. Defaults to ``False``.
    ignore_links: :class:`bool`
        Whether to leave links alone when escaping markdown. For example,
        if a URL in the text contains characters such as ``_`` then it will
        be left alone. This option is not supported with ``as_needed``.
        Defaults to ``True``.

    Returns
    -------
    :class:`str`
        The text with the markdown special characters escaped with a slash.
    """
    ...

def escape_mentions(text: str) -> str:
    """A helper function that escapes everyone, here, role, and user mentions.

    .. note::

        This does not include channel mentions.

    .. note::

        For more granular control over what mentions should be escaped
        within messages, refer to the :class:`~nextcord.AllowedMentions`
        class.

    Parameters
    ----------
    text: :class:`str`
        The text to escape mentions from.

    Returns
    -------
    :class:`str`
        The text with the mentions removed.
    """
    ...

def parse_raw_mentions(text: str) -> List[int]:
    """A helper function that parses mentions from a string as an array of :class:`~nextcord.User` IDs
    matched with the syntax of ``<@user_id>`` or ``<@!user_id>``.

    .. note::

        This does not include role or channel mentions. See :func:`parse_raw_role_mentions`
        and :func:`parse_raw_channel_mentions` for those.

    .. versionadded:: 2.2

    Parameters
    ----------
    text: :class:`str`
        The text to parse mentions from.

    Returns
    -------
    List[:class:`int`]
        A list of user IDs that were mentioned.
    """
    ...

def parse_raw_role_mentions(text: str) -> List[int]:
    """A helper function that parses mentions from a string as an array of :class:`~nextcord.Role` IDs
    matched with the syntax of ``<@&role_id>``.

    .. versionadded:: 2.2

    Parameters
    ----------
    text: :class:`str`
        The text to parse mentions from.

    Returns
    -------
    List[:class:`int`]
        A list of role IDs that were mentioned.
    """
    ...

def parse_raw_channel_mentions(text: str) -> List[int]:
    """A helper function that parses mentions from a string as an array of :class:`~nextcord.abc.GuildChannel` IDs
    matched with the syntax of ``<#channel_id>``.

    .. versionadded:: 2.2

    Parameters
    ----------
    text: :class:`str`
        The text to parse mentions from.

    Returns
    -------
    List[:class:`int`]
        A list of channel IDs that were mentioned.
    """
    ...

@overload
def as_chunks(iterator: Iterator[T], max_size: int) -> Iterator[List[T]]:
    ...

@overload
def as_chunks(iterator: AsyncIterator[T], max_size: int) -> AsyncIterator[List[T]]:
    ...

def as_chunks(iterator: _Iter[T], max_size: int) -> _Iter[List[T]]:
    """A helper function that collects an iterator into chunks of a given size.

    .. versionadded:: 2.0

    Parameters
    ----------
    iterator: Union[:class:`collections.abc.Iterator`, :class:`collections.abc.AsyncIterator`]
        The iterator to chunk, can be sync or async.
    max_size: :class:`int`
        The maximum chunk size.


    .. warning::

        The last chunk collected may not be as large as ``max_size``.

    Returns
    -------
    Union[:class:`Iterator`, :class:`AsyncIterator`]
        A new iterator which yields chunks of a given size.
    """
    ...

def flatten_literal_params(parameters: Iterable[Any]) -> Tuple[Any, ...]:
    ...

def normalise_optional_params(parameters: Iterable[Any]) -> Tuple[Any, ...]:
    ...

def evaluate_annotation(tp: Any, globals: Dict[str, Any], locals: Dict[str, Any], cache: Dict[str, Any], *, implicit_str: bool = ...) -> Any:
    ...

def resolve_annotation(annotation: Any, globalns: Dict[str, Any], localns: Optional[Dict[str, Any]], cache: Optional[Dict[str, Any]]) -> Any:
    ...

TimestampStyle = Literal["f", "F", "d", "D", "t", "T", "R"]
def format_dt(dt: datetime.datetime, /, style: Optional[TimestampStyle] = ...) -> str:
    """A helper function to format a :class:`datetime.datetime` for presentation within Discord.

    This allows for a locale-independent way of presenting data using Discord specific Markdown.

    +-------------+----------------------------+-----------------+
    |    Style    |       Example Output       |   Description   |
    +=============+============================+=================+
    | t           | 22:57                      | Short Time      |
    +-------------+----------------------------+-----------------+
    | T           | 22:57:58                   | Long Time       |
    +-------------+----------------------------+-----------------+
    | d           | 17/05/2016                 | Short Date      |
    +-------------+----------------------------+-----------------+
    | D           | 17 May 2016                | Long Date       |
    +-------------+----------------------------+-----------------+
    | f (default) | 17 May 2016 22:57          | Short Date Time |
    +-------------+----------------------------+-----------------+
    | F           | Tuesday, 17 May 2016 22:57 | Long Date Time  |
    +-------------+----------------------------+-----------------+
    | R           | 5 years ago                | Relative Time   |
    +-------------+----------------------------+-----------------+

    Note that the exact output depends on the user's locale setting in the client. The example output
    presented is using the ``en-GB`` locale.

    .. versionadded:: 2.0

    Parameters
    ----------
    dt: :class:`datetime.datetime`
        The datetime to format.
    style: :class:`str`
        The style to format the datetime with.

    Returns
    -------
    :class:`str`
        The formatted string.
    """
    ...

_FUNCTION_DESCRIPTION_REGEX = ...
_ARG_NAME_SUBREGEX = ...
_ARG_DESCRIPTION_SUBREGEX = ...
_ARG_TYPE_SUBREGEX = ...
_GOOGLE_DOCSTRING_ARG_REGEX = ...
_SPHINX_DOCSTRING_ARG_REGEX = ...
_NUMPY_DOCSTRING_ARG_REGEX = ...
def parse_docstring(func: Callable[..., Any], max_chars: int = ...) -> Dict[str, Any]:
    """Parses the docstring of a function into a dictionary.

    Parameters
    ----------
    func: :data:`~typing.Callable`
        The function to parse the docstring of.
    max_chars: :class:`int`
        The maximum number of characters to allow in the descriptions.
        If MISSING, then there is no maximum.

    Returns
    -------
    :class:`Dict[str, Any]`
        The parsed docstring including the function description and
        descriptions of arguments.
    """
    ...
