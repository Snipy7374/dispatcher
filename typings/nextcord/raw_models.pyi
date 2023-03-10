"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from .partial_emoji import PartialEmoji
from .types.raw_models import BulkMessageDeleteEvent, IntegrationDeleteEvent, MemberRemoveEvent, MessageDeleteEvent, MessageUpdateEvent, ReactionActionEvent, ReactionClearEmojiEvent, ReactionClearEvent, TypingEvent

if TYPE_CHECKING:
    ...
__all__ = ("RawMessageDeleteEvent", "RawBulkMessageDeleteEvent", "RawMessageUpdateEvent", "RawReactionActionEvent", "RawReactionClearEvent", "RawReactionClearEmojiEvent", "RawIntegrationDeleteEvent", "RawTypingEvent", "RawMemberRemoveEvent")
class _RawReprMixin:
    __slots__: tuple[str, ...] = ...
    def __repr__(self) -> str:
        ...
    


class RawMessageDeleteEvent(_RawReprMixin):
    """Represents the event payload for a :func:`on_raw_message_delete` event.

    Attributes
    ----------
    channel_id: :class:`int`
        The channel ID where the deletion took place.
    guild_id: Optional[:class:`int`]
        The guild ID where the deletion took place, if applicable.
    message_id: :class:`int`
        The message ID that got deleted.
    cached_message: Optional[:class:`Message`]
        The cached message, if found in the internal message cache.
    """
    __slots__ = ...
    def __init__(self, data: MessageDeleteEvent) -> None:
        ...
    


class RawBulkMessageDeleteEvent(_RawReprMixin):
    """Represents the event payload for a :func:`on_raw_bulk_message_delete` event.

    Attributes
    ----------
    message_ids: Set[:class:`int`]
        A :class:`set` of the message IDs that were deleted.
    channel_id: :class:`int`
        The channel ID where the message got deleted.
    guild_id: Optional[:class:`int`]
        The guild ID where the message got deleted, if applicable.
    cached_messages: List[:class:`Message`]
        The cached messages, if found in the internal message cache.
    """
    __slots__ = ...
    def __init__(self, data: BulkMessageDeleteEvent) -> None:
        ...
    


class RawMessageUpdateEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_message_edit` event.

    Attributes
    ----------
    message_id: :class:`int`
        The message ID that got updated.
    channel_id: :class:`int`
        The channel ID where the update took place.

        .. versionadded:: 1.3
    guild_id: Optional[:class:`int`]
        The guild ID where the message got updated, if applicable.

        .. versionadded:: 1.7

    data: :class:`dict`
        The raw data given by the `gateway <https://discord.com/developers/docs/topics/gateway#message-update>`_
    cached_message: Optional[:class:`Message`]
        The cached message, if found in the internal message cache. Represents the message before
        it is modified by the data in :attr:`RawMessageUpdateEvent.data`.
    """
    __slots__ = ...
    def __init__(self, data: MessageUpdateEvent) -> None:
        ...
    


class RawReactionActionEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_reaction_add` or
    :func:`on_raw_reaction_remove` event.

    Attributes
    ----------
    message_id: :class:`int`
        The message ID that got or lost a reaction.
    user_id: :class:`int`
        The user ID who added the reaction or whose reaction was removed.
    channel_id: :class:`int`
        The channel ID where the reaction got added or removed.
    guild_id: Optional[:class:`int`]
        The guild ID where the reaction got added or removed, if applicable.
    emoji: :class:`PartialEmoji`
        The custom or unicode emoji being used.
    member: Optional[:class:`Member`]
        The member who added the reaction. Only available if ``event_type`` is ``REACTION_ADD`` and the reaction is inside a guild.

        .. versionadded:: 1.3

    event_type: :class:`str`
        The event type that triggered this action. Can be
        ``REACTION_ADD`` for reaction addition or
        ``REACTION_REMOVE`` for reaction removal.

        .. versionadded:: 1.3
    """
    __slots__ = ...
    def __init__(self, data: ReactionActionEvent, emoji: PartialEmoji, event_type: str) -> None:
        ...
    


class RawReactionClearEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_reaction_clear` event.

    Attributes
    ----------
    message_id: :class:`int`
        The message ID that got its reactions cleared.
    channel_id: :class:`int`
        The channel ID where the reactions got cleared.
    guild_id: Optional[:class:`int`]
        The guild ID where the reactions got cleared.
    """
    __slots__ = ...
    def __init__(self, data: ReactionClearEvent) -> None:
        ...
    


class RawReactionClearEmojiEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_reaction_clear_emoji` event.

    .. versionadded:: 1.3

    Attributes
    ----------
    message_id: :class:`int`
        The message ID that got its reactions cleared.
    channel_id: :class:`int`
        The channel ID where the reactions got cleared.
    guild_id: Optional[:class:`int`]
        The guild ID where the reactions got cleared.
    emoji: :class:`PartialEmoji`
        The custom or unicode emoji being removed.
    """
    __slots__ = ...
    def __init__(self, data: ReactionClearEmojiEvent, emoji: PartialEmoji) -> None:
        ...
    


class RawIntegrationDeleteEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_integration_delete` event.

    .. versionadded:: 2.0

    Attributes
    ----------
    integration_id: :class:`int`
        The ID of the integration that got deleted.
    application_id: Optional[:class:`int`]
        The ID of the bot/OAuth2 application for this deleted integration.
    guild_id: :class:`int`
        The guild ID where the integration got deleted.
    """
    __slots__ = ...
    def __init__(self, data: IntegrationDeleteEvent) -> None:
        ...
    


class RawTypingEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_typing` event.

    .. versionadded:: 2.0

    Attributes
    ----------
    channel_id: :class:`int`
        The channel ID where the typing originated from.
    user_id: :class:`int`
        The ID of the user that started typing.
    when: :class:`datetime.datetime`
        When the typing started as an aware datetime in UTC.
    guild_id: Optional[:class:`int`]
        The guild ID where the typing originated from, if applicable.
    member: Optional[:class:`Member`]
        The member who started typing. Only available if the member started typing in a guild.
    """
    __slots__ = ...
    def __init__(self, data: TypingEvent) -> None:
        ...
    


class RawMemberRemoveEvent(_RawReprMixin):
    """Represents the payload for a :func:`on_raw_member_remove` event.

    .. versionadded:: 2.0

    Attributes
    ----------
    guild_id: :class:`int`
        The guild ID where the member left from.
    """
    __slots__ = ...
    def __init__(self, data: MemberRemoveEvent) -> None:
        ...
    


