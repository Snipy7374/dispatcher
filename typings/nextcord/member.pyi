"""
This type stub file was generated by pyright.
"""

import datetime
from typing import Any, List, Literal, Optional, TYPE_CHECKING, Union
from . import abc
from .activity import ActivityTypes
from .asset import Asset
from .colour import Colour
from .enums import Status
from .permissions import Permissions
from .user import _UserTag
from .abc import Snowflake
from .channel import DMChannel, StageChannel, VoiceChannel
from .flags import PublicUserFlags
from .guild import Guild
from .message import Message
from .role import Role
from .state import ConnectionState
from .types.member import MemberWithUser as MemberWithUserPayload
from .types.voice import VoiceState as VoiceStatePayload

__all__ = ("VoiceState", "Member")
if TYPE_CHECKING:
    VocalGuildChannel = Union[VoiceChannel, StageChannel]
class VoiceState:
    """Represents a Discord user's voice state.

    Attributes
    ----------
    deaf: :class:`bool`
        Indicates if the user is currently deafened by the guild.
    mute: :class:`bool`
        Indicates if the user is currently muted by the guild.
    self_mute: :class:`bool`
        Indicates if the user is currently muted by their own accord.
    self_deaf: :class:`bool`
        Indicates if the user is currently deafened by their own accord.
    self_stream: :class:`bool`
        Indicates if the user is currently streaming via 'Go Live' feature.

        .. versionadded:: 1.3

    self_video: :class:`bool`
        Indicates if the user is currently broadcasting video.
    suppress: :class:`bool`
        Indicates if the user is suppressed from speaking.

        Only applies to stage channels.

        .. versionadded:: 1.7

    requested_to_speak_at: Optional[:class:`datetime.datetime`]
        An aware datetime object that specifies the date and time in UTC that the member
        requested to speak. It will be ``None`` if they are not requesting to speak
        anymore or have been accepted to speak.

        Only applicable to stage channels.

        .. versionadded:: 1.7

    afk: :class:`bool`
        Indicates if the user is currently in the AFK channel in the guild.
    channel: Optional[Union[:class:`VoiceChannel`, :class:`StageChannel`]]
        The voice channel that the user is currently connected to. ``None`` if the user
        is not currently in a voice channel.
    """
    __slots__ = ...
    def __init__(self, *, data: VoiceStatePayload, channel: Optional[VocalGuildChannel] = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


def flatten_user(cls):
    ...

@flatten_user
class Member(abc.Messageable, _UserTag):
    """Represents a Discord member to a :class:`Guild`.

    This implements a lot of the functionality of :class:`User`.

    .. container:: operations

        .. describe:: x == y

            Checks if two members are equal.
            Note that this works with :class:`User` instances too.

        .. describe:: x != y

            Checks if two members are not equal.
            Note that this works with :class:`User` instances too.

        .. describe:: hash(x)

            Returns the member's hash.

        .. describe:: str(x)

            Returns the member's name with the discriminator.

    Attributes
    ----------
    joined_at: Optional[:class:`datetime.datetime`]
        An aware datetime object that specifies the date and time in UTC that the member joined the guild.
        If the member left and rejoined the guild, this will be the latest date. In certain cases, this can be ``None``.
    activities: Tuple[Union[:class:`BaseActivity`, :class:`Spotify`]]
        The activities that the user is currently doing.

        .. note::

            Due to a Discord API limitation, a user's Spotify activity may not appear
            if they are listening to a song with a title longer
            than 128 characters. See :dpyissue:`1738` for more information.

    guild: :class:`Guild`
        The guild that the member belongs to.
    nick: Optional[:class:`str`]
        The guild specific nickname of the user.
    pending: :class:`bool`
        Whether the member is pending member verification.

        .. versionadded:: 1.6
    premium_since: Optional[:class:`datetime.datetime`]
        An aware datetime object that specifies the date and time in UTC when the member used their
        "Nitro boost" on the guild, if available. This could be ``None``.
    """
    __slots__ = ...
    if TYPE_CHECKING:
        name: str
        id: int
        discriminator: str
        bot: bool
        system: bool
        created_at: datetime.datetime
        default_avatar: Asset
        avatar: Optional[Asset]
        dm_channel: Optional[DMChannel]
        create_dm = ...
        mutual_guilds: List[Guild]
        public_flags: PublicUserFlags
        banner: Optional[Asset]
        accent_color: Optional[Colour]
        accent_colour: Optional[Colour]
    def __init__(self, *, data: MemberWithUserPayload, guild: Guild, state: ConnectionState) -> None:
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
    
    @property
    def status(self) -> Union[Status, str]:
        """Union[:class:`Status`, :class:`str`]: The member's overall status. If the value is unknown, then it will be a :class:`str` instead."""
        ...
    
    @property
    def raw_status(self) -> str:
        """:class:`str`: The member's overall status as a string value.

        .. versionadded:: 1.5
        """
        ...
    
    @status.setter
    def status(self, value: Status) -> None:
        ...
    
    @property
    def mobile_status(self) -> Status:
        """:class:`Status`: The member's status on a mobile device, if applicable."""
        ...
    
    @property
    def desktop_status(self) -> Status:
        """:class:`Status`: The member's status on the desktop client, if applicable."""
        ...
    
    @property
    def web_status(self) -> Status:
        """:class:`Status`: The member's status on the web client, if applicable."""
        ...
    
    def is_on_mobile(self) -> bool:
        """:class:`bool`: A helper function that determines if a member is active on a mobile device."""
        ...
    
    @property
    def colour(self) -> Colour:
        """:class:`Colour`: A property that returns a colour denoting the rendered colour
        for the member. If the default colour is the one rendered then an instance
        of :meth:`Colour.default` is returned.

        There is an alias for this named :attr:`color`.
        """
        ...
    
    @property
    def color(self) -> Colour:
        """:class:`Colour`: A property that returns a color denoting the rendered color for
        the member. If the default color is the one rendered then an instance of :meth:`Colour.default`
        is returned.

        There is an alias for this named :attr:`colour`.
        """
        ...
    
    @property
    def roles(self) -> List[Role]:
        """List[:class:`Role`]: A :class:`list` of :class:`Role` that the member belongs to. Note
        that the first element of this list is always the default '@everyone'
        role.

        These roles are sorted by their position in the role hierarchy.
        """
        ...
    
    @property
    def mention(self) -> str:
        """:class:`str`: Returns a string that allows you to mention the member.

        .. versionchanged:: 2.2
            The nickname mention syntax is no longer returned as it is deprecated by Discord.
        """
        ...
    
    @property
    def display_name(self) -> str:
        """:class:`str`: Returns the user's display name.

        For regular users this is just their username, but
        if they have a guild specific nickname then that
        is returned instead.
        """
        ...
    
    @property
    def display_avatar(self) -> Asset:
        """:class:`Asset`: Returns the member's display avatar.

        For regular members this is just their avatar, but
        if they have a guild specific avatar then that
        is returned instead.

        .. versionadded:: 2.0
        """
        ...
    
    @property
    def guild_avatar(self) -> Optional[Asset]:
        """Optional[:class:`Asset`]: Returns an :class:`Asset` for the guild avatar
        the member has. If unavailable, ``None`` is returned.

        .. versionadded:: 2.0
        """
        ...
    
    @property
    def activity(self) -> Optional[ActivityTypes]:
        """Optional[Union[:class:`BaseActivity`, :class:`Spotify`]]: Returns the primary
        activity the user is currently doing. Could be ``None`` if no activity is being done.

        .. note::

            Due to a Discord API limitation, this may be ``None`` if
            the user is listening to a song on Spotify with a title longer
            than 128 characters. See :dpyissue:`1738` for more information.

        .. note::

            A user may have multiple activities, these can be accessed under :attr:`activities`.
        """
        ...
    
    def mentioned_in(self, message: Message) -> bool:
        """Checks if the member is mentioned in the specified message.

        Parameters
        ----------
        message: :class:`Message`
            The message to check if you're mentioned in.

        Returns
        -------
        :class:`bool`
            Indicates if the member is mentioned in the message.
        """
        ...
    
    @property
    def top_role(self) -> Role:
        """:class:`Role`: Returns the member's highest role.

        This is useful for figuring where a member stands in the role
        hierarchy chain.
        """
        ...
    
    @property
    def guild_permissions(self) -> Permissions:
        """:class:`Permissions`: Returns the member's guild permissions.

        This only takes into consideration the guild permissions
        and not most of the implied permissions or any of the
        channel permission overwrites. For 100% accurate permission
        calculation, please use :meth:`abc.GuildChannel.permissions_for`.

        This does take into consideration guild ownership and the
        administrator implication.
        """
        ...
    
    @property
    def voice(self) -> Optional[VoiceState]:
        """Optional[:class:`VoiceState`]: Returns the member's current voice state."""
        ...
    
    @property
    def communication_disabled_until(self) -> Optional[datetime.datetime]:
        """Optional[:class:`datetime.datetime`]: A datetime object that represents
        the time in which the member will be able to interact again.

        .. note::

            This is ``None`` if the user has no timeout.

        .. versionadded:: 2.0
        """
        ...
    
    async def ban(self, *, delete_message_seconds: Optional[int] = ..., delete_message_days: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7]] = ..., reason: Optional[str] = ...) -> None:
        """|coro|

        Bans this member. Equivalent to :meth:`Guild.ban`.
        """
        ...
    
    async def unban(self, *, reason: Optional[str] = ...) -> None:
        """|coro|

        Unbans this member. Equivalent to :meth:`Guild.unban`.
        """
        ...
    
    async def kick(self, *, reason: Optional[str] = ...) -> None:
        """|coro|

        Kicks this member. Equivalent to :meth:`Guild.kick`.
        """
        ...
    
    async def timeout(self, timeout: Union[datetime.datetime, datetime.timedelta], *, reason: Optional[str] = ...) -> None:
        """|coro|

        Times out this member.

        .. note::

            This is a more direct method of timing out a member.
            You can also time out members using :meth:`Member.edit`.

        .. versionadded:: 2.0

        Parameters
        ----------
        timeout: Optional[Union[:class:`~datetime.datetime`, :class:`~datetime.timedelta`]]
            The time until the member should not be timed out.
            Set this to None to disable their timeout.
        reason: Optional[:class:`str`]
            The reason for editing this member. Shows up on the audit log.
        """
        ...
    
    async def edit(self, *, nick: Optional[str] = ..., mute: bool = ..., deafen: bool = ..., suppress: bool = ..., roles: List[abc.Snowflake] = ..., voice_channel: Optional[VocalGuildChannel] = ..., reason: Optional[str] = ..., timeout: Optional[Union[datetime.datetime, datetime.timedelta]] = ...) -> Optional[Member]:
        """|coro|

        Edits the member's data.

        Depending on the parameter passed, this requires different permissions listed below:

        +---------------+--------------------------------------+
        |   Parameter   |              Permission              |
        +---------------+--------------------------------------+
        | nick          | :attr:`Permissions.manage_nicknames` |
        +---------------+--------------------------------------+
        | mute          | :attr:`Permissions.mute_members`     |
        +---------------+--------------------------------------+
        | deafen        | :attr:`Permissions.deafen_members`   |
        +---------------+--------------------------------------+
        | roles         | :attr:`Permissions.manage_roles`     |
        +---------------+--------------------------------------+
        | voice_channel | :attr:`Permissions.move_members`     |
        +---------------+--------------------------------------+
        | timeout       | :attr:`Permissions.moderate_members` |
        +---------------+--------------------------------------+

        All parameters are optional.

        .. versionchanged:: 1.1
            Can now pass ``None`` to ``voice_channel`` to kick a member from voice.

        .. versionchanged:: 2.0
            The newly member is now optionally returned, if applicable.

        Parameters
        ----------
        nick: Optional[:class:`str`]
            The member's new nickname. Use ``None`` to remove the nickname.
        mute: :class:`bool`
            Indicates if the member should be guild muted or un-muted.
        deafen: :class:`bool`
            Indicates if the member should be guild deafened or un-deafened.
        suppress: :class:`bool`
            Indicates if the member should be suppressed in stage channels.

            .. versionadded:: 1.7

        roles: List[:class:`Role`]
            The member's new list of roles. This *replaces* the roles.
        voice_channel: Optional[:class:`VoiceChannel`]
            The voice channel to move the member to.
            Pass ``None`` to kick them from voice.
        reason: Optional[:class:`str`]
            The reason for editing this member. Shows up on the audit log.
        timeout: Optional[Union[:class:`~datetime.datetime`, :class:`~datetime.timedelta`]
            The time until the member should not be timed out.
            Set this to None to disable their timeout.

            .. versionadded:: 2.0

        Raises
        ------
        Forbidden
            You do not have the proper permissions to the action requested.
        HTTPException
            The operation failed.

        Returns
        -------
        Optional[:class:`.Member`]
            The newly updated member, if applicable. This is only returned
            when certain fields are updated.
        """
        ...
    
    async def request_to_speak(self) -> None:
        """|coro|

        Request to speak in the connected channel.

        Only applies to stage channels.

        .. note::

            Requesting members that are not the client is equivalent
            to :attr:`.edit` providing ``suppress`` as ``False``.

        .. versionadded:: 1.7

        Raises
        ------
        Forbidden
            You do not have the proper permissions to the action requested.
        HTTPException
            The operation failed.
        """
        ...
    
    async def move_to(self, channel: Optional[VocalGuildChannel], *, reason: Optional[str] = ...) -> None:
        """|coro|

        Moves a member to a new voice channel (they must be connected first).

        You must have the :attr:`~Permissions.move_members` permission to
        use this.

        This raises the same exceptions as :meth:`edit`.

        .. versionchanged:: 1.1
            Can now pass ``None`` to kick a member from voice.

        Parameters
        ----------
        channel: Optional[:class:`VoiceChannel`]
            The new voice channel to move the member to.
            Pass ``None`` to kick them from voice.
        reason: Optional[:class:`str`]
            The reason for doing this action. Shows up on the audit log.
        """
        ...
    
    async def disconnect(self, *, reason: Optional[str] = ...) -> None:
        """|coro|

        Disconnects a member from the voice channel they are connected to.

        You must have the :attr:`~Permissions.move_members` permission to
        use this.

        This raises the same exceptions as :meth:`edit`.

        Parameters
        ----------
        reason: Optional[:class:`str`]
            The reason for doing this action. Shows up on the audit log.
        """
        ...
    
    async def add_roles(self, *roles: Snowflake, reason: Optional[str] = ..., atomic: bool = ...) -> None:
        r"""|coro|

        Gives the member a number of :class:`Role`\s.

        You must have the :attr:`~Permissions.manage_roles` permission to
        use this, and the added :class:`Role`\s must appear lower in the list
        of roles than the highest role of the member.

        Parameters
        ----------
        \*roles: :class:`abc.Snowflake`
            An argument list of :class:`abc.Snowflake` representing a :class:`Role`
            to give to the member.
        reason: Optional[:class:`str`]
            The reason for adding these roles. Shows up on the audit log.
        atomic: :class:`bool`
            Whether to atomically add roles. This will ensure that multiple
            operations will always be applied regardless of the current
            state of the cache.

        Raises
        ------
        Forbidden
            You do not have permissions to add these roles.
        HTTPException
            Adding roles failed.
        """
        ...
    
    async def remove_roles(self, *roles: Snowflake, reason: Optional[str] = ..., atomic: bool = ...) -> None:
        r"""|coro|

        Removes :class:`Role`\s from this member.

        You must have the :attr:`~Permissions.manage_roles` permission to
        use this, and the removed :class:`Role`\s must appear lower in the list
        of roles than the highest role of the member.

        Parameters
        ----------
        \*roles: :class:`abc.Snowflake`
            An argument list of :class:`abc.Snowflake` representing a :class:`Role`
            to remove from the member.
        reason: Optional[:class:`str`]
            The reason for removing these roles. Shows up on the audit log.
        atomic: :class:`bool`
            Whether to atomically remove roles. This will ensure that multiple
            operations will always be applied regardless of the current
            state of the cache.

        Raises
        ------
        Forbidden
            You do not have permissions to remove these roles.
        HTTPException
            Removing the roles failed.
        """
        ...
    
    def get_role(self, role_id: int, /) -> Optional[Role]:
        """Returns a role with the given ID from roles which the member has.

        .. versionadded:: 2.0

        Parameters
        ----------
        role_id: :class:`int`
            The ID to search for.

        Returns
        -------
        Optional[:class:`Role`]
            The role or ``None`` if not found in the member's roles.
        """
        ...
    

