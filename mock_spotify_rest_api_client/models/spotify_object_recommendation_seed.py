from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_recommendation_seed_type import (
    SpotifyObjectRecommendationSeedType,
)

T = TypeVar("T", bound="SpotifyObjectRecommendationSeed")


@_attrs_define
class SpotifyObjectRecommendationSeed:
    """
    Attributes:
        after_filtering_size (float):
        after_relinking_size (float):
        href (str):
        id (str):
        initial_pool_size (float):
        type (SpotifyObjectRecommendationSeedType):
    """

    after_filtering_size: float
    after_relinking_size: float
    href: str
    id: str
    initial_pool_size: float
    type: SpotifyObjectRecommendationSeedType

    def to_dict(self) -> Dict[str, Any]:
        after_filtering_size = self.after_filtering_size

        after_relinking_size = self.after_relinking_size

        href = self.href

        id = self.id

        initial_pool_size = self.initial_pool_size

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "afterFilteringSize": after_filtering_size,
                "afterRelinkingSize": after_relinking_size,
                "href": href,
                "id": id,
                "initialPoolSize": initial_pool_size,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after_filtering_size = d.pop("afterFilteringSize")

        after_relinking_size = d.pop("afterRelinkingSize")

        href = d.pop("href")

        id = d.pop("id")

        initial_pool_size = d.pop("initialPoolSize")

        type = SpotifyObjectRecommendationSeedType(d.pop("type"))

        spotify_object_recommendation_seed = cls(
            after_filtering_size=after_filtering_size,
            after_relinking_size=after_relinking_size,
            href=href,
            id=id,
            initial_pool_size=initial_pool_size,
            type=type,
        )

        return spotify_object_recommendation_seed
