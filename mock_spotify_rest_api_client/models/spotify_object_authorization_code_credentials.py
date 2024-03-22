from typing import Any, Dict, Literal, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectAuthorizationCodeCredentials")


@_attrs_define
class SpotifyObjectAuthorizationCodeCredentials:
    """
    Attributes:
        access_token (str):
        expires_in (float):
        refresh_token (str):
        scope (str):
        token_type (Literal['Bearer']):
    """

    access_token: str
    expires_in: float
    refresh_token: str
    scope: str
    token_type: Literal["Bearer"]

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        expires_in = self.expires_in

        refresh_token = self.refresh_token

        scope = self.scope

        token_type = self.token_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "access_token": access_token,
                "expires_in": expires_in,
                "refresh_token": refresh_token,
                "scope": scope,
                "token_type": token_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        expires_in = d.pop("expires_in")

        refresh_token = d.pop("refresh_token")

        scope = d.pop("scope")

        token_type = d.pop("token_type")

        spotify_object_authorization_code_credentials = cls(
            access_token=access_token,
            expires_in=expires_in,
            refresh_token=refresh_token,
            scope=scope,
            token_type=token_type,
        )

        return spotify_object_authorization_code_credentials
