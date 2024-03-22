from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_device import SpotifyObjectDevice


T = TypeVar("T", bound="SpotifyObjectListdevicesSpotifyObjectDevice")


@_attrs_define
class SpotifyObjectListdevicesSpotifyObjectDevice:
    """
    Attributes:
        devices (List['SpotifyObjectDevice']):
    """

    devices: List["SpotifyObjectDevice"]

    def to_dict(self) -> Dict[str, Any]:
        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()
            devices.append(devices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "devices": devices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_device import SpotifyObjectDevice

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = SpotifyObjectDevice.from_dict(devices_item_data)

            devices.append(devices_item)

        spotify_object_listdevices_spotify_object_device = cls(
            devices=devices,
        )

        return spotify_object_listdevices_spotify_object_device
