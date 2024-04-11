from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectTrackAudioFeatures")


@_attrs_define
class SpotifyObjectTrackAudioFeatures:
    """
    Attributes:
        acousticness (float):
        analysis_url (str):
        danceability (float):
        duration_ms (float):
        energy (float):
        id (str):
        instrumentalness (float):
        key (float):
        liveness (float):
        loudness (float):
        mode (float):
        speechiness (float):
        tempo (float):
        time_signature (float):
        track_href (str):
        uri (str):
        valence (float):
    """

    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: float
    energy: float
    id: str
    instrumentalness: float
    key: float
    liveness: float
    loudness: float
    mode: float
    speechiness: float
    tempo: float
    time_signature: float
    track_href: str
    uri: str
    valence: float

    def to_dict(self) -> Dict[str, Any]:
        acousticness = self.acousticness

        analysis_url = self.analysis_url

        danceability = self.danceability

        duration_ms = self.duration_ms

        energy = self.energy

        id = self.id

        instrumentalness = self.instrumentalness

        key = self.key

        liveness = self.liveness

        loudness = self.loudness

        mode = self.mode

        speechiness = self.speechiness

        tempo = self.tempo

        time_signature = self.time_signature

        track_href = self.track_href

        uri = self.uri

        valence = self.valence

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "acousticness": acousticness,
                "analysis_url": analysis_url,
                "danceability": danceability,
                "duration_ms": duration_ms,
                "energy": energy,
                "id": id,
                "instrumentalness": instrumentalness,
                "key": key,
                "liveness": liveness,
                "loudness": loudness,
                "mode": mode,
                "speechiness": speechiness,
                "tempo": tempo,
                "time_signature": time_signature,
                "track_href": track_href,
                "uri": uri,
                "valence": valence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acousticness = d.pop("acousticness")

        analysis_url = d.pop("analysis_url")

        danceability = d.pop("danceability")

        duration_ms = d.pop("duration_ms")

        energy = d.pop("energy")

        id = d.pop("id")

        instrumentalness = d.pop("instrumentalness")

        key = d.pop("key")

        liveness = d.pop("liveness")

        loudness = d.pop("loudness")

        mode = d.pop("mode")

        speechiness = d.pop("speechiness")

        tempo = d.pop("tempo")

        time_signature = d.pop("time_signature")

        track_href = d.pop("track_href")

        uri = d.pop("uri")

        valence = d.pop("valence")

        spotify_object_track_audio_features = cls(
            acousticness=acousticness,
            analysis_url=analysis_url,
            danceability=danceability,
            duration_ms=duration_ms,
            energy=energy,
            id=id,
            instrumentalness=instrumentalness,
            key=key,
            liveness=liveness,
            loudness=loudness,
            mode=mode,
            speechiness=speechiness,
            tempo=tempo,
            time_signature=time_signature,
            track_href=track_href,
            uri=uri,
            valence=valence,
        )

        return spotify_object_track_audio_features
