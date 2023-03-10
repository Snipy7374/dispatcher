"""
This type stub file was generated by pyright.
"""

from typing import Any, List, Optional, TYPE_CHECKING, Tuple, Union
from .abc import GuildChannel, Snowflake
from .asset import Asset
from .enums import ScheduledEventEntityType, ScheduledEventPrivacyLevel, ScheduledEventStatus
from .iterators import ScheduledEventUserIterator
from .mixins import Hashable
from datetime import datetime
from .file import File
from .guild import Guild
from .message import Attachment
from .state import ConnectionState
from .types.scheduled_events import ScheduledEvent as ScheduledEventPayload, ScheduledEventUser as ScheduledEventUserPayload

__all__: Tuple[str, ...] = ...
if TYPE_CHECKING:
    ...
class EntityMetadata:
    """Represents the metadata for an event

    Parameters
    ----------
    location : Optional[str]
        The location of the event, defaults to None
    """
    def __init__(self, *, location: Optional[str] = ..., **kwargs: Any) -> None:
        ...
    


class ScheduledEventUser(Hashable):
    """Represents a user in a scheduled event

    Attributes
    ----------
    event: :class:`ScheduledEvent`
        The event the user is interested in.
    user: Optional[:class:`User`]
        The related user object. Blank if no member intents
    member: Optional[:class:`Member`]
        The related member object, if requested with
        :meth:`ScheduledEvent.fetch_users`.
    user_id: int
        The id of the interested user


    .. warning::

        user or member may be ``None``, this may occur if you don't have
        :attr:`Intents.members` enabled.
    """
    __slots__: Tuple[str, ...] = ...
    def __init__(self, *, update: bool = ..., event: ScheduledEvent, state: ConnectionState, data: Optional[ScheduledEventUserPayload] = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @classmethod
    def from_id(cls, *, event: ScheduledEvent, state: ConnectionState, user_id: int) -> ScheduledEventUser:
        ...
    


class ScheduledEvent(Hashable):
    """Represents a Discord scheduled event

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: x == y

            Checks if two events are equal.

        .. describe:: x != y

            Checks if two events are not equal.

        .. describe:: hash(x)

            Returns the event's hash.

        .. describe:: str(x)

            Returns the event's name.

    Attributes
    ----------
    channel: Optional[:class:`abc.GuildChannel`]
        The channel the event will take place, if any.
    channel_id: Optional[:class:`int`]
        The channel id where the event will take place, if any.
    creator: Optional[:class:`User`]
        The user who created the event, if cached.
    description: :class:`str`
        The description of the event.
    end_time: :class:`datetime.datetime`
        The scheduled end time for the event, if set.
    guild: :class:`Guild`
        The guild the event will be in.
    id: :class:`int`
        The snowflake id for the event.
    metadata: Optional[:class:`EntityMetadata`]
        The metadata for the event, if any.
    name: :class:`str`
        The name of the event.
    privacy_level: :class:`ScheduledEventPrivacyLevel`
        The privacy level for the event.
    start_time: :class:`datetime.datetime`
        The scheduled start time for the event.
    user_count: :class:`int`
        An approximate count of the 'interested' users.
    image: :class:`Asset`
        The event cover image.
    """
    __slots__: Tuple[str, ...] = ...
    def __init__(self, *, guild: Guild, state: ConnectionState, data: ScheduledEventPayload) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def location(self) -> Optional[str]:
        """Optional[:class:`str`]: The location of the event, if any."""
        ...
    
    @property
    def users(self) -> List[ScheduledEventUser]:
        """List[:class:`ScheduledEventUser`]: The users who are interested in the event.

        .. note::
            This may not be accurate or populated until
            :meth:`~.ScheduledEvent.fetch_users` is called
        """
        ...
    
    async def delete(self) -> None:
        """|coro|

        Delete the scheduled event.
        """
        ...
    
    async def edit(self, *, channel: GuildChannel = ..., metadata: EntityMetadata = ..., name: str = ..., privacy_level: ScheduledEventPrivacyLevel = ..., start_time: datetime = ..., end_time: datetime = ..., description: str = ..., type: ScheduledEventEntityType = ..., status: ScheduledEventStatus = ..., reason: Optional[str] = ..., image: Optional[Union[bytes, Asset, Attachment, File]] = ...) -> ScheduledEvent:
        """|coro|

        Edit the scheduled event.

        .. versionchanged:: 2.1
            The ``image`` parameter now accepts :class:`File`, :class:`Attachment`, and :class:`Asset`.

        Parameters
        ----------
        channel: :class:`abc.GuildChannel`
            The new channel for the event.
        metadata: :class:`EntityMetadata`
            The new metadata for the event.
        name: :class:`str`
            The new name for the event.
        privacy_level: :class:`ScheduledEventPrivacyLevel`
            The new privacy level for the event.
        start_time: :class:`py:datetime.datetime`
            The new scheduled start time.
        end_time: :class:`py:datetime.datetime`
            The new scheduled end time.
        description: :class:`str`
            The new description for the event.
        type: :class:`ScheduledEventEntityType`
            The new type for the event.
        status: :class:`ScheduledEventStatus`
            The new status for the event.
        reason: Optional[:class:`str`]
            The reason for editing this scheduled event. Shows up in the audit logs.

            .. note::

                Only the following edits to an event's status are permitted:
                scheduled -> active ;
                active -> completed ;
                scheduled -> canceled
        image: Optional[Union[:class:`bytes`, :class:`Asset`, :class:`Attachment`, :class:`File`]]
            A :term:`py:bytes-like object`, :class:`File`, :class:`Attachment`, or :class:`Asset`
            representing the cover image. Could be ``None`` to denote removal of the cover image.

        Returns
        -------
        :class:`ScheduledEvent`
            The updated event object.
        """
        ...
    
    def get_user(self, user_id: int) -> Optional[ScheduledEventUser]:
        """Get a user that is interested.

        .. note::

            This may not be accurate or populated until
            :meth:`ScheduledEvent.fetch_users` is called.

        Parameters
        ----------
        user_id: :class:`int`
            The user id to get from cache.

        Returns
        -------
        Optional[:class:`ScheduledEventUser`]
            The user object, if found.
        """
        ...
    
    def fetch_users(self, *, limit: int = ..., with_member: bool = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> ScheduledEventUserIterator:
        """Fetch the users that are interested, returns an asyc iterator.

        Parameters
        ----------
        limit: :class:`int`
            Amount of users to fetch, by default 100
        with_member: :class:`bool`
            If the user objects should contain members too, by default False
        before: Optional[:class:`int`]
            A snowflake id to start with, useful for chunks of users, by default None
        after: Optional[:class:`int`]
            A snowflake id to end with, useful for chunks of usersby default None

        Yields
        ------
        :class:`ScheduledEventUser`
            A full event user object
        """
        ...
    

