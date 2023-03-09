__all__ = (
    "MultipleCompatibleLibraries",
    "NoCompatibleLibraries",
)


class MultipleCompatibleLibraries(Exception):
    def __init__(self, libs, *args, **kwargs):
        super().__init__("Multiple compatible libraries found: " + ", ".join(libs), *args, **kwargs)


class NoCompatibleLibraries(Exception):
    def __init__(self, libs, *args, **kwargs):
        super().__init__(
            "No compatible libraries found."
            "The compatible libraries are:"
            ", ".join(libs), *args, **kwargs,
        )
