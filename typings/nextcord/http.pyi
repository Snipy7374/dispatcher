"""
This type stub file was generated by pyright.
"""

import asyncio
import aiohttp
from typing import Any, Callable, ClassVar, Coroutine, Dict, Iterable, List, Literal, Optional, Sequence, TYPE_CHECKING, Tuple, Type, TypeVar, Union
from .file import File
from types import TracebackType
from typing_extensions import Self
from .enums import AuditLogAction, InteractionResponseType
from .types import appinfo, audit_log, auto_moderation, channel, components, embed, emoji, guild, integration, interactions, invite, member, message, role, role_connections, scheduled_events, sticker, template, threads, user, webhook, widget
from .types.snowflake import Snowflake, SnowflakeList

_log = ...
if TYPE_CHECKING:
    T = TypeVar("T")
    BE = TypeVar("BE", bound=BaseException)
    Response = Coroutine[Any, Any, T]
async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    ...

_DEFAULT_API_VERSION = ...
_API_VERSION: Literal[9, 10] = ...
class UnsupportedAPIVersion(UserWarning):
    """Warning category raised when changing the API version to an unsupported version."""
    ...


class Route:
    BASE: ClassVar[str] = ...
    def __init__(self, method: str, path: str, **parameters: Any) -> None:
        ...
    
    @property
    def bucket(self) -> str:
        ...
    


class MaybeUnlock:
    def __init__(self, lock: asyncio.Lock) -> None:
        ...
    
    def __enter__(self) -> Self:
        ...
    
    def defer(self) -> None:
        ...
    
    def __exit__(self, exc_type: Optional[Type[BE]], exc: Optional[BE], traceback: Optional[TracebackType]) -> None:
        ...
    


class HTTPClient:
    """Represents an HTTP client sending HTTP requests to the Discord API."""
    def __init__(self, connector: Optional[aiohttp.BaseConnector] = ..., *, proxy: Optional[str] = ..., proxy_auth: Optional[aiohttp.BasicAuth] = ..., loop: Optional[asyncio.AbstractEventLoop] = ..., unsync_clock: bool = ..., dispatch: Callable) -> None:
        ...
    
    def recreate(self) -> None:
        ...
    
    async def ws_connect(self, url: str, *, compress: int = ...) -> Any:
        ...
    
    async def request(self, route: Route, *, files: Optional[Sequence[File]] = ..., form: Optional[Iterable[Dict[str, Any]]] = ..., **kwargs: Any) -> Any:
        ...
    
    async def get_from_cdn(self, url: str) -> bytes:
        ...
    
    async def close(self) -> None:
        ...
    
    async def static_login(self, token: str) -> user.User:
        ...
    
    def logout(self) -> Response[None]:
        ...
    
    def start_group(self, user_id: Snowflake, recipients: List[int]) -> Response[channel.GroupDMChannel]:
        ...
    
    def leave_group(self, channel_id) -> Response[None]:
        ...
    
    def start_private_message(self, user_id: Snowflake) -> Response[channel.DMChannel]:
        ...
    
    def get_message_payload(self, content: Optional[str], *, tts: bool = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., flags: Optional[int] = ...) -> Dict[str, Any]:
        ...
    
    def send_message(self, channel_id: Snowflake, content: Optional[str], *, tts: bool = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[int, str]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., flags: Optional[int] = ...) -> Response[message.Message]:
        ...
    
    def send_typing(self, channel_id: Snowflake) -> Response[None]:
        ...
    
    def get_message_multipart_form(self, payload: Dict[str, Any], message_key: Optional[str] = ..., *, files: Sequence[File], content: Optional[str] = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., attachments: Optional[List[Dict[str, Any]]] = ..., flags: Optional[int] = ...) -> List[Dict[str, Any]]:
        ...
    
    def send_multipart_helper(self, route: Route, *, files: Sequence[File], content: Optional[str] = ..., tts: bool = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., attachments: Optional[List[Dict[str, Any]]] = ..., flags: Optional[int] = ...) -> Response[message.Message]:
        ...
    
    def send_files(self, channel_id: Snowflake, *, files: Sequence[File], content: Optional[str] = ..., tts: bool = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[int, str]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., flags: Optional[int] = ...) -> Response[message.Message]:
        ...
    
    def delete_message(self, channel_id: Snowflake, message_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def delete_messages(self, channel_id: Snowflake, message_ids: SnowflakeList, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def edit_message(self, channel_id: Snowflake, message_id: Snowflake, **fields: Any) -> Response[message.Message]:
        ...
    
    def add_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]:
        ...
    
    def remove_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str, member_id: Snowflake) -> Response[None]:
        ...
    
    def remove_own_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]:
        ...
    
    def get_reaction_users(self, channel_id: Snowflake, message_id: Snowflake, emoji: str, limit: int, after: Optional[Snowflake] = ...) -> Response[List[user.User]]:
        ...
    
    def clear_reactions(self, channel_id: Snowflake, message_id: Snowflake) -> Response[None]:
        ...
    
    def clear_single_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]:
        ...
    
    def get_message(self, channel_id: Snowflake, message_id: Snowflake) -> Response[message.Message]:
        ...
    
    def get_channel(self, channel_id: Snowflake) -> Response[channel.Channel]:
        ...
    
    def logs_from(self, channel_id: Snowflake, limit: int, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ..., around: Optional[Snowflake] = ...) -> Response[List[message.Message]]:
        ...
    
    def publish_message(self, channel_id: Snowflake, message_id: Snowflake) -> Response[message.Message]:
        ...
    
    def pin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def unpin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def pins_from(self, channel_id: Snowflake) -> Response[List[message.Message]]:
        ...
    
    def kick(self, user_id: Snowflake, guild_id: Snowflake, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def ban(self, user_id: Snowflake, guild_id: Snowflake, delete_message_seconds: int = ..., reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def unban(self, user_id: Snowflake, guild_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def guild_voice_state(self, user_id: Snowflake, guild_id: Snowflake, *, mute: Optional[bool] = ..., deafen: Optional[bool] = ..., reason: Optional[str] = ...) -> Response[member.Member]:
        ...
    
    def edit_profile(self, payload: Dict[str, Any]) -> Response[user.User]:
        ...
    
    def change_my_nickname(self, guild_id: Snowflake, nickname: str, *, reason: Optional[str] = ...) -> Response[member.Nickname]:
        ...
    
    def change_nickname(self, guild_id: Snowflake, user_id: Snowflake, nickname: str, *, reason: Optional[str] = ...) -> Response[member.Member]:
        ...
    
    def edit_my_voice_state(self, guild_id: Snowflake, payload: Dict[str, Any]) -> Response[None]:
        ...
    
    def edit_voice_state(self, guild_id: Snowflake, user_id: Snowflake, payload: Dict[str, Any]) -> Response[None]:
        ...
    
    def edit_member(self, guild_id: Snowflake, user_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[member.MemberWithUser]:
        ...
    
    def edit_channel(self, channel_id: Snowflake, *, reason: Optional[str] = ..., **options: Any) -> Response[channel.Channel]:
        ...
    
    def bulk_channel_update(self, guild_id: Snowflake, data: List[guild.ChannelPositionUpdate], *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def create_channel(self, guild_id: Snowflake, channel_type: channel.ChannelType, *, reason: Optional[str] = ..., **options: Any) -> Response[channel.GuildChannel]:
        ...
    
    def delete_channel(self, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def start_thread_with_message(self, channel_id: Snowflake, message_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, reason: Optional[str] = ...) -> Response[threads.Thread]:
        ...
    
    def start_thread_without_message(self, channel_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, type: threads.ThreadType, invitable: bool = ..., reason: Optional[str] = ...) -> Response[threads.Thread]:
        ...
    
    def start_thread_in_forum_channel(self, channel_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, rate_limit_per_user: int, content: Optional[str] = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., applied_tag_ids: Optional[List[str]] = ..., flags: Optional[int] = ..., reason: Optional[str] = ...) -> Response[threads.Thread]:
        ...
    
    def start_thread_in_forum_channel_with_files(self, channel_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, rate_limit_per_user: int, files: Sequence[File], content: Optional[str] = ..., embed: Optional[embed.Embed] = ..., embeds: Optional[List[embed.Embed]] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ..., stickers: Optional[List[int]] = ..., components: Optional[List[components.Component]] = ..., attachments: Optional[List[Dict[str, Any]]] = ..., applied_tag_ids: Optional[List[str]] = ..., flags: Optional[int] = ..., reason: Optional[str] = ...) -> Response[threads.Thread]:
        ...
    
    def join_thread(self, channel_id: Snowflake) -> Response[None]:
        ...
    
    def add_user_to_thread(self, channel_id: Snowflake, user_id: Snowflake) -> Response[None]:
        ...
    
    def leave_thread(self, channel_id: Snowflake) -> Response[None]:
        ...
    
    def remove_user_from_thread(self, channel_id: Snowflake, user_id: Snowflake) -> Response[None]:
        ...
    
    def get_public_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]:
        ...
    
    def get_private_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]:
        ...
    
    def get_joined_private_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]:
        ...
    
    def get_active_threads(self, guild_id: Snowflake) -> Response[threads.ThreadPaginationPayload]:
        ...
    
    def get_thread_members(self, channel_id: Snowflake) -> Response[List[threads.ThreadMember]]:
        ...
    
    def create_webhook(self, channel_id: Snowflake, *, name: str, avatar: Optional[str] = ..., reason: Optional[str] = ...) -> Response[webhook.Webhook]:
        ...
    
    def channel_webhooks(self, channel_id: Snowflake) -> Response[List[webhook.Webhook]]:
        ...
    
    def guild_webhooks(self, guild_id: Snowflake) -> Response[List[webhook.Webhook]]:
        ...
    
    def get_webhook(self, webhook_id: Snowflake) -> Response[webhook.Webhook]:
        ...
    
    def follow_webhook(self, channel_id: Snowflake, webhook_channel_id: Snowflake, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_guilds(self, limit: int, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[List[guild.Guild]]:
        ...
    
    def leave_guild(self, guild_id: Snowflake) -> Response[None]:
        ...
    
    def get_guild(self, guild_id: Snowflake, *, with_counts: bool = ...) -> Response[guild.Guild]:
        ...
    
    def delete_guild(self, guild_id: Snowflake) -> Response[None]:
        ...
    
    def create_guild(self, name: str, region: str, icon: Optional[str]) -> Response[guild.Guild]:
        ...
    
    def edit_guild(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[guild.Guild]:
        ...
    
    def get_template(self, code: str) -> Response[template.Template]:
        ...
    
    def guild_templates(self, guild_id: Snowflake) -> Response[List[template.Template]]:
        ...
    
    def create_template(self, guild_id: Snowflake, payload: template.CreateTemplate) -> Response[template.Template]:
        ...
    
    def sync_template(self, guild_id: Snowflake, code: str) -> Response[template.Template]:
        ...
    
    def edit_template(self, guild_id: Snowflake, code: str, payload) -> Response[template.Template]:
        ...
    
    def delete_template(self, guild_id: Snowflake, code: str) -> Response[None]:
        ...
    
    def create_from_template(self, code: str, name: str, region: str, icon: Optional[str]) -> Response[guild.Guild]:
        ...
    
    def get_bans(self, guild_id: Snowflake, limit: Optional[int] = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[List[guild.Ban]]:
        ...
    
    def get_ban(self, user_id: Snowflake, guild_id: Snowflake) -> Response[guild.Ban]:
        ...
    
    def get_vanity_code(self, guild_id: Snowflake) -> Response[invite.VanityInvite]:
        ...
    
    def change_vanity_code(self, guild_id: Snowflake, code: str, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_all_guild_channels(self, guild_id: Snowflake) -> Response[List[guild.GuildChannel]]:
        ...
    
    def get_members(self, guild_id: Snowflake, limit: int, after: Optional[Snowflake]) -> Response[List[member.MemberWithUser]]:
        ...
    
    def get_member(self, guild_id: Snowflake, member_id: Snowflake) -> Response[member.MemberWithUser]:
        ...
    
    def prune_members(self, guild_id: Snowflake, days: int, compute_prune_count: bool, roles: List[str], *, reason: Optional[str] = ...) -> Response[guild.GuildPrune]:
        ...
    
    def estimate_pruned_members(self, guild_id: Snowflake, days: int, roles: List[str]) -> Response[guild.GuildPrune]:
        ...
    
    def get_sticker(self, sticker_id: Snowflake) -> Response[sticker.Sticker]:
        ...
    
    def list_premium_sticker_packs(self) -> Response[sticker.ListPremiumStickerPacks]:
        ...
    
    def get_all_guild_stickers(self, guild_id: Snowflake) -> Response[List[sticker.GuildSticker]]:
        ...
    
    def get_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake) -> Response[sticker.GuildSticker]:
        ...
    
    def create_guild_sticker(self, guild_id: Snowflake, payload: sticker.CreateGuildSticker, file: File, reason: Optional[str]) -> Response[sticker.GuildSticker]:
        ...
    
    def modify_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake, payload: sticker.EditGuildSticker, reason: Optional[str]) -> Response[sticker.GuildSticker]:
        ...
    
    def delete_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake, reason: Optional[str]) -> Response[None]:
        ...
    
    def get_all_custom_emojis(self, guild_id: Snowflake) -> Response[List[emoji.Emoji]]:
        ...
    
    def get_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> Response[emoji.Emoji]:
        ...
    
    def create_custom_emoji(self, guild_id: Snowflake, name: str, image: Optional[str], *, roles: Optional[SnowflakeList] = ..., reason: Optional[str] = ...) -> Response[emoji.Emoji]:
        ...
    
    def delete_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def edit_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, *, payload: Dict[str, Any], reason: Optional[str] = ...) -> Response[emoji.Emoji]:
        ...
    
    def get_all_integrations(self, guild_id: Snowflake) -> Response[List[integration.Integration]]:
        ...
    
    def create_integration(self, guild_id: Snowflake, type: integration.IntegrationType, id: int) -> Response[None]:
        ...
    
    def edit_integration(self, guild_id: Snowflake, integration_id: Snowflake, **payload: Any) -> Response[None]:
        ...
    
    def sync_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> Response[None]:
        ...
    
    def delete_integration(self, guild_id: Snowflake, integration_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_audit_logs(self, guild_id: Snowflake, limit: int = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ..., user_id: Optional[Snowflake] = ..., action_type: Optional[AuditLogAction] = ...) -> Response[audit_log.AuditLog]:
        ...
    
    def get_widget(self, guild_id: Snowflake) -> Response[widget.Widget]:
        ...
    
    def edit_widget(self, guild_id: Snowflake, payload) -> Response[widget.WidgetSettings]:
        ...
    
    def create_invite(self, channel_id: Snowflake, *, reason: Optional[str] = ..., max_age: int = ..., max_uses: int = ..., temporary: bool = ..., unique: bool = ..., target_type: Optional[invite.InviteTargetType] = ..., target_user_id: Optional[Snowflake] = ..., target_application_id: Optional[Snowflake] = ...) -> Response[invite.Invite]:
        ...
    
    def get_invite(self, invite_id: str, *, with_counts: bool = ..., with_expiration: bool = ...) -> Response[invite.Invite]:
        ...
    
    def invites_from(self, guild_id: Snowflake) -> Response[List[invite.Invite]]:
        ...
    
    def invites_from_channel(self, channel_id: Snowflake) -> Response[List[invite.Invite]]:
        ...
    
    def delete_invite(self, invite_id: str, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_roles(self, guild_id: Snowflake) -> Response[List[role.Role]]:
        ...
    
    def edit_role(self, guild_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[role.Role]:
        ...
    
    def delete_role(self, guild_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def replace_roles(self, user_id: Snowflake, guild_id: Snowflake, role_ids: List[int], *, reason: Optional[str] = ...) -> Response[member.MemberWithUser]:
        ...
    
    def create_role(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[role.Role]:
        ...
    
    def move_role_position(self, guild_id: Snowflake, positions: List[guild.RolePositionUpdate], *, reason: Optional[str] = ...) -> Response[List[role.Role]]:
        ...
    
    def add_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def remove_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def edit_channel_permissions(self, channel_id: Snowflake, target: Snowflake, allow: str, deny: str, type: channel.OverwriteType, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def delete_channel_permissions(self, channel_id: Snowflake, target: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def move_member(self, user_id: Snowflake, guild_id: Snowflake, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[member.MemberWithUser]:
        ...
    
    def get_stage_instance(self, channel_id: Snowflake) -> Response[channel.StageInstance]:
        ...
    
    def create_stage_instance(self, *, reason: Optional[str], **payload: Any) -> Response[channel.StageInstance]:
        ...
    
    def edit_stage_instance(self, channel_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[None]:
        ...
    
    def delete_stage_instance(self, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_global_commands(self, application_id: Snowflake, with_localizations: bool = ...) -> Response[List[interactions.ApplicationCommand]]:
        ...
    
    def get_global_command(self, application_id: Snowflake, command_id: Snowflake) -> Response[interactions.ApplicationCommand]:
        ...
    
    def upsert_global_command(self, application_id: Snowflake, payload) -> Response[interactions.ApplicationCommand]:
        ...
    
    def edit_global_command(self, application_id: Snowflake, command_id: Snowflake, payload: interactions.EditApplicationCommand) -> Response[interactions.ApplicationCommand]:
        ...
    
    def delete_global_command(self, application_id: Snowflake, command_id: Snowflake) -> Response[None]:
        ...
    
    def bulk_upsert_global_commands(self, application_id: Snowflake, payload) -> Response[List[interactions.ApplicationCommand]]:
        ...
    
    def get_guild_commands(self, application_id: Snowflake, guild_id: Snowflake, with_localizations: bool = ...) -> Response[List[interactions.ApplicationCommand]]:
        ...
    
    def get_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[interactions.ApplicationCommand]:
        ...
    
    def upsert_guild_command(self, application_id: Snowflake, guild_id: Snowflake, payload: interactions.EditApplicationCommand) -> Response[interactions.ApplicationCommand]:
        ...
    
    def edit_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake, payload: interactions.EditApplicationCommand) -> Response[interactions.ApplicationCommand]:
        ...
    
    def delete_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[None]:
        ...
    
    def bulk_upsert_guild_commands(self, application_id: Snowflake, guild_id: Snowflake, payload: List[interactions.EditApplicationCommand]) -> Response[List[interactions.ApplicationCommand]]:
        ...
    
    def create_interaction_response(self, interaction_id: Snowflake, token: str, *, type: InteractionResponseType, data: Optional[interactions.InteractionApplicationCommandCallbackData] = ...) -> Response[None]:
        ...
    
    def get_original_interaction_response(self, application_id: Snowflake, token: str) -> Response[message.Message]:
        ...
    
    def edit_original_interaction_response(self, application_id: Snowflake, token: str, file: Optional[File] = ..., content: Optional[str] = ..., embeds: Optional[List[embed.Embed]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ...) -> Response[message.Message]:
        ...
    
    def delete_original_interaction_response(self, application_id: Snowflake, token: str) -> Response[None]:
        ...
    
    def create_followup_message(self, application_id: Snowflake, token: str, files: List[File] = ..., content: Optional[str] = ..., tts: bool = ..., embeds: Optional[List[embed.Embed]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ...) -> Response[message.Message]:
        ...
    
    def edit_followup_message(self, application_id: Snowflake, token: str, message_id: Snowflake, file: Optional[File] = ..., content: Optional[str] = ..., embeds: Optional[List[embed.Embed]] = ..., allowed_mentions: Optional[message.AllowedMentions] = ...) -> Response[message.Message]:
        ...
    
    def delete_followup_message(self, application_id: Snowflake, token: str, message_id: Snowflake) -> Response[None]:
        ...
    
    def get_guild_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake) -> Response[List[interactions.GuildApplicationCommandPermissions]]:
        ...
    
    def get_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[interactions.GuildApplicationCommandPermissions]:
        ...
    
    def edit_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake, payload: interactions.BaseGuildApplicationCommandPermissions) -> Response[None]:
        ...
    
    def bulk_edit_guild_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, payload: List[interactions.PartialGuildApplicationCommandPermissions]) -> Response[None]:
        ...
    
    def application_info(self) -> Response[appinfo.AppInfo]:
        ...
    
    @staticmethod
    def format_websocket_url(url: str, encoding: str = ..., zlib: bool = ...) -> str:
        ...
    
    async def get_gateway(self, *, encoding: str = ..., zlib: bool = ...) -> str:
        ...
    
    async def get_bot_gateway(self, *, encoding: str = ..., zlib: bool = ...) -> Tuple[int, str]:
        ...
    
    def get_user(self, user_id: Snowflake) -> Response[user.User]:
        ...
    
    def get_guild_events(self, guild_id: Snowflake, with_user_count: bool) -> Response[List[scheduled_events.ScheduledEvent]]:
        ...
    
    def create_event(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[scheduled_events.ScheduledEvent]:
        ...
    
    def get_event(self, guild_id: Snowflake, event_id: Snowflake, with_user_count: bool) -> Response[scheduled_events.ScheduledEvent]:
        ...
    
    def edit_event(self, guild_id: Snowflake, event_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[scheduled_events.ScheduledEvent]:
        ...
    
    def delete_event(self, guild_id: Snowflake, event_id: Snowflake) -> Response[None]:
        ...
    
    def get_event_users(self, guild_id: Snowflake, event_id: Snowflake, *, limit: int = ..., with_member: bool = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[List[scheduled_events.ScheduledEventUser]]:
        ...
    
    def list_guild_auto_moderation_rules(self, guild_id: Snowflake) -> Response[List[auto_moderation.AutoModerationRule]]:
        ...
    
    def get_auto_moderation_rule(self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake) -> Response[auto_moderation.AutoModerationRule]:
        ...
    
    def create_auto_moderation_rule(self, guild_id: Snowflake, data: auto_moderation.AutoModerationRuleCreate, *, reason: Optional[str] = ...) -> Response[auto_moderation.AutoModerationRule]:
        ...
    
    def modify_auto_moderation_rule(self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake, data: auto_moderation.AutoModerationRuleModify, *, reason: Optional[str] = ...) -> Response[auto_moderation.AutoModerationRule]:
        ...
    
    def delete_auto_moderation_rule(self, guild_id: Snowflake, auto_moderation_rule_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]:
        ...
    
    def get_role_connection_metadata(self, application_id: Snowflake) -> Response[List[role_connections.ApplicationRoleConnectionMetadata]]:
        ...
    
    def update_role_connection_metadata(self, application_id: Snowflake, data: List[role_connections.ApplicationRoleConnectionMetadata], *, reason: Optional[str] = ...) -> Response[List[role_connections.ApplicationRoleConnectionMetadata]]:
        ...
    


