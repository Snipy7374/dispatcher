"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING
from ..components import Component
from .item import Item
from ..interactions import ClientT, Interaction
from ..state import ConnectionState
from ..types.components import ActionRow as ActionRowPayload

__all__ = ("Modal", "ModalStore")
if TYPE_CHECKING:
    ...
class Modal:
    """Represents a Discord modal popup.

    This object must be inherited to create a modal within Discord.

    .. versionadded:: 2.0

    Parameters
    ----------
    title: :class:`str`
        The title of the modal.
    timeout: Optional[:class:`float`] = None
        Timeout in seconds from last interaction with the UI before no longer accepting input.
        If ``None`` then there is no timeout.
    custom_id: :class:`str` = MISSING
        The ID of the modal that gets received during an interaction.
        If the ``custom_id`` is MISSING, then a random ``custom_id`` is set.
    auto_defer: :class:`bool` = True
        Whether or not to automatically defer the modal when the callback completes
        without responding to the interaction. Set this to ``False`` if you want to
        handle the modal interaction outside of the callback.

    Attributes
    ----------
    title: :class:`str`
        The title of the modal.
    timeout: Optional[:class:`float`]
        Timeout from last interaction with the UI before no longer accepting input.
        If ``None`` then there is no timeout.
    children: List[:class:`Item`]
        The list of children attached to this modal.
    custom_id: :class:`str`
        The ID of the modal that gets received during an interaction.
    auto_defer: :class:`bool` = True
        Whether or not to automatically defer the modal when the callback completes
        without responding to the interaction. Set this to ``False`` if you want to
        handle the modal interaction outside of the callback.
    """
    def __init__(self, title: str, *, timeout: Optional[float] = ..., custom_id: str = ..., auto_defer: bool = ...) -> None:
        ...
    
    def to_components(self) -> List[ActionRowPayload]:
        ...
    
    def to_dict(self) -> Dict[str, Any]:
        ...
    
    def add_item(self, item: Item) -> Modal:
        """Adds an item to the modal.

        Parameters
        ----------
        item: :class:`Item`
            The item to add to the modal.

        Raises
        ------
        TypeError
            An :class:`Item` was not passed.
        ValueError
            The row the item is trying to be added to is full.
        """
        ...
    
    def remove_item(self, item: Item) -> Modal:
        """Removes an item from the modal.

        Parameters
        ----------
        item: :class:`Item`
            The item to remove from the modal.
        """
        ...
    
    def clear_items(self) -> None:
        """Removes all items from the modal."""
        ...
    
    async def callback(self, interaction: Interaction) -> None:
        """|coro|

        The callback that is called when the user press the submit button.

        The default implementation does nothing and the user sees an error
        message on their screen, so you need to overwrite this function.

        Parameters
        ----------
        interaction: :class:`Interaction`
            The interaction fired by the user.

        """
        ...
    
    async def on_timeout(self) -> None:
        """|coro|

        A callback that is called when a modal's timeout elapses without being explicitly stopped.
        """
        ...
    
    async def on_error(self, error: Exception, interaction: Interaction) -> None:
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
        """Stops listening to interaction events from this modal.

        This operation cannot be undone.
        """
        ...
    
    def is_finished(self) -> bool:
        """:class:`bool`: Whether the modal has finished interacting."""
        ...
    
    def is_dispatching(self) -> bool:
        """:class:`bool`: Whether the modal has been added for dispatching purposes."""
        ...
    
    def is_persistent(self) -> bool:
        """:class:`bool`: Whether the modal is set up as persistent.

        A persistent modal has a set ``custom_id`` and all their components with a set ``custom_id`` and
        a :attr:`timeout` set to ``None``.
        """
        ...
    
    async def wait(self) -> bool:
        """Waits until the modal has finished interacting.

        A modal is considered finished when :meth:`stop` is called
        or it times out.

        Returns
        -------
        :class:`bool`
            If ``True``, then the modal timed out. If ``False`` then
            the modal finished normally.
        """
        ...
    


class ModalStore:
    def __init__(self, state: ConnectionState) -> None:
        ...
    
    @property
    def persistent_modals(self) -> List[Modal]:
        ...
    
    def add_modal(self, modal: Modal, user_id: Optional[int] = ...) -> None:
        ...
    
    def remove_modal(self, modal: Modal) -> None:
        ...
    
    def dispatch(self, custom_id: str, interaction: Interaction[ClientT]) -> None:
        ...
    

