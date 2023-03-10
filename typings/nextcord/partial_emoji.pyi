"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Optional, TYPE_CHECKING, Union
from .asset import AssetMixin
from datetime import datetime
from typing_extensions import Self
from .state import ConnectionState
from .types.emoji import DefaultReaction
from .types.message import PartialEmoji as PartialEmojiPayload

__all__ = ("PartialEmoji", )
if TYPE_CHECKING:
    ...
class _EmojiTag:
    __slots__ = ...
    id: int


class PartialEmoji(_EmojiTag, AssetMixin):
    """Represents a "partial" emoji.

    This model will be given in two scenarios:

    - "Raw" data events such as :func:`on_raw_reaction_add`
    - Custom emoji that the bot cannot see from e.g. :attr:`Message.reactions`

    .. container:: operations

        .. describe:: x == y

            Checks if two emoji are the same.

        .. describe:: x != y

            Checks if two emoji are not the same.

        .. describe:: hash(x)

            Return the emoji's hash.

        .. describe:: str(x)

            Returns the emoji rendered for discord.

    Attributes
    ----------
    name: Optional[:class:`str`]
        The custom emoji name, if applicable, or the unicode codepoint
        of the non-custom emoji. This can be ``None`` if the emoji
        got deleted (e.g. removing a reaction with a deleted emoji).
    animated: :class:`bool`
        Whether the emoji is animated or not.
    id: Optional[:class:`int`]
        The ID of the custom emoji, if applicable.
    """
    __slots__ = ...
    _CUSTOM_EMOJI_RE = ...
    if TYPE_CHECKING:
        id: Optional[int]
        ...
    def __init__(self, *, name: str, animated: bool = ..., id: Optional[int] = ...) -> None:
        ...
    
    @classmethod
    def from_dict(cls, data: Union[PartialEmojiPayload, Dict[str, Any]]) -> Self:
        ...
    
    @classmethod
    def from_default_reaction(cls, data: DefaultReaction) -> Self:
        ...
    
    @classmethod
    def from_str(cls, value: str) -> Self:
        """Converts a Discord string representation of an emoji to a :class:`PartialEmoji`.

        The formats accepted are:

        - ``a:name:id``
        - ``<a:name:id>``
        - ``name:id``
        - ``<:name:id>``

        If the format does not match then it is assumed to be a unicode emoji.

        .. versionadded:: 2.0

        Parameters
        ----------
        value: :class:`str`
            The string representation of an emoji.

        Returns
        -------
        :class:`PartialEmoji`
            The partial emoji from this string.
        """
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        ...
    
    @classmethod
    def with_state(cls, state: ConnectionState, *, name: str, animated: bool = ..., id: Optional[int] = ...) -> Self:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __ne__(self, other: Any) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def is_custom_emoji(self) -> bool:
        """:class:`bool`: Checks if this is a custom non-Unicode emoji."""
        ...
    
    def is_unicode_emoji(self) -> bool:
        """:class:`bool`: Checks if this is a Unicode emoji."""
        ...
    
    @property
    def created_at(self) -> Optional[datetime]:
        """Optional[:class:`datetime.datetime`]: Returns the emoji's creation time in UTC, or None if Unicode emoji.

        .. versionadded:: 1.6
        """
        ...
    
    @property
    def url(self) -> str:
        """:class:`str`: Returns the URL of the emoji, if it is custom.

        If this isn't a custom emoji then an empty string is returned
        """
        ...
    
    async def read(self) -> bytes:
        ...
    

