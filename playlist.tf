data "spotify_search_track" "acdc" {
  artist = "AC/DC"
}

resource "spotify_playlist" "tf_project" {
  name = "tf project"
  tracks = ["4OROzZUy6gOWN4UGQVaZMF",data.spotify_search_track.acdc.tracks[0].id]
}