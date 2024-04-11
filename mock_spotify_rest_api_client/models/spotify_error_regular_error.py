from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_error_regular_error_error import SpotifyErrorRegularErrorError


T = TypeVar("T", bound="SpotifyErrorRegularError")


@_attrs_define
class SpotifyErrorRegularError:
    """
    Attributes:
        error (SpotifyErrorRegularErrorError):
    """

    error: "SpotifyErrorRegularErrorError"

    def to_dict(self) -> Dict[str, Any]:
        error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_error_regular_error_error import (
            SpotifyErrorRegularErrorError,
        )

        d = src_dict.copy()
        error = SpotifyErrorRegularErrorError.from_dict(d.pop("error"))

        spotify_error_regular_error = cls(
            error=error,
        )

        return spotify_error_regular_error
