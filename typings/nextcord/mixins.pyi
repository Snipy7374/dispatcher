"""
This type stub file was generated by pyright.
"""

from typing import List, TYPE_CHECKING
from .message import Message
from .state import ConnectionState

if TYPE_CHECKING:
    ...
__all__ = ("EqualityComparable", "Hashable", "PinsMixin")
class EqualityComparable:
    __slots__ = ...
    id: int
    def __eq__(self, other: object) -> bool:
        ...
    
    def __ne__(self, other: object) -> bool:
        ...
    


class Hashable(EqualityComparable):
    __slots__ = ...
    def __hash__(self) -> int:
        ...
    


class PinsMixin:
    __slots__ = ...
    _state: ConnectionState
    async def pins(self) -> List[Message]:
        """|coro|

        Retrieves all messages that are currently pinned in the channel.

        .. note::

            Due to a limitation with the Discord API, the :class:`.Message`
            objects returned by this method do not contain complete
            :attr:`.Message.reactions` data.

        Raises
        ------
        ~nextcord.HTTPException
            Retrieving the pinned messages failed.

        Returns
        -------
        List[:class:`~nextcord.Message`]
            The messages that are currently pinned.
        """
        ...
    


