"""
This type stub file was generated by pyright.
"""

import datetime
from typing import Any, Dict, List, Mapping, Optional, Protocol, TYPE_CHECKING, Union
from .colour import Colour
from typing_extensions import Self
from nextcord.types.embed import Embed as EmbedData, EmbedType

if TYPE_CHECKING:
    ...
__all__ = ("Embed", )
EmptyEmbed = ...
class EmbedProxy:
    def __init__(self, layer: Dict[str, Any]) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getattr__(self, _: str) -> None:
        ...
    


if TYPE_CHECKING:
    class _EmbedFooterProxy(Protocol):
        text: Optional[str]
        icon_url: Optional[str]
        ...
    
    
    class _EmbedFieldProxy(Protocol):
        name: Optional[str]
        value: Optional[str]
        inline: bool
        ...
    
    
    class _EmbedMediaProxy(Protocol):
        url: Optional[str]
        proxy_url: Optional[str]
        height: Optional[int]
        width: Optional[int]
        ...
    
    
    class _EmbedVideoProxy(Protocol):
        url: Optional[str]
        height: Optional[int]
        width: Optional[int]
        ...
    
    
    class _EmbedProviderProxy(Protocol):
        name: Optional[str]
        url: Optional[str]
        ...
    
    
    class _EmbedAuthorProxy(Protocol):
        name: Optional[str]
        url: Optional[str]
        icon_url: Optional[str]
        proxy_icon_url: Optional[str]
        ...
    
    
class Embed:
    """Represents a Discord embed.

    .. container:: operations

        .. describe:: len(x)

            Returns the total size of the embed.
            Useful for checking if it's within the 6000 character limit.

        .. describe:: bool(b)

            Returns whether the embed has any data set.

            .. versionadded:: 2.0

    Certain properties return an ``EmbedProxy``, a type
    that acts similar to a regular :class:`dict` except using dotted access,
    e.g. ``embed.author.icon_url``. If the attribute
    is invalid or empty, then ``None`` is returned.

    For ease of use, all parameters that expect a :class:`str` are implicitly
    casted to :class:`str` for you.

    .. versionchanged:: 2.2
        ``Embed.Empty`` is now an alias for ``None`` for a non-breaking change, every field uses ``None``
            and is typed as ``Optional[...]`` over ``Embed.Empty``.
            This also means that you can no longer use ``len()`` on an empty field.

    Attributes
    ----------
    title: :class:`str`
        The title of the embed.
        This can be set during initialisation.
    type: :class:`str`
        The type of embed. Usually "rich".
        This can be set during initialisation.
        Possible strings for embed types can be found on discord's
        `api docs <https://discord.com/developers/docs/resources/channel#embed-object-embed-types>`_
    description: :class:`str`
        The description of the embed.
        This can be set during initialisation.
    url: :class:`str`
        The hyperlink of the embed title.
        This can be set during initialisation.
        This makes no effect if there is no ``title`` field.
    timestamp: :class:`datetime.datetime`
        The timestamp of the embed content. This is an aware datetime.
        If a naive datetime is passed, it is converted to an aware
        datetime with the local timezone.
    colour: Union[:class:`Colour`, :class:`int`]
        The colour code of the embed. Aliased to ``color`` as well.
        This can be set during initialisation.
    """
    __slots__ = ...
    def __init__(self, *, colour: Optional[Union[int, Colour]] = ..., color: Optional[Union[int, Colour]] = ..., title: Optional[Any] = ..., type: EmbedType = ..., url: Optional[Any] = ..., description: Optional[Any] = ..., timestamp: Optional[datetime.datetime] = ...) -> None:
        ...
    
    @property
    def Empty(self) -> None:
        ...
    
    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Self:
        """Converts a :class:`dict` to a :class:`Embed` provided it is in the
        format that Discord expects it to be in.

        You can find out about this format in the `official Discord documentation`__.

        .. _DiscordDocs: https://discord.com/developers/docs/resources/channel#embed-object

        __ DiscordDocs_

        Parameters
        ----------
        data: :class:`dict`
            The dictionary to convert into an embed.
        """
        ...
    
    def copy(self) -> Self:
        """Returns a shallow copy of the embed."""
        ...
    
    def __len__(self) -> int:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    @property
    def colour(self) -> Optional[Colour]:
        ...
    
    @colour.setter
    def colour(self, value: Optional[Union[int, Colour]]): # -> None:
        ...
    
    color = ...
    @property
    def timestamp(self) -> Optional[datetime.datetime]:
        ...
    
    @timestamp.setter
    def timestamp(self, value: Optional[datetime.datetime]): # -> None:
        ...
    
    @property
    def footer(self) -> _EmbedFooterProxy:
        """Returns an ``EmbedProxy`` denoting the footer contents.

        See :meth:`set_footer` for possible values you can access.

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    def set_footer(self, *, text: Optional[Any] = ..., icon_url: Optional[Any] = ...) -> Self:
        """Sets the footer for the embed content.

        This function returns the class instance to allow for fluent-style
        chaining.

        Parameters
        ----------
        text: Optional[:class:`str`]
            The footer text.
        icon_url: Optional[:class:`str`]
            The URL of the footer icon. Only HTTP(S) is supported.
        """
        ...
    
    def remove_footer(self) -> Self:
        """Clears embed's footer information.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. versionadded:: 2.0
        """
        ...
    
    @property
    def image(self) -> _EmbedMediaProxy:
        """Returns an ``EmbedProxy`` denoting the image contents.

        Possible attributes you can access are:

        - ``url``
        - ``proxy_url``
        - ``width``
        - ``height``

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    def set_image(self, url: Optional[Any]) -> Self:
        """Sets the image for the embed content.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. versionchanged:: 1.4
            Passing ``None`` removes the image.

        Parameters
        ----------
        url: Optional[:class:`str`]
            The source URL for the image. Only HTTP(S) is supported.
        """
        ...
    
    @property
    def thumbnail(self) -> _EmbedMediaProxy:
        """Returns an ``EmbedProxy`` denoting the thumbnail contents.

        Possible attributes you can access are:

        - ``url``
        - ``proxy_url``
        - ``width``
        - ``height``

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    def set_thumbnail(self, url: Optional[Any]) -> Self:
        """Sets the thumbnail for the embed content.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. versionchanged:: 1.4
            Passing ``None`` removes the thumbnail.

        Parameters
        ----------
        url: :class:`str`
            The source URL for the thumbnail. Only HTTP(S) is supported.
        """
        ...
    
    @property
    def video(self) -> _EmbedVideoProxy:
        """Returns an ``EmbedProxy`` denoting the video contents.

        Possible attributes include:

        - ``url`` for the video URL.
        - ``height`` for the video height.
        - ``width`` for the video width.

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    @property
    def provider(self) -> _EmbedProviderProxy:
        """Returns an ``EmbedProxy`` denoting the provider contents.

        The only attributes that might be accessed are ``name`` and ``url``.

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    @property
    def author(self) -> _EmbedAuthorProxy:
        """Returns an ``EmbedProxy`` denoting the author contents.

        See :meth:`set_author` for possible values you can access.

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    def set_author(self, *, name: Any, url: Optional[Any] = ..., icon_url: Optional[Any] = ...) -> Self:
        """Sets the author for the embed content.

        This function returns the class instance to allow for fluent-style
        chaining.

        Parameters
        ----------
        name: Optional[:class:`str`]
            The name of the author.
        url: Optional[:class:`str`]
            The URL for the author.
        icon_url: Optional[:class:`str`]
            The URL of the author icon. Only HTTP(S) is supported.
        """
        ...
    
    def remove_author(self) -> Self:
        """Clears embed's author information.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. versionadded:: 1.4
        """
        ...
    
    @property
    def fields(self) -> List[_EmbedFieldProxy]:
        """List[Optional[``EmbedProxy``]]: Returns a :class:`list` of ``EmbedProxy`` denoting the field contents.

        See :meth:`add_field` for possible values you can access.

        If the attribute has no value then ``None`` is returned.
        """
        ...
    
    def add_field(self, *, name: Any, value: Any, inline: bool = ...) -> Self:
        """Adds a field to the embed object.

        This function returns the class instance to allow for fluent-style
        chaining.

        Parameters
        ----------
        name: :class:`str`
            The name of the field.
        value: :class:`str`
            The value of the field.
        inline: :class:`bool`
            Whether the field should be displayed inline. Defaults to ``True``.
        """
        ...
    
    def insert_field_at(self, index: int, *, name: Any, value: Any, inline: bool = ...) -> Self:
        """Inserts a field before a specified index to the embed.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. versionadded:: 1.2

        Parameters
        ----------
        index: :class:`int`
            The index of where to insert the field.
        name: :class:`str`
            The name of the field.
        value: :class:`str`
            The value of the field.
        inline: :class:`bool`
            Whether the field should be displayed inline. Defaults to ``True``.
        """
        ...
    
    def clear_fields(self) -> Self:
        """Removes all fields from this embed.

        This function returns the class instance to allow for fluent-style
        chaining.
        """
        ...
    
    def remove_field(self, index: int) -> Self:
        """Removes a field at a specified index.

        If the index is invalid or out of bounds then the error is
        silently swallowed.

        This function returns the class instance to allow for fluent-style
        chaining.

        .. note::

            When deleting a field by index, the index of the other fields
            shift to fill the gap just like a regular list.

        Parameters
        ----------
        index: :class:`int`
            The index of the field to remove.
        """
        ...
    
    def set_field_at(self, index: int, *, name: Any, value: Any, inline: bool = ...) -> Self:
        """Modifies a field to the embed object.

        The index must point to a valid pre-existing field.

        This function returns the class instance to allow for fluent-style
        chaining.

        Parameters
        ----------
        index: :class:`int`
            The index of the field to modify.
        name: :class:`str`
            The name of the field.
        value: :class:`str`
            The value of the field.
        inline: :class:`bool`
            Whether the field should be displayed inline.

        Raises
        ------
        IndexError
            An invalid index was provided.
        """
        ...
    
    def to_dict(self) -> EmbedData:
        """Converts this embed object into a dict."""
        ...
    

