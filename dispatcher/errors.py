__all__ = (
    "MultipleCompatibleLibraries",
    "NoCompatibleLibraries",
)


class MultipleCompatibleLibraries(Exception):
    def __init__(self, libs, *args, **kwargs):
        super().__init__("Multiple compatible libraries found: " + ", ".join(libs), *args, **kwargs)


class NoCompatibleLibraries(Exception):
    pass
