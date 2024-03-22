from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_track_audio_features import (
        SpotifyObjectTrackAudioFeatures,
    )


T = TypeVar("T", bound="SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures")


@_attrs_define
class SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures:
    """
    Attributes:
        audio_features (List['SpotifyObjectTrackAudioFeatures']):
    """

    audio_features: List["SpotifyObjectTrackAudioFeatures"]

    def to_dict(self) -> Dict[str, Any]:
        audio_features = []
        for audio_features_item_data in self.audio_features:
            audio_features_item = audio_features_item_data.to_dict()
            audio_features.append(audio_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "audio_features": audio_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spotify_object_track_audio_features import (
            SpotifyObjectTrackAudioFeatures,
        )

        d = src_dict.copy()
        audio_features = []
        _audio_features = d.pop("audio_features")
        for audio_features_item_data in _audio_features:
            audio_features_item = SpotifyObjectTrackAudioFeatures.from_dict(
                audio_features_item_data
            )

            audio_features.append(audio_features_item)

        spotify_object_listaudio_features_spotify_object_track_audio_features = cls(
            audio_features=audio_features,
        )

        return spotify_object_listaudio_features_spotify_object_track_audio_features
