"""
This type stub file was generated by pyright.
"""

from typing import ClassVar, List, Optional, Sequence, TYPE_CHECKING
from typing_extensions import Self
from ..components import Component
from .item import Item, ItemCallbackType
from ..interactions import ClientT, Interaction
from ..message import Message
from ..state import ConnectionState
from ..types.components import ActionRow as ActionRowPayload, Component as ComponentPayload

__all__ = ("View", )
if TYPE_CHECKING:
    ...
_log = ...
class _ViewWeights:
    __slots__ = ...
    def __init__(self, children: List[Item]) -> None:
        ...
    
    def find_open_space(self, item: Item) -> int:
        ...
    
    def add_item(self, item: Item) -> None:
        ...
    
    def remove_item(self, item: Item) -> None:
        ...
    
    def clear(self) -> None:
        ...
    


class View:
    """Represents a UI view.

    This object must be inherited to create a UI within Discord.

    .. versionadded:: 2.0

    Parameters
    ----------
    timeout: Optional[:class:`float`]
        Timeout in seconds from last interaction with the UI before no longer accepting input.
        If ``None`` then there is no timeout.
    auto_defer: :class:`bool` = True
        Whether or not to automatically defer the component interaction when the callback
        completes without responding to the interaction. Set this to ``False`` if you want to
        handle view interactions outside of the callback.

    Attributes
    ----------
    timeout: Optional[:class:`float`]
        Timeout from last interaction with the UI before no longer accepting input.
        If ``None`` then there is no timeout.
    children: List[:class:`Item`]
        The list of children attached to this view.
    auto_defer: :class:`bool` = True
        Whether or not to automatically defer the component interaction when the callback
        completes without responding to the interaction. Set this to ``False`` if you want to
        handle view interactions outside of the callback.
    """
    __discord_ui_view__: ClassVar[bool] = ...
    __view_children_items__: ClassVar[List[ItemCallbackType]] = ...
    def __init_subclass__(cls) -> None:
        ...
    
    def __init__(self, *, timeout: Optional[float] = ..., auto_defer: bool = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def to_components(self) -> List[ActionRowPayload]:
        ...
    
    @classmethod
    def from_message(cls, message: Message, /, *, timeout: Optional[float] = ...) -> View:
        """Converts a message's components into a :class:`View`.

        The :attr:`.Message.components` of a message are read-only
        and separate types from those in the ``nextcord.ui`` namespace.
        In order to modify and edit message components they must be
        converted into a :class:`View` first.

        Parameters
        ----------
        message: :class:`nextcord.Message`
            The message with components to convert into a view.
        timeout: Optional[:class:`float`]
            The timeout of the converted view.

        Returns
        -------
        :class:`View`
            The converted view. This always returns a :class:`View` and not
            one of its subclasses.
        """
        ...
    
    def add_item(self, item: Item[Self]) -> None:
        """Adds an item to the view.

        Parameters
        ----------
        item: :class:`Item`
            The item to add to the view.

        Raises
        ------
        TypeError
            An :class:`Item` was not passed.
        ValueError
            Maximum number of children has been exceeded (25)
            or the row the item is trying to be added to is full.
        """
        ...
    
    def remove_item(self, item: Item) -> None:
        """Removes an item from the view.

        Parameters
        ----------
        item: :class:`Item`
            The item to remove from the view.
        """
        ...
    
    def clear_items(self) -> None:
        """Removes all items from the view."""
        ...
    
    async def interaction_check(self, interaction: Interaction) -> bool:
        """|coro|

        A callback that is called when an interaction happens within the view
        that checks whether the view should process item callbacks for the interaction.

        This is useful to override if, for example, you want to ensure that the
        interaction author is a given user.

        The default implementation of this returns ``True``.

        .. note::

            If an exception occurs within the body then the check
            is considered a failure and :meth:`on_error` is called.

        Parameters
        ----------
        interaction: :class:`~nextcord.Interaction`
            The interaction that occurred.

        Returns
        -------
        :class:`bool`
            Whether the view children's callbacks should be called.
        """
        ...
    
    async def on_timeout(self) -> None:
        """|coro|

        A callback that is called when a view's timeout elapses without being explicitly stopped.
        """
        ...
    
    async def on_error(self, error: Exception, item: Item, interaction: Interaction) -> None:
        """|coro|

        A callback that is called when an item's callback or :meth:`interaction_check`
        fails with an error.

        The default implementation prints the traceback to stderr.

        Parameters
        ----------
        error: :class:`Exception`
            The exception that was raised.
        item: :class:`Item`
            The item that failed the dispatch.
        interaction: :class:`~nextcord.Interaction`
            The interaction that led to the failure.
        """
        ...
    
    def refresh(self, components: List[Component]) -> None:
        ...
    
    def stop(self) -> None:
        """Stops listening to interaction events from this view.

        This operation cannot be undone.
        """
        ...
    
    def is_finished(self) -> bool:
        """:class:`bool`: Whether the view has finished interacting."""
        ...
    
    def is_dispatching(self) -> bool:
        """:class:`bool`: Whether the view has been added for dispatching purposes."""
        ...
    
    def is_persistent(self) -> bool:
        """:class:`bool`: Whether the view is set up as persistent.

        A persistent view has all their components with a set ``custom_id`` and
        a :attr:`timeout` set to ``None``.
        """
        ...
    
    async def wait(self) -> bool:
        """Waits until the view has finished interacting.

        A view is considered finished when :meth:`stop` is called
        or it times out.

        Returns
        -------
        :class:`bool`
            If ``True``, then the view timed out. If ``False`` then
            the view finished normally.
        """
        ...
    


class ViewStore:
    def __init__(self, state: ConnectionState) -> None:
        ...
    
    @property
    def persistent_views(self) -> Sequence[View]:
        ...
    
    def add_view(self, view: View, message_id: Optional[int] = ...) -> None:
        ...
    
    def remove_view(self, view: View, message_id: Optional[int] = ...) -> None:
        ...
    
    def dispatch(self, component_type: int, custom_id: str, interaction: Interaction[ClientT]) -> None:
        ...
    
    def is_message_tracked(self, message_id: int) -> bool:
        ...
    
    def remove_message_tracking(self, message_id: int) -> Optional[View]:
        ...
    
    def update_from_message(self, message_id: int, components: List[ComponentPayload]) -> None:
        ...
    

