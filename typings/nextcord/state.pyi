"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Any, Callable, Coroutine, Dict, List, Optional, Sequence, Set, TYPE_CHECKING, TypeVar, Union
from . import utils
from .activity import BaseActivity
from .channel import *
from .emoji import Emoji
from .enums import Status
from .flags import Intents, MemberCacheFlags
from .guild import Guild, GuildChannel, VocalGuildChannel
from .member import Member
from .mentions import AllowedMentions
from .message import Message
from .partial_emoji import PartialEmoji
from .raw_models import *
from .scheduled_events import ScheduledEvent
from .sticker import GuildSticker
from .threads import Thread
from .ui.modal import Modal
from .ui.view import View
from .user import User
from asyncio import Future
from .abc import MessageableChannel, PrivateChannel
from .application_command import BaseApplicationCommand
from .client import Client
from .gateway import DiscordWebSocket
from .http import HTTPClient
from .types.channel import DMChannel as DMChannelPayload
from .types.emoji import Emoji as EmojiPayload
from .types.interactions import ApplicationCommand as ApplicationCommandPayload
from .types.message import Message as MessagePayload
from .types.scheduled_events import ScheduledEvent as ScheduledEventPayload
from .types.sticker import GuildSticker as GuildStickerPayload
from .types.user import PartialUser as PartialUserPayload, User as UserPayload
from .voice_client import VoiceProtocol

if TYPE_CHECKING:
    T = TypeVar("T")
    CS = TypeVar("CS", bound="ConnectionState")
    Channel = Union[GuildChannel, VocalGuildChannel, PrivateChannel, PartialMessageable]
MISSING = utils.MISSING
class ChunkRequest:
    def __init__(self, guild_id: int, loop: asyncio.AbstractEventLoop, resolver: Callable[[int], Any], *, cache: bool = ...) -> None:
        ...
    
    def add_members(self, members: List[Member]) -> None:
        ...
    
    async def wait(self) -> List[Member]:
        ...
    
    def get_future(self) -> asyncio.Future[List[Member]]:
        ...
    
    def done(self) -> None:
        ...
    


_log = ...
async def logging_coroutine(coroutine: Coroutine[Any, Any, T], *, info: str) -> Optional[T]:
    ...

class ConnectionState:
    if TYPE_CHECKING:
        _get_websocket: Callable[..., DiscordWebSocket]
        _get_client: Callable[..., Client]
        _parsers: Dict[str, Callable[[Dict[str, Any]], None]]
        ...
    def __init__(self, *, dispatch: Callable, handlers: Dict[str, Callable], hooks: Dict[str, Callable], http: HTTPClient, loop: asyncio.AbstractEventLoop, max_messages: Optional[int] = ..., application_id: Optional[int] = ..., heartbeat_timeout: float = ..., guild_ready_timeout: float = ..., allowed_mentions: Optional[AllowedMentions] = ..., activity: Optional[BaseActivity] = ..., status: Optional[Status] = ..., intents: Intents = ..., chunk_guilds_at_startup: bool = ..., member_cache_flags: MemberCacheFlags = ...) -> None:
        ...
    
    def clear(self, *, views: bool = ..., modals: bool = ...) -> None:
        ...
    
    def process_chunk_requests(self, guild_id: int, nonce: Optional[str], members: List[Member], complete: bool) -> None:
        ...
    
    def call_handlers(self, key: str, *args: Any, **kwargs: Any) -> None:
        ...
    
    async def call_hooks(self, key: str, *args: Any, **kwargs: Any) -> None:
        ...
    
    @property
    def self_id(self) -> Optional[int]:
        ...
    
    @property
    def intents(self) -> Intents:
        ...
    
    @property
    def voice_clients(self) -> List[VoiceProtocol]:
        ...
    
    def store_user(self, data: UserPayload) -> User:
        ...
    
    def deref_user(self, user_id: int) -> None:
        ...
    
    def create_user(self, data: Union[PartialUserPayload, UserPayload]) -> User:
        ...
    
    def deref_user_no_intents(self, user_id: int) -> None:
        ...
    
    def get_user(self, id: Optional[int]) -> Optional[User]:
        ...
    
    def store_emoji(self, guild: Guild, data: EmojiPayload) -> Emoji:
        ...
    
    def store_sticker(self, guild: Guild, data: GuildStickerPayload) -> GuildSticker:
        ...
    
    def store_view(self, view: View, message_id: Optional[int] = ...) -> None:
        ...
    
    def store_modal(self, modal: Modal, user_id: Optional[int] = ...) -> None:
        ...
    
    def remove_view(self, view: View, message_id: Optional[int] = ...) -> None:
        ...
    
    def remove_modal(self, modal: Modal) -> None:
        ...
    
    def prevent_view_updates_for(self, message_id: Optional[int]) -> Optional[View]:
        ...
    
    @property
    def persistent_views(self) -> Sequence[View]:
        ...
    
    @property
    def guilds(self) -> List[Guild]:
        ...
    
    @property
    def emojis(self) -> List[Emoji]:
        ...
    
    @property
    def stickers(self) -> List[GuildSticker]:
        ...
    
    def get_emoji(self, emoji_id: Optional[int]) -> Optional[Emoji]:
        ...
    
    def get_sticker(self, sticker_id: Optional[int]) -> Optional[GuildSticker]:
        ...
    
    @property
    def private_channels(self) -> List[PrivateChannel]:
        ...
    
    def add_dm_channel(self, data: DMChannelPayload) -> DMChannel:
        ...
    
    @property
    def application_commands(self) -> Set[BaseApplicationCommand]:
        """Gets a copy of the ApplicationCommand object set. If the original is given out and modified, massive desyncs
        may occur. This should be used internally as well if size-changed-during-iteration is a worry.
        """
        ...
    
    def get_application_command(self, command_id: int) -> Optional[BaseApplicationCommand]:
        ...
    
    def get_application_command_from_signature(self, name: Optional[str], cmd_type: int, guild_id: Optional[int]) -> Optional[BaseApplicationCommand]:
        ...
    
    def get_guild_application_commands(self, guild_id: Optional[int] = ..., rollout: bool = ...) -> List[BaseApplicationCommand]:
        """Gets all commands that have the given guild ID. If guild_id is None, all guild commands are returned. if
        rollout is True, guild_ids_to_rollout is used.
        """
        ...
    
    def get_global_application_commands(self, rollout: bool = ...) -> List[BaseApplicationCommand]:
        """Gets all commands that are registered globally. If rollout is True, is_global is used."""
        ...
    
    def add_application_command(self, command: BaseApplicationCommand, *, overwrite: bool = ..., use_rollout: bool = ..., pre_remove: bool = ...) -> None:
        """Adds the command to the state and updates the state with any changes made to the command.
        Removes all existing references, then adds them.
        Safe to call multiple times on the same application command.

        Parameters
        ----------
        command: :class:`BaseApplicationCommand`
            The command to add/update the state with.
        overwrite: :class:`bool`
            If the library will let you add a command that overlaps with an existing command. Default ``False``.
        use_rollout: :class:`bool`
            If the command should be added to the state with its rollout guild IDs.
        pre_remove: :class:`bool`
            If the command should be removed before adding it. This will clear all signatures from storage, including
            rollout ones.
        """
        ...
    
    def remove_application_command(self, command: BaseApplicationCommand) -> None:
        """Removes the command and all signatures + associated IDs from the state.
        Safe to call with commands that aren't in the state.

        Parameters
        ----------
        command: :class:`BaseApplicationCommand`
            the command to remove from the state.
        """
        ...
    
    def add_all_rollout_signatures(self) -> None:
        """This adds all command signatures for rollouts to the signature cache."""
        ...
    
    async def sync_all_application_commands(self, data: Optional[Dict[Optional[int], List[ApplicationCommandPayload]]] = ..., *, use_rollout: bool = ..., associate_known: bool = ..., delete_unknown: bool = ..., update_known: bool = ..., register_new: bool = ..., ignore_forbidden: bool = ...): # -> None:
        """|coro|

        Syncs all application commands with Discord. Will sync global commands if any commands added are global, and
        syncs with all guilds that have an application command targeting them.

        This may call Discord many times depending on how different guilds you have local commands for, and how many
        commands Discord needs to be updated or added, which may cause your bot to be rate limited or even Cloudflare
        banned in VERY extreme cases.

        This may incur high CPU usage depending on how many commands you have and how complex they are, which may cause
        your bot to halt while it checks local commands against the existing commands that Discord has.

        For a more targeted version of this method, see :func:`Client.sync_application_commands`

        Parameters
        ----------
        data: Optional[Dict[Optional[:class:`int`], List[:class:`dict`]]]
            Data to use when comparing local application commands to what Discord has. The key should be the
            :class:`int` guild ID (`None` for global) corresponding to the value list of application command payloads
            from Discord. Any guild ID's not provided will be fetched if needed. Defaults to ``None``
        use_rollout: :class:`bool`
            If the rollout guild IDs of commands should be used. Defaults to ``True``
        associate_known: :class:`bool`
            If local commands that match a command already on Discord should be associated with each other.
            Defaults to ``True``
        delete_unknown: :class:`bool`
            If commands on Discord that don't match a local command should be deleted. Defaults to ``True``.
        update_known: :class:`bool`
            If commands on Discord have a basic match with a local command, but don't fully match, should be updated.
            Defaults to ``True``
        register_new: :class:`bool`
            If a local command that doesn't have a basic match on Discord should be added to Discord.
            Defaults to ``True``
        ignore_forbidden: :class:`bool`
            If this command should raise an :class:`errors.Forbidden` exception when the bot encounters a guild where
            it doesn't have permissions to view application commands.
            Defaults to ``True``
        """
        ...
    
    async def sync_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ..., associate_known: bool = ..., delete_unknown: bool = ..., update_known: bool = ..., register_new: bool = ...) -> None:
        """|coro|
        Syncs the locally added application commands with the Guild corresponding to the given ID, or syncs
        global commands if the guild_id is ``None``.

        Parameters
        ----------
        data: Optional[List[:class:`dict`]]
            Data to use when comparing local application commands to what Discord has. Should be a list of application
            command data from Discord. If left as ``None``, it will be fetched if needed. Defaults to ``None``.
        guild_id: Optional[:class:`int`]
            ID of the guild to sync application commands with. If set to ``None``, global commands will be synced instead.
            Defaults to ``None``.
        associate_known: :class:`bool`
            If local commands that match a command already on Discord should be associated with each other.
            Defaults to ``True``.
        delete_unknown: :class:`bool`
            If commands on Discord that don't match a local command should be deleted. Defaults to ``True``.
        update_known: :class:`bool`
            If commands on Discord have a basic match with a local command, but don't fully match, should be updated.
            Defaults to ``True``.
        register_new: :class:`bool`
            If a local command that doesn't have a basic match on Discord should be added to Discord.
            Defaults to ``True``.

        """
        ...
    
    async def discover_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ..., associate_known: bool = ..., delete_unknown: bool = ..., update_known: bool = ...) -> None:
        """|coro|
        Associates existing, deletes unknown, and updates modified commands for either global commands or a specific
        guild. This does a deep check on found commands, which may be expensive CPU-wise.

        Running this for global or the same guild multiple times at once may cause unexpected or unstable behavior.

        Parameters
        ----------
        data: Optional[List[:class:`dict]]
            Payload from ``HTTPClient.get_guild_commands`` or ``HTTPClient.get_global_commands`` to deploy with. If None,
            the payload will be retrieved from Discord.
        guild_id: Optional[:class:`int`]
            Guild ID to deploy application commands to. If ``None``, global commands are deployed to.
        associate_known: :class:`bool`
            If True, commands on Discord that pass a signature check and a deep check will be associated with locally
            added ApplicationCommand objects.
        delete_unknown: :class:`bool`
            If ``True``, commands on Discord that fail a signature check will be removed. If ``update_known`` is False,
            commands that pass the signature check but fail the deep check will also be removed.
        update_known: :class:`bool`
            If ``True``, commands on Discord that pass a signature check but fail the deep check will be updated.
        """
        ...
    
    async def deploy_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., *, guild_id: Optional[int] = ..., associate_known: bool = ..., delete_unknown: bool = ..., update_known: bool = ...) -> None:
        ...
    
    async def associate_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ...) -> None:
        ...
    
    async def delete_unknown_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ...) -> None:
        ...
    
    async def update_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ...) -> None:
        ...
    
    async def register_new_application_commands(self, data: Optional[List[ApplicationCommandPayload]] = ..., guild_id: Optional[int] = ...) -> None:
        """|coro|
        Registers locally added application commands that don't match a signature that Discord has registered for
        either global commands or a specific guild.

        Parameters
        ----------
        data: Optional[List[:class:`dict`]]
            Data to use when comparing local application commands to what Discord has. Should be a list of application
            command data from Discord. If left as ``None``, it will be fetched if needed. Defaults to ``None``
        guild_id: Optional[:class:`int`]
            ID of the guild to sync application commands with. If set to ``None``, global commands will be synced instead.
            Defaults to ``None``.
        """
        ...
    
    async def register_application_command(self, command: BaseApplicationCommand, guild_id: Optional[int] = ...) -> None:
        """|coro|
        Registers the given application command either for a specific guild or globally and adds the command to the bot.

        Parameters
        ----------
        command: :class:`BaseApplicationCommand`
            Application command to register.
        guild_id: Optional[:class:`int`]
            ID of the guild to register the application commands to. If set to ``None``, the commands will be registered
            as global commands instead. Defaults to ``None``.
        """
        ...
    
    async def delete_application_command(self, command: BaseApplicationCommand, guild_id: Optional[int] = ...) -> None:
        """|coro|
        Deletes the given application from Discord for the given guild ID or globally, then removes the signature and
        command ID from the cache if possible.

        Parameters
        ----------
        command: :class:`ApplicationCommand`
            Application command to delete.
        guild_id: Optional[:class:`int`]
            Guild ID to delete the application commands from. If ``None``, the command is deleted from global.
        """
        ...
    
    async def chunker(self, guild_id: int, query: str = ..., limit: int = ..., presences: bool = ..., *, nonce: Optional[str] = ...) -> None:
        ...
    
    async def query_members(self, guild: Guild, query: Optional[str], limit: int, user_ids: Optional[List[int]], cache: bool, presences: bool): # -> List[Member]:
        ...
    
    def parse_ready(self, data) -> None:
        ...
    
    def parse_resumed(self, data) -> None:
        ...
    
    def parse_message_create(self, data) -> None:
        ...
    
    def parse_message_delete(self, data) -> None:
        ...
    
    def parse_message_delete_bulk(self, data) -> None:
        ...
    
    def parse_message_update(self, data) -> None:
        ...
    
    def parse_message_reaction_add(self, data) -> None:
        ...
    
    def parse_message_reaction_remove_all(self, data) -> None:
        ...
    
    def parse_message_reaction_remove(self, data) -> None:
        ...
    
    def parse_message_reaction_remove_emoji(self, data) -> None:
        ...
    
    def parse_interaction_create(self, data) -> None:
        ...
    
    def parse_presence_update(self, data) -> None:
        ...
    
    def parse_user_update(self, data) -> None:
        ...
    
    def parse_invite_create(self, data) -> None:
        ...
    
    def parse_invite_delete(self, data) -> None:
        ...
    
    def parse_channel_delete(self, data) -> None:
        ...
    
    def parse_channel_update(self, data) -> None:
        ...
    
    def parse_channel_create(self, data) -> None:
        ...
    
    def parse_channel_pins_update(self, data) -> None:
        ...
    
    def parse_thread_create(self, data) -> None:
        ...
    
    def parse_thread_update(self, data) -> None:
        ...
    
    def parse_thread_delete(self, data) -> None:
        ...
    
    def parse_thread_list_sync(self, data) -> None:
        ...
    
    def parse_thread_member_update(self, data) -> None:
        ...
    
    def parse_thread_members_update(self, data) -> None:
        ...
    
    def parse_guild_member_add(self, data) -> None:
        ...
    
    def parse_guild_member_remove(self, data) -> None:
        ...
    
    def parse_guild_member_update(self, data) -> None:
        ...
    
    def parse_guild_emojis_update(self, data) -> None:
        ...
    
    def parse_guild_stickers_update(self, data) -> None:
        ...
    
    def is_guild_evicted(self, guild) -> bool:
        ...
    
    async def chunk_guild(self, guild, *, wait: bool = ..., cache=...): # -> List[Member] | Future[List[Member]]:
        ...
    
    def parse_guild_create(self, data) -> None:
        ...
    
    def parse_guild_update(self, data) -> None:
        ...
    
    def parse_guild_delete(self, data) -> None:
        ...
    
    def parse_guild_ban_add(self, data) -> None:
        ...
    
    def parse_guild_ban_remove(self, data) -> None:
        ...
    
    def parse_guild_role_create(self, data) -> None:
        ...
    
    def parse_guild_role_delete(self, data) -> None:
        ...
    
    def parse_guild_role_update(self, data) -> None:
        ...
    
    def parse_guild_members_chunk(self, data) -> None:
        ...
    
    def parse_guild_integrations_update(self, data) -> None:
        ...
    
    def parse_integration_create(self, data) -> None:
        ...
    
    def parse_integration_update(self, data) -> None:
        ...
    
    def parse_integration_delete(self, data) -> None:
        ...
    
    def parse_webhooks_update(self, data) -> None:
        ...
    
    def parse_stage_instance_create(self, data) -> None:
        ...
    
    def parse_stage_instance_update(self, data) -> None:
        ...
    
    def parse_stage_instance_delete(self, data) -> None:
        ...
    
    def parse_voice_state_update(self, data) -> None:
        ...
    
    def parse_voice_server_update(self, data) -> None:
        ...
    
    def parse_typing_start(self, data) -> None:
        ...
    
    def get_reaction_emoji(self, data) -> Union[Emoji, PartialEmoji]:
        ...
    
    def get_channel(self, id: Optional[int]) -> Optional[Union[Channel, Thread]]:
        ...
    
    def get_scheduled_event(self, id: int) -> Optional[ScheduledEvent]:
        ...
    
    def create_message(self, *, channel: MessageableChannel, data: MessagePayload) -> Message:
        ...
    
    def create_scheduled_event(self, *, guild: Guild, data: ScheduledEventPayload) -> ScheduledEvent:
        ...
    
    def parse_guild_scheduled_event_create(self, data) -> None:
        ...
    
    def parse_guild_scheduled_event_update(self, data) -> None:
        ...
    
    def parse_guild_scheduled_event_delete(self, data) -> None:
        ...
    
    def parse_guild_scheduled_event_user_add(self, data) -> None:
        ...
    
    def parse_guild_scheduled_event_user_remove(self, data) -> None:
        ...
    
    def parse_auto_moderation_rule_create(self, data) -> None:
        ...
    
    def parse_auto_moderation_rule_update(self, data) -> None:
        ...
    
    def parse_auto_moderation_rule_delete(self, data) -> None:
        ...
    
    def parse_auto_moderation_action_execution(self, data) -> None:
        ...
    
    def parse_guild_audit_log_entry_create(self, data) -> None:
        ...
    


class AutoShardedConnectionState(ConnectionState):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    async def chunker(self, guild_id: int, query: str = ..., limit: int = ..., presences: bool = ..., *, shard_id: Optional[int] = ..., nonce: Optional[str] = ...) -> None:
        ...
    
    def parse_ready(self, data) -> None:
        ...
    
    def parse_resumed(self, data) -> None:
        ...
    

