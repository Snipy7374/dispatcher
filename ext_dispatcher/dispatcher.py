

class Dispatcher:
    """A class that handles dispatch logic for you.

    .. versionadded:: 0.0.1

    Parameters
    ----------
    bot: ?
    """
    def __init__(self, bot):
        self.bot = bot
        pass

    def dispatch(self, event_name: str, *args, **kwargs) -> None:
        """A method to dispatch custom events.

        .. versionaddeed:: 0.0.1

        Parameters
        ----------

        event_name: :class:`str`
        *args: Any
        **kwargs: Any
        """
        pass