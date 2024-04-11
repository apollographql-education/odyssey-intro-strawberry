from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.spotify_object_paginated_spotify_object_playlist_track import (
    SpotifyObjectPaginatedSpotifyObjectPlaylistTrack,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/playlists/{playlist_id}/tracks".format(
            playlist_id=playlist_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SpotifyObjectPaginatedSpotifyObjectPlaylistTrack.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    """Get full details of the items of a playlist owned by a Spotify user.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    """Get full details of the items of a playlist owned by a Spotify user.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    """Get full details of the items of a playlist owned by a Spotify user.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]]:
    """Get full details of the items of a playlist owned by a Spotify user.

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack]
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
        )
    ).parsed
