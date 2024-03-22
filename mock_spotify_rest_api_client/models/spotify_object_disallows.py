from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyObjectDisallows")


@_attrs_define
class SpotifyObjectDisallows:
    """
    Attributes:
        interrupting_playback (Union[Unset, bool]):
        pausing (Union[Unset, bool]):
        resuming (Union[Unset, bool]):
        seeking (Union[Unset, bool]):
        skipping_next (Union[Unset, bool]):
        skipping_prev (Union[Unset, bool]):
        toggling_repeat_context (Union[Unset, bool]):
        toggling_shuffle (Union[Unset, bool]):
        toggling_repeat_track (Union[Unset, bool]):
        transferring_playback (Union[Unset, bool]):
    """

    interrupting_playback: Union[Unset, bool] = UNSET
    pausing: Union[Unset, bool] = UNSET
    resuming: Union[Unset, bool] = UNSET
    seeking: Union[Unset, bool] = UNSET
    skipping_next: Union[Unset, bool] = UNSET
    skipping_prev: Union[Unset, bool] = UNSET
    toggling_repeat_context: Union[Unset, bool] = UNSET
    toggling_shuffle: Union[Unset, bool] = UNSET
    toggling_repeat_track: Union[Unset, bool] = UNSET
    transferring_playback: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        interrupting_playback = self.interrupting_playback

        pausing = self.pausing

        resuming = self.resuming

        seeking = self.seeking

        skipping_next = self.skipping_next

        skipping_prev = self.skipping_prev

        toggling_repeat_context = self.toggling_repeat_context

        toggling_shuffle = self.toggling_shuffle

        toggling_repeat_track = self.toggling_repeat_track

        transferring_playback = self.transferring_playback

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if interrupting_playback is not UNSET:
            field_dict["interrupting_playback"] = interrupting_playback
        if pausing is not UNSET:
            field_dict["pausing"] = pausing
        if resuming is not UNSET:
            field_dict["resuming"] = resuming
        if seeking is not UNSET:
            field_dict["seeking"] = seeking
        if skipping_next is not UNSET:
            field_dict["skipping_next"] = skipping_next
        if skipping_prev is not UNSET:
            field_dict["skipping_prev"] = skipping_prev
        if toggling_repeat_context is not UNSET:
            field_dict["toggling_repeat_context"] = toggling_repeat_context
        if toggling_shuffle is not UNSET:
            field_dict["toggling_shuffle"] = toggling_shuffle
        if toggling_repeat_track is not UNSET:
            field_dict["toggling_repeat_track"] = toggling_repeat_track
        if transferring_playback is not UNSET:
            field_dict["transferring_playback"] = transferring_playback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interrupting_playback = d.pop("interrupting_playback", UNSET)

        pausing = d.pop("pausing", UNSET)

        resuming = d.pop("resuming", UNSET)

        seeking = d.pop("seeking", UNSET)

        skipping_next = d.pop("skipping_next", UNSET)

        skipping_prev = d.pop("skipping_prev", UNSET)

        toggling_repeat_context = d.pop("toggling_repeat_context", UNSET)

        toggling_shuffle = d.pop("toggling_shuffle", UNSET)

        toggling_repeat_track = d.pop("toggling_repeat_track", UNSET)

        transferring_playback = d.pop("transferring_playback", UNSET)

        spotify_object_disallows = cls(
            interrupting_playback=interrupting_playback,
            pausing=pausing,
            resuming=resuming,
            seeking=seeking,
            skipping_next=skipping_next,
            skipping_prev=skipping_prev,
            toggling_repeat_context=toggling_repeat_context,
            toggling_shuffle=toggling_shuffle,
            toggling_repeat_track=toggling_repeat_track,
            transferring_playback=transferring_playback,
        )

        return spotify_object_disallows
