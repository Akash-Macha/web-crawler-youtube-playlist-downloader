import pytube as pt


def download_playlist_and_get_video_titles(url, path):
    p = pt.Playlist(url)

    titles = []
    for video in p.videos:
        titles.append(video.title)
        video.streams.get_by_resolution(resolution='720p').download(output_path=path)

    return titles
