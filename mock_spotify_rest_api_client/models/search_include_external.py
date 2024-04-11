from enum import Enum


class SearchIncludeExternal(str, Enum):
    AUDIO = "audio"

    def __str__(self) -> str:
        return str(self.value)
