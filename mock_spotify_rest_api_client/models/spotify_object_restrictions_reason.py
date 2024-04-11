from enum import Enum


class SpotifyObjectRestrictionsReason(str, Enum):
    EXPLICIT = "explicit"
    MARKET = "market"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
