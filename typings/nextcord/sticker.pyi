"""
This type stub file was generated by pyright.
"""

import datetime
from typing import Optional, TYPE_CHECKING, Union
from .asset import Asset, AssetMixin
from .enums import StickerFormatType
from .mixins import Hashable
from .utils import cached_slot_property
from .guild import Guild
from .state import ConnectionState
from .types.sticker import Sticker as StickerPayload, StickerItem as StickerItemPayload, StickerPack as StickerPackPayload

__all__ = ("StickerPack", "StickerItem", "Sticker", "StandardSticker", "GuildSticker")
if TYPE_CHECKING:
    ...
class StickerPack(Hashable):
    """Represents a sticker pack.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the sticker pack.

        .. describe:: x == y

           Checks if the sticker pack is equal to another sticker pack.

        .. describe:: x != y

           Checks if the sticker pack is not equal to another sticker pack.

    Attributes
    ----------
    name: :class:`str`
        The name of the sticker pack.
    description: :class:`str`
        The description of the sticker pack.
    id: :class:`int`
        The id of the sticker pack.
    stickers: List[:class:`StandardSticker`]
        The stickers of this sticker pack.
    sku_id: :class:`int`
        The SKU ID of the sticker pack.
    cover_sticker_id: :class:`int`
         The ID of the sticker used for the cover of the sticker pack.
    cover_sticker: :class:`StandardSticker`
        The sticker used for the cover of the sticker pack.
    """
    __slots__ = ...
    def __init__(self, *, state: ConnectionState, data: StickerPackPayload) -> None:
        ...
    
    @property
    def banner(self) -> Asset:
        """:class:`Asset`: The banner asset of the sticker pack."""
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    


class _StickerTag(Hashable, AssetMixin):
    __slots__ = ...
    id: int
    format: StickerFormatType
    async def read(self) -> bytes:
        """|coro|

        Retrieves the content of this sticker as a :class:`bytes` object.

        .. note::

            Stickers that use the :attr:`StickerFormatType.lottie` format cannot be read.

        Raises
        ------
        HTTPException
            Downloading the asset failed.
        NotFound
            The asset was deleted.
        TypeError
            The sticker is a lottie type.

        Returns
        -------
        :class:`bytes`
            The content of the asset.
        """
        ...
    


class StickerItem(_StickerTag):
    """Represents a sticker item.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the sticker item.

        .. describe:: x == y

           Checks if the sticker item is equal to another sticker item.

        .. describe:: x != y

           Checks if the sticker item is not equal to another sticker item.

    Attributes
    ----------
    name: :class:`str`
        The sticker's name.
    id: :class:`int`
        The id of the sticker.
    format: :class:`StickerFormatType`
        The format for the sticker's image.
    url: :class:`str`
        The URL for the sticker's image.
    """
    __slots__ = ...
    def __init__(self, *, state: ConnectionState, data: StickerItemPayload) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    async def fetch(self) -> Union[Sticker, StandardSticker, GuildSticker]:
        """|coro|

        Attempts to retrieve the full sticker data of the sticker item.

        Raises
        ------
        HTTPException
            Retrieving the sticker failed.

        Returns
        -------
        Union[:class:`StandardSticker`, :class:`GuildSticker`]
            The retrieved sticker.
        """
        ...
    


class Sticker(_StickerTag):
    """Represents a sticker.

    .. versionadded:: 1.6

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the sticker.

        .. describe:: x == y

           Checks if the sticker is equal to another sticker.

        .. describe:: x != y

           Checks if the sticker is not equal to another sticker.

    Attributes
    ----------
    name: :class:`str`
        The sticker's name.
    id: :class:`int`
        The id of the sticker.
    description: :class:`str`
        The description of the sticker.
    pack_id: :class:`int`
        The id of the sticker's pack.
    format: :class:`StickerFormatType`
        The format for the sticker's image.
    url: :class:`str`
        The URL for the sticker's image.
    """
    __slots__ = ...
    def __init__(self, *, state: ConnectionState, data: StickerPayload) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns the sticker's creation time in UTC."""
        ...
    


class StandardSticker(Sticker):
    """Represents a sticker that is found in a standard sticker pack.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the sticker.

        .. describe:: x == y

           Checks if the sticker is equal to another sticker.

        .. describe:: x != y

           Checks if the sticker is not equal to another sticker.

    Attributes
    ----------
    name: :class:`str`
        The sticker's name.
    id: :class:`int`
        The id of the sticker.
    description: :class:`str`
        The description of the sticker.
    pack_id: :class:`int`
        The id of the sticker's pack.
    format: :class:`StickerFormatType`
        The format for the sticker's image.
    tags: List[:class:`str`]
        A list of tags for the sticker.
    sort_value: :class:`int`
        The sticker's sort order within its pack.
    """
    __slots__ = ...
    def __repr__(self) -> str:
        ...
    
    async def pack(self) -> StickerPack:
        """|coro|

        Retrieves the sticker pack that this sticker belongs to.

        Raises
        ------
        InvalidData
            The corresponding sticker pack was not found.
        HTTPException
            Retrieving the sticker pack failed.

        Returns
        -------
        :class:`StickerPack`
            The retrieved sticker pack.
        """
        ...
    


class GuildSticker(Sticker):
    """Represents a sticker that belongs to a guild.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the sticker.

        .. describe:: x == y

           Checks if the sticker is equal to another sticker.

        .. describe:: x != y

           Checks if the sticker is not equal to another sticker.

    Attributes
    ----------
    name: :class:`str`
        The sticker's name.
    id: :class:`int`
        The id of the sticker.
    description: :class:`str`
        The description of the sticker.
    format: :class:`StickerFormatType`
        The format for the sticker's image.
    available: :class:`bool`
        Whether this sticker is available for use.
    guild_id: :class:`int`
        The ID of the guild that this sticker is from.
    user: Optional[:class:`User`]
        The user that created this sticker. This can only be retrieved using :meth:`Guild.fetch_sticker` and
        having the :attr:`~Permissions.manage_emojis_and_stickers` permission.
    emoji: :class:`str`
        The name of a unicode emoji that represents this sticker.
    """
    __slots__ = ...
    def __repr__(self) -> str:
        ...
    
    @cached_slot_property("_cs_guild")
    def guild(self) -> Optional[Guild]:
        """Optional[:class:`Guild`]: The guild that this sticker is from.
        Could be ``None`` if the bot is not in the guild.

        .. versionadded:: 2.0
        """
        ...
    
    async def edit(self, *, name: str = ..., description: str = ..., emoji: str = ..., reason: Optional[str] = ...) -> GuildSticker:
        """|coro|

        Edits a :class:`GuildSticker` for the guild.

        Parameters
        ----------
        name: :class:`str`
            The sticker's new name. Must be at least 2 characters.
        description: Optional[:class:`str`]
            The sticker's new description. Can be ``None``.
        emoji: :class:`str`
            The name of a unicode emoji that represents the sticker's expression.
        reason: :class:`str`
            The reason for editing this sticker. Shows up on the audit log.

        Raises
        ------
        Forbidden
            You are not allowed to edit stickers.
        HTTPException
            An error occurred editing the sticker.

        Returns
        -------
        :class:`GuildSticker`
            The newly modified sticker.
        """
        ...
    
    async def delete(self, *, reason: Optional[str] = ...) -> None:
        """|coro|

        Deletes the custom :class:`Sticker` from the guild.

        You must have :attr:`~Permissions.manage_emojis_and_stickers` permission to
        do this.

        Parameters
        ----------
        reason: Optional[:class:`str`]
            The reason for deleting this sticker. Shows up on the audit log.

        Raises
        ------
        Forbidden
            You are not allowed to delete stickers.
        HTTPException
            An error occurred deleting the sticker.
        """
        ...
    

