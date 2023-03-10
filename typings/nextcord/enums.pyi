"""
This type stub file was generated by pyright.
"""

import enum
from typing import Any, NamedTuple, Optional, Type, TypeVar

__all__ = ("Enum", "IntEnum", "StrEnum", "UnknownEnumValue", "ChannelType", "MessageType", "VoiceRegion", "SpeakingState", "VerificationLevel", "ContentFilter", "Status", "DefaultAvatar", "AuditLogAction", "AuditLogActionCategory", "UserFlags", "ActivityType", "NotificationLevel", "TeamMembershipState", "WebhookType", "ExpireBehaviour", "ExpireBehavior", "StickerType", "StickerFormatType", "InviteTarget", "Locale", "VideoQualityMode", "ComponentType", "ButtonStyle", "TextInputStyle", "StagePrivacyLevel", "InteractionType", "InteractionResponseType", "ApplicationCommandType", "ApplicationCommandOptionType", "NSFWLevel", "ScheduledEventEntityType", "ScheduledEventPrivacyLevel", "ScheduledEventStatus", "AutoModerationEventType", "AutoModerationTriggerType", "KeywordPresetType", "AutoModerationActionType", "SortOrderType", "RoleConnectionMetadataType", "ForumLayoutType")
class UnknownEnumValue(NamedTuple):
    """Proxy for the underlying name and value of an attribute not known to the Enum."""
    name: str
    value: Any
    def __str__(self) -> str:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Enum(enum.Enum):
    """An enum that supports trying for unknown values."""
    @classmethod
    def try_value(cls, value): # -> Self@Enum:
        ...
    


class IntEnum(int, Enum):
    """An enum that supports comparing and hashing as an int."""
    def __int__(self) -> int:
        ...
    


class StrEnum(str, Enum):
    """An enum that supports comparing and hashing as a string."""
    def __str__(self) -> str:
        ...
    


class ChannelType(IntEnum):
    text = ...
    private = ...
    voice = ...
    group = ...
    category = ...
    news = ...
    news_thread = ...
    public_thread = ...
    private_thread = ...
    stage_voice = ...
    guild_directory = ...
    forum = ...
    def __str__(self) -> str:
        ...
    


class MessageType(IntEnum):
    default = ...
    recipient_add = ...
    recipient_remove = ...
    call = ...
    channel_name_change = ...
    channel_icon_change = ...
    pins_add = ...
    new_member = ...
    premium_guild_subscription = ...
    premium_guild_tier_1 = ...
    premium_guild_tier_2 = ...
    premium_guild_tier_3 = ...
    channel_follow_add = ...
    guild_stream = ...
    guild_discovery_disqualified = ...
    guild_discovery_requalified = ...
    guild_discovery_grace_period_initial_warning = ...
    guild_discovery_grace_period_final_warning = ...
    thread_created = ...
    reply = ...
    chat_input_command = ...
    thread_starter_message = ...
    guild_invite_reminder = ...
    context_menu_command = ...
    auto_moderation_action = ...


class VoiceRegion(StrEnum):
    us_west = ...
    us_east = ...
    us_south = ...
    us_central = ...
    eu_west = ...
    eu_central = ...
    singapore = ...
    london = ...
    sydney = ...
    amsterdam = ...
    frankfurt = ...
    brazil = ...
    hongkong = ...
    russia = ...
    japan = ...
    southafrica = ...
    south_korea = ...
    india = ...
    europe = ...
    dubai = ...
    vip_us_east = ...
    vip_us_west = ...
    vip_amsterdam = ...


class SpeakingState(IntEnum):
    none = ...
    voice = ...
    soundshare = ...
    priority = ...
    def __str__(self) -> str:
        ...
    


class VerificationLevel(IntEnum):
    none = ...
    low = ...
    medium = ...
    high = ...
    highest = ...
    def __str__(self) -> str:
        ...
    


class ContentFilter(IntEnum):
    disabled = ...
    no_role = ...
    all_members = ...
    def __str__(self) -> str:
        ...
    


class Status(StrEnum):
    online = ...
    offline = ...
    idle = ...
    dnd = ...
    do_not_disturb = ...
    invisible = ...


class DefaultAvatar(IntEnum):
    blurple = ...
    grey = ...
    gray = ...
    green = ...
    orange = ...
    red = ...
    def __str__(self) -> str:
        ...
    


class NotificationLevel(IntEnum):
    all_messages = ...
    only_mentions = ...


class AuditLogActionCategory(IntEnum):
    create = ...
    delete = ...
    update = ...


class AuditLogAction(IntEnum):
    guild_update = ...
    channel_create = ...
    channel_update = ...
    channel_delete = ...
    overwrite_create = ...
    overwrite_update = ...
    overwrite_delete = ...
    kick = ...
    member_prune = ...
    ban = ...
    unban = ...
    member_update = ...
    member_role_update = ...
    member_move = ...
    member_disconnect = ...
    bot_add = ...
    role_create = ...
    role_update = ...
    role_delete = ...
    invite_create = ...
    invite_update = ...
    invite_delete = ...
    webhook_create = ...
    webhook_update = ...
    webhook_delete = ...
    emoji_create = ...
    emoji_update = ...
    emoji_delete = ...
    message_delete = ...
    message_bulk_delete = ...
    message_pin = ...
    message_unpin = ...
    integration_create = ...
    integration_update = ...
    integration_delete = ...
    stage_instance_create = ...
    stage_instance_update = ...
    stage_instance_delete = ...
    sticker_create = ...
    sticker_update = ...
    sticker_delete = ...
    scheduled_event_create = ...
    scheduled_event_update = ...
    scheduled_event_delete = ...
    thread_create = ...
    thread_update = ...
    thread_delete = ...
    auto_moderation_rule_create = ...
    auto_moderation_rule_update = ...
    auto_moderation_rule_delete = ...
    auto_moderation_block_message = ...
    auto_moderation_flag_to_channel = ...
    auto_moderation_user_communication_disabled = ...
    @property
    def category(self) -> Optional[AuditLogActionCategory]:
        ...
    
    @property
    def target_type(self) -> Optional[str]:
        ...
    


class UserFlags(IntEnum):
    staff = ...
    partner = ...
    hypesquad = ...
    bug_hunter = ...
    mfa_sms = ...
    premium_promo_dismissed = ...
    hypesquad_bravery = ...
    hypesquad_brilliance = ...
    hypesquad_balance = ...
    early_supporter = ...
    team_user = ...
    system = ...
    has_unread_urgent_messages = ...
    bug_hunter_level_2 = ...
    verified_bot = ...
    verified_bot_developer = ...
    discord_certified_moderator = ...
    bot_http_interactions = ...
    known_spammer = ...
    active_developer = ...


class ActivityType(IntEnum):
    unknown = ...
    playing = ...
    streaming = ...
    listening = ...
    watching = ...
    custom = ...
    competing = ...


class TeamMembershipState(IntEnum):
    invited = ...
    accepted = ...


class WebhookType(IntEnum):
    incoming = ...
    channel_follower = ...
    application = ...


class ExpireBehaviour(IntEnum):
    remove_role = ...
    kick = ...


ExpireBehavior = ExpireBehaviour
class StickerType(IntEnum):
    standard = ...
    guild = ...


class StickerFormatType(IntEnum):
    png = ...
    apng = ...
    lottie = ...
    gif = ...
    @property
    def file_extension(self) -> str:
        ...
    


class InviteTarget(IntEnum):
    unknown = ...
    stream = ...
    embedded_application = ...


class InteractionType(IntEnum):
    ping = ...
    application_command = ...
    component = ...
    application_command_autocomplete = ...
    modal_submit = ...


class InteractionResponseType(IntEnum):
    pong = ...
    channel_message = ...
    deferred_channel_message = ...
    deferred_message_update = ...
    message_update = ...
    application_command_autocomplete_result = ...
    modal = ...


class ApplicationCommandType(IntEnum):
    chat_input = ...
    user = ...
    message = ...


class ApplicationCommandOptionType(IntEnum):
    sub_command = ...
    sub_command_group = ...
    string = ...
    integer = ...
    boolean = ...
    user = ...
    channel = ...
    role = ...
    mentionable = ...
    number = ...
    attachment = ...


class Locale(StrEnum):
    da = ...
    de = ...
    en_GB = ...
    en_US = ...
    es_ES = ...
    fr = ...
    hr = ...
    id = ...
    it = ...
    lt = ...
    hu = ...
    nl = ...
    no = ...
    pl = ...
    pt_BR = ...
    ro = ...
    fi = ...
    sv_SE = ...
    vi = ...
    tr = ...
    cs = ...
    el = ...
    bg = ...
    ru = ...
    uk = ...
    hi = ...
    th = ...
    zh_CN = ...
    ja = ...
    zh_TW = ...
    ko = ...


class VideoQualityMode(IntEnum):
    auto = ...
    full = ...


class ComponentType(IntEnum):
    action_row = ...
    button = ...
    select = ...
    string_select = ...
    text_input = ...
    user_select = ...
    role_select = ...
    mentionable_select = ...
    channel_select = ...


class ButtonStyle(IntEnum):
    primary = ...
    secondary = ...
    success = ...
    danger = ...
    link = ...
    blurple = ...
    grey = ...
    gray = ...
    green = ...
    red = ...
    url = ...


class TextInputStyle(IntEnum):
    short = ...
    paragraph = ...


class StagePrivacyLevel(IntEnum):
    public = ...
    closed = ...
    guild_only = ...


class NSFWLevel(IntEnum):
    default = ...
    explicit = ...
    safe = ...
    age_restricted = ...


class ScheduledEventEntityType(IntEnum):
    stage_instance = ...
    voice = ...
    external = ...


class ScheduledEventPrivacyLevel(IntEnum):
    guild_only = ...


class ScheduledEventStatus(IntEnum):
    scheduled = ...
    active = ...
    completed = ...
    canceled = ...
    cancelled = ...


class AutoModerationEventType(IntEnum):
    message_send = ...


class AutoModerationTriggerType(IntEnum):
    keyword = ...
    spam = ...
    keyword_preset = ...
    mention_spam = ...


class KeywordPresetType(IntEnum):
    profanity = ...
    sexual_content = ...
    slurs = ...


class AutoModerationActionType(IntEnum):
    block_message = ...
    send_alert_message = ...
    timeout = ...


class SortOrderType(IntEnum):
    latest_activity = ...
    creation_date = ...


class RoleConnectionMetadataType(IntEnum):
    integer_less_than_or_equal = ...
    integer_greater_than_or_equal = ...
    integer_equal = ...
    integer_not_equal = ...
    datetime_less_than_or_equal = ...
    datetime_greater_than_or_equal = ...
    boolean_equal = ...
    boolean_not_equal = ...


class ForumLayoutType(IntEnum):
    not_set = ...
    list = ...
    gallery = ...


T = TypeVar("T")
def try_enum(cls: Type[T], val: Any) -> T:
    """A function that tries to turn the value into enum ``cls``.

    If it fails it returns a proxy invalid value instead.
    """
    ...
