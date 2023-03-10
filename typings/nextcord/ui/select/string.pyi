"""
This type stub file was generated by pyright.
"""

from typing import Callable, Generic, List, Optional, TYPE_CHECKING, Tuple, TypeVar, Union
from ...components import SelectOption, StringSelectMenu
from ...emoji import Emoji
from ...interactions import ClientT
from ...partial_emoji import PartialEmoji
from ..item import ItemCallbackType
from .base import SelectBase
from typing_extensions import Self

if TYPE_CHECKING:
    ...
__all__ = ("Select", "select", "StringSelect", "string_select")
V = TypeVar("V", bound="View", covariant=True)
class StringSelect(SelectBase, Generic[V]):
    """Represents a UI string select menu.

    This is usually represented as a drop down menu.

    In order to get the selected items that the user has chosen, use :attr:`StringSelect.values`.

    There is an alias for this class called ``Select``.

    .. versionadded:: 2.0

    Parameters
    ----------
    custom_id: :class:`str`
        The ID of the select menu that gets received during an interaction.
        If not given then one is generated for you.
    placeholder: Optional[:class:`str`]
        The placeholder text that is shown if nothing is selected, if any.
    min_values: :class:`int`
        The minimum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    max_values: :class:`int`
        The maximum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    options: List[:class:`.SelectOption`]
        A list of options that can be selected in this menu.
    disabled: :class:`bool`
        Whether the select is disabled or not.
    row: Optional[:class:`int`]
        The relative row this select menu belongs to. A Discord component can only have 5
        rows. By default, items are arranged automatically into those 5 rows. If you'd
        like to control the relative positioning of the row then passing an index is advised.
        For example, row=1 will show up before row=2. Defaults to ``None``, which is automatic
        ordering. The row number must be between 0 and 4 (i.e. zero indexed).
    """
    __item_repr_attributes__: Tuple[str, ...] = ...
    def __init__(self, *, custom_id: str = ..., placeholder: Optional[str] = ..., min_values: int = ..., max_values: int = ..., options: List[SelectOption] = ..., disabled: bool = ..., row: Optional[int] = ...) -> None:
        ...
    
    @property
    def options(self) -> List[SelectOption]:
        """List[:class:`.SelectOption`]: A list of options that can be selected in this menu."""
        ...
    
    @options.setter
    def options(self, value: List[SelectOption]) -> None:
        ...
    
    def add_option(self, *, label: str, value: str = ..., description: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., default: bool = ...) -> None:
        """Adds an option to the select menu.

        To append a pre-existing :class:`.SelectOption` use the
        :meth:`append_option` method instead.

        Parameters
        ----------
        label: :class:`str`
            The label of the option. This is displayed to users.
            Can only be up to 100 characters.
        value: :class:`str`
            The value of the option. This is not displayed to users.
            If not given, defaults to the label. Can only be up to 100 characters.
        description: Optional[:class:`str`]
            An additional description of the option, if any.
            Can only be up to 100 characters.
        emoji: Optional[Union[:class:`str`, :class:`.Emoji`, :class:`.PartialEmoji`]]
            The emoji of the option, if available. This can either be a string representing
            the custom or unicode emoji or an instance of :class:`.PartialEmoji` or :class:`.Emoji`.
        default: :class:`bool`
            Whether this option is selected by default.

        Raises
        ------
        ValueError
            The number of options exceeds 25.
        """
        ...
    
    def append_option(self, option: SelectOption) -> None:
        """Appends an option to the select menu.

        Parameters
        ----------
        option: :class:`.SelectOption`
            The option to append to the select menu.

        Raises
        ------
        ValueError
            The number of options exceeds 25.
        """
        ...
    
    @classmethod
    def from_component(cls, component: StringSelectMenu) -> Self:
        ...
    


def string_select(*, placeholder: Optional[str] = ..., custom_id: str = ..., min_values: int = ..., max_values: int = ..., options: List[SelectOption] = ..., disabled: bool = ..., row: Optional[int] = ...) -> Callable[[ItemCallbackType[StringSelect[V], ClientT]], ItemCallbackType[StringSelect[V], ClientT]]:
    """A decorator that attaches a string select menu to a component.

    There is an alias for this function called ``select``.

    The function being decorated should have three parameters, ``self`` representing
    the :class:`.ui.View`, the :class:`.ui.StringSelect` being pressed and
    the :class:`.Interaction` you receive.

    In order to get the selected items that the user has chosen within the callback
    use :attr:`StringSelect.values`.

    Parameters
    ----------
    placeholder: Optional[:class:`str`]
        The placeholder text that is shown if nothing is selected, if any.
    custom_id: :class:`str`
        The ID of the select menu that gets received during an interaction.
        It is recommended not to set this parameter to prevent conflicts.
    row: Optional[:class:`int`]
        The relative row this select menu belongs to. A Discord component can only have 5
        rows. By default, items are arranged automatically into those 5 rows. If you'd
        like to control the relative positioning of the row then passing an index is advised.
        For example, row=1 will show up before row=2. Defaults to ``None``, which is automatic
        ordering. The row number must be between 0 and 4 (i.e. zero indexed).
    min_values: :class:`int`
        The minimum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    max_values: :class:`int`
        The maximum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    options: List[:class:`.SelectOption`]
        A list of options that can be selected in this menu.
    disabled: :class:`bool`
        Whether the select is disabled or not. Defaults to ``False``.
    """
    ...

Select = StringSelect
select = ...