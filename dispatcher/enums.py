"""
MIT License

Copyright (c) 2023 Snipy7374

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from enum import Enum


class Event(Enum):
    """Represents all the discord events.
    These offer to register listeners/events and to dispatch events in a more pythonic way;
    additionally autocompletion and documentation are both supported.
    
    .. versionadded:: 0.0.1
    """

    connect = "connect"
    """Called when the client has successfully connected to Discord.
    Represents the :func:`on_connect` event.
    """
    disconnect = "disconnect"
    """Called when the client has disconnected from Discord, or a connection attempt to Discord has failed.
    Represents the :func:`on_disconnect` event.
    """
    error = "error"
    """Called when an uncaught exception occurred.
    Represents the :func:`on_error` event.
    """
    gateway_error = "gateway_error"
    """Called when a known gateway event cannot be parsed.
    Represents the :func:`on_gateway_error` event.
    """
    ready = "ready"
    """Called when the client is done preparing the data received from Discord.
    Represents the :func:`on_ready` event.
    """
    resumed = "resumed"
    """Called when the client has resumed a session.
    Represents the :func:`on_resumed` event.
    """
    shard_connect = "shard_connect"
    """Called when a shard has successfully connected to Discord.
    Represents the :func:`on_shard_connect` event.
    """
    shard_disconnect = "shard_disconnect"
    """Called when a shard has disconnected from Discord.
    Represents the :func:`on_shard_disconnect` event.
    """
    shard_ready = "shard_ready"
    """Called when a shard has become ready.
    Represents the :func:`on_shard_ready` event.
    """
    shard_resumed = "shard_resumed"
    """Called when a shard has resumed a session.
    Represents the :func:`on_shard_resumed` event.
    """
    socket_event_type = "socket_event_type"
    """Called whenever a websocket event is received from the WebSocket.
    Represents the :func:`on_socket_event_type` event.
    """
    socket_raw_receive = "socket_raw_receive"
    """Called whenever a message is completely received from the WebSocket, before it's processed and parsed.
    Represents the :func:`on_socket_raw_receive` event.
    """
    socket_raw_send = "socket_raw_send"
    """Called whenever a send operation is done on the WebSocket before the message is sent.
    Represents the :func:`on_socket_raw_send` event.
    """
    guild_channel_create = "guild_channel_create"
    """Called whenever a guild channel is created.
    Represents the :func:`on_guild_channel_create` event.
    """
    guild_channel_update = "guild_channel_update"
    """Called whenever a guild channel is updated.
    Represents the :func:`on_guild_channel_update` event.
    """
    guild_channel_delete = "guild_channel_delete"
    """Called whenever a guild channel is deleted.
    Represents the :func:`on_guild_channel_delete` event.
    """
    guild_channel_pins_update = "guild_channel_pins_update"
    """Called whenever a message is pinned or unpinned from a guild channel.
    Represents the :func:`on_guild_channel_pins_update` event.
    """
    invite_create = "invite_create"
    """Called when an :class:`Invite` is created.
    Represents the :func:`.on_invite_create` event.
    """
    invite_delete = "invite_delete"
    """Called when an Invite is deleted.
    Represents the :func:`.on_invite_delete` event.
    """
    private_channel_update = "private_channel_update"
    """Called whenever a private group DM is updated.
    Represents the :func:`on_private_channel_update` event.
    """
    private_channel_pins_update = "private_channel_pins_update"
    """Called whenever a message is pinned or unpinned from a private channel.
    Represents the :func:`on_private_channel_pins_update` event.
    """
    webhooks_update = "webhooks_update"
    """Called whenever a webhook is created, modified, or removed from a guild channel.
    Represents the :func:`on_webhooks_update` event.
    """
    thread_create = "thread_create"
    """Called whenever a thread is created.
    Represents the :func:`on_thread_create` event.
    """
    thread_update = "thread_update"
    """Called when a thread is updated.
    Represents the :func:`on_thread_update` event.
    """
    thread_delete = "thread_delete"
    """Called when a thread is deleted.
    Represents the :func:`on_thread_delete` event.
    """
    thread_join = "thread_join"
    """Called whenever the bot joins a thread or gets access to a thread.
    Represents the :func:`on_thread_join` event.
    """
    thread_remove = "thread_remove"
    """Called whenever a thread is removed. This is different from a thread being deleted.
    Represents the :func:`on_thread_remove` event.
    """
    thread_member_join = "thread_member_join"
    """Called when a `ThreadMember` joins a `Thread`.
    Represents the :func:`on_thread_member_join` event.
    """
    thread_member_remove = "thread_member_remove"
    """Called when a `ThreadMember` leaves a `Thread`.
    Represents the :func:`on_thread_member_remove` event.
    """
    raw_thread_member_remove = "raw_thread_member_remove"
    """Called when a `ThreadMember` leaves `Thread` regardless of the thread member cache.
    Represents the :func:`on_raw_thread_member_remove` event.
    """
    raw_thread_update = "raw_thread_update"
    """Called whenever a thread is updated regardless of the state of the internal thread cache.
    Represents the :func:`on_raw_thread_update` event.
    """
    raw_thread_delete = "raw_thread_delete"
    """Called whenever a thread is deleted regardless of the state of the internal thread cache.
    Represents the :func:`on_raw_thread_delete` event.
    """
    guild_join = "guild_join"
    """Called when a `Guild` is either created by the `Client` or when the Client joins a guild.
    Represents the :func:`on_guild_join` event.
    """
    guild_remove = "guild_remove"
    """Called when a `Guild` is removed from the :class:`Client`.
    Represents the :func:`on_guild_remove` event.
    """
    guild_update = "guild_update"
    """Called when a `Guild` updates.
    Represents the :func:`on_guild_update` event.
    """
    guild_available = "guild_available"
    """Called when a guild becomes available.
    Represents the :func:`on_guild_available` event.
    """
    guild_unavailable = "guild_unavailable"
    """Called when a guild becomes unavailable.
    Represents the :func:`on_guild_unavailable` event.
    """
    guild_role_create = "guild_role_create"
    """Called when a `Guild` creates a new `Role`.
    Represents the :func:`on_guild_role_create` event.
    """
    guild_role_update = "guild_role_update"
    """Called when a `Guild` updates a `Role`.
    Represents the :func:`on_guild_role_update` event.
    """
    guild_role_delete = "guild_role_delete"
    """Called when a `Guild` deletes a `Role`.
    Represents the :func:`on_guild_role_delete` event.
    """
    guild_emojis_update = "guild_emojis_update"
    """Called when a `Guild` adds or removes `Emoji`.
    Represents the :func:`on_guild_emojis_update` event.
    """
    guild_stickers_update = "guild_stickers_update"
    """Called when a `Guild` updates its stickers.
    Represents the :func:`on_guild_stickers_update` event.
    """
    guild_integrations_update = "guild_integrations_update"
    """Called whenever an integration is created, modified, or removed from a guild.
    Represents the :func:`on_guild_integrations_update` event.
    """
    guild_scheduled_event_create = "guild_scheduled_event_create"
    """Called when a guild scheduled event is created.
    Represents the :func:`on_guild_scheduled_event_create` event.
    """
    guild_scheduled_event_update = "guild_scheduled_event_update"
    """Called when a guild scheduled event is updated.
    Represents the :func:`on_guild_scheduled_event_update` event.
    """
    guild_scheduled_event_delete = "guild_scheduled_event_delete"
    """Called when a guild scheduled event is deleted.
    Represents the :func:`on_guild_scheduled_event_delete` event.
    """
    guild_scheduled_event_subscribe = "guild_scheduled_event_subscribe"
    """Called when a user subscribes from a guild scheduled event.
    Represents the :func:`on_guild_scheduled_event_subscribe` event.
    """
    guild_scheduled_event_unsubscribe = "guild_scheduled_event_unsubscribe"
    """Called when a user unsubscribes from a guild scheduled event.
    Represents the :func:`on_guild_scheduled_event_unsubscribe` event.
    """
    raw_guild_scheduled_event_subscribe = "raw_guild_scheduled_event_subscribe"
    """Called when a user subscribes from a guild scheduled event regardless of the guild scheduled event cache.
    Represents the :func:`on_raw_guild_scheduled_event_subscribe` event.
    """
    raw_guild_scheduled_event_unsubscribe = "raw_guild_scheduled_event_unsubscribe"
    """Called when a user subscribes to or unsubscribes from a guild scheduled event regardless of the guild scheduled event cache.
    Represents the :func:`on_raw_guild_scheduled_event_unsubscribe` event.
    """
    application_command_permissions_update = "application_command_permissions_update"
    """Called when the permissions of an application command or the application-wide command permissions are updated.
    Represents the :func:`on_application_command_permissions_update` event.
    """
    automod_action_execution = "automod_action_execution"
    """Called when an auto moderation action is executed due to a rule triggering for a particular event.
    Represents the :func:`on_automod_action_execution` event.
    """
    automod_rule_create = "automod_rule_create"
    """Called when an `AutoModRule` is created.
    Represents the :func:`on_automod_rule_create` event.
    """
    automod_rule_update = "automod_rule_update"
    """Called when an `AutoModRule` is updated.
    Represents the :func:`on_automod_rule_update` event.
    """
    automod_rule_delete = "automod_rule_delete"
    """Called when an `AutoModRule` is deleted.
    Represents the :func:`on_automod_rule_delete` event.
    """
    integration_create = "integration_create"
    """Called when an integration is created.
    Represents the :func:`on_integration_create` event.
    """
    integration_update = "integration_update"
    """Called when an integration is updated.
    Represents the :func:`on_integration_update` event.
    """
    raw_integration_delete = "raw_integration_delete"
    """Called when an integration is deleted.
    Represents the :func:`on_raw_integration_delete` event.
    """
    member_join = "member_join"
    """Called when a `Member` joins a `Guild`.
    Represents the :func:`on_member_join` event.
    """
    member_update = "member_update"
    """Called when a `Member` updates their profile.
    Represents the :func:`on_member_update` event.
    """
    member_remove = "member_remove"
    """Called when a `Member` leaves a `Guild`.
    Represents the :func:`on_member_remove` event.
    """
    raw_member_remove = "raw_member_remove"
    """Called when a member leaves a `Guild` regardless of the member cache.
    Represents the :func:`on_raw_member_remove` event.
    """
    raw_member_update = "raw_member_update"
    """Called when a member updates their profile regardless of the member cache.
    Represents the :func:`on_raw_member_update` event.
    """
    audit_log_entry_create = "audit_log_entry_create"
    """Called when an audit log entry is created.
    Represents the :func:`on_audit_log_entry_create` event.
    """
    member_ban = "member_ban"
    """Called when user gets banned from a `Guild`.
    Represents the :func:`on_member_ban` event.
    """
    member_unban = "member_unban"
    """Called when a `User` gets unbanned from a `Guild`.
    Represents the :func:`on_member_unban` event.
    """
    presence_update = "presence_update"
    """Called when a `Member` updates their presence.
    Represents the :func:`on_presence_update` event.
    """
    user_update = "user_update"
    """Called when a `User` is updated.
    Represents the :func:`on_user_update` event.
    """
    voice_state_update = "voice_state_update"
    """Called when a `Member` changes their `VoiceState`.
    Represents the :func:`on_voice_state_update` event.
    """
    stage_instance_create = "stage_instance_create"
    """Called when a `StageInstance` is created for a `StageChannel`.
    Represents the :func:`on_stage_instance_create` event.
    """
    stage_instance_update = "stage_instance_update"
    """Called when a `StageInstance` is updated.
    Represents the :func:`on_stage_instance_update` event.
    """
    stage_instance_delete = "stage_instance_delete"
    """Called when a `StageInstance` is deleted for a `StageChannel`.
    Represents the :func:`on_stage_instance_delete` event.
    """
    application_command = "application_command"
    """Called when an application command is invoked.
    Represents the :func:`on_application_command` event.
    """
    application_command_autocomplete = "application_command_autocomplete"
    """Called when an application command autocomplete is called.
    Represents the :func:`on_application_command_autocomplete` event.
    """
    button_click = "button_click"
    """Called when a button is clicked.
    Represents the :func:`on_button_click` event.
    """
    dropdown = "dropdown"
    """Called when a select menu is clicked.
    Represents the :func:`on_dropdown` event.
    """
    interaction = "interaction"
    """Called when an interaction happened.
    Represents the :func:`on_interaction` event.
    """
    message_interaction = "message_interaction"
    """Called when a message interaction happened.
    Represents the :func:`on_message_interaction` event.
    """
    modal_submit = "modal_submit"
    """Called when a modal is submitted.
    Represents the :func:`on_modal_submit` event.
    """
    message = "message"
    """Called when a `Message` is created and sent.
    Represents the :func:`on_message` event.
    """
    message_edit = "message_edit"
    """Called when a `Message` receives an update event.
    Represents the :func:`on_message_edit` event.
    """
    message_delete = "message_delete"
    """Called when a message is deleted.
    Represents the :func:`on_message_delete` event.
    """
    bulk_message_delete = "bulk_message_delete"
    """Called when messages are bulk deleted.
    Represents the :func:`on_bulk_message_delete` event.
    """
    raw_message_delete = "raw_message_delete"
    """Called when a message is deleted regardless of the message being in the internal message cache or not.
    Represents the :func:`on_raw_message_delete` event.
    """
    raw_message_edit = "raw_message_edit"
    """Called when a message is edited regardless of the state of the internal message cache.
    Represents the :func:`on_raw_message_edit` event.
    """
    raw_bulk_message_delete = "raw_bulk_message_delete"
    """Called when a bulk delete is triggered regardless of the messages being in the internal message cache or not.
    Represents the :func:`on_raw_bulk_message_delete` event.
    """
    reaction_add = "reaction_add"
    """Called when a message has a reaction added to it.
    Represents the :func:`on_reaction_add` event.
    """
    reaction_remove = "reaction_remove"
    """Called when a message has a reaction removed from it.
    Represents the :func:`on_reaction_remove` event.
    """
    reaction_clear = "reaction_clear"
    """Called when a message has all its reactions removed from it.
    Represents the :func:`on_reaction_clear` event.
    """
    reaction_clear_emoji = "reaction_clear_emoji"
    """Called when a message has a specific reaction removed from it.
    Represents the :func:`on_reaction_clear_emoji` event.
    """
    raw_reaction_add = "raw_reaction_add"
    """Called when a message has a reaction added regardless of the state of the internal message cache.
    Represents the :func:`on_raw_reaction_add` event.
    """
    raw_reaction_remove = "raw_reaction_remove"
    """Called when a message has a reaction removed regardless of the state of the internal message cache.
    Represents the :func:`on_raw_reaction_remove` event.
    """
    raw_reaction_clear = "raw_reaction_clear"
    """Called when a message has all its reactions removed regardless of the state of the internal message cache.
    Represents the :func:`on_raw_reaction_clear` event.
    """
    raw_reaction_clear_emoji = "raw_reaction_clear_emoji"
    """Called when a message has a specific reaction removed from it regardless of the state of the internal message cache.
    Represents the :func:`on_raw_reaction_clear_emoji` event.
    """
    typing = "typing"
    """Called when someone begins typing a message.
    Represents the :func:`on_typing` event.
    """
    raw_typing = "raw_typing"
    """Called when someone begins typing a message regardless of whether `Intents.members` and `Intents.guilds` are enabled.
    Represents the :func:`on_raw_typing` event.
    """
    # ext.commands events
    command = "command"
    """Called when a command is found and is about to be invoked.
    Represents the :func:`.on_command` event.
    """
    command_completion = "command_completion"
    """Called when a command has completed its invocation.
    Represents the :func:`.on_command_completion` event.
    """
    command_error = "command_error"
    """Called when an error is raised inside a command either through user input error, check failure, or an error in your own code.
    Represents the :func:`.on_command_error` event.
    """
    slash_command = "slash_command"
    """Called when a slash command is found and is about to be invoked.
    Represents the :func:`.on_slash_command` event.
    """
    slash_command_completion = "slash_command_completion"
    """Called when a slash command has completed its invocation.
    Represents the :func:`.on_slash_command_completion` event.
    """
    slash_command_error = "slash_command_error"
    """Called when an error is raised inside a slash command either through user input error, check failure, or an error in your own code.
    Represents the :func:`.on_slash_command_error` event.
    """
    user_command = "user_command"
    """Called when a user command is found and is about to be invoked.
    Represents the :func:`.on_user_command` event.
    """
    user_command_completion = "user_command_completion"
    """Called when a user command has completed its invocation.
    Represents the :func:`.on_user_command_completion` event.
    """
    user_command_error = "user_command_error"
    """Called when an error is raised inside a user command either through check failure, or an error in your own code.
    Represents the :func:`.on_user_command_error` event.
    """
    message_command = "message_command"
    """Called when a message command is found and is about to be invoked.
    Represents the :func:`.on_message_command` event.
    """
    message_command_completion = "message_command_completion"
    """Called when a message command has completed its invocation.
    Represents the :func:`.on_message_command_completion` event.
    """
    message_command_error = "message_command_error"
    """Called when an error is raised inside a message command either through check failure, or an error in your own code.
    Represents the :func:`.on_message_command_error` event.
    """