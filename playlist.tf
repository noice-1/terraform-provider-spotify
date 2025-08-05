data "spotify_search_track" "acdc" {
  artist = "AC/DC"
}

data "spotify_search_track" "linkinpark" {
  artist = "Linkin Park"
}

data "spotify_search_track" "thewanted" {
  artist = "The Wanted"
}

resource "spotify_playlist" "tf_project" {
  name = "tf project"
  tracks = ["4OROzZUy6gOWN4UGQVaZMF", 
            data.spotify_search_track.acdc.tracks[0].id,
            data.spotify_search_track.linkinpark.tracks[0].id,
            data.spotify_search_track.linkinpark.tracks[1].id,
            data.spotify_search_track.thewanted.tracks[0].id,
            data.spotify_search_track.thewanted.tracks[1].id,
            "47FjToieQbxqNnuiRRQtym",
            "2IvNxLl01CTAfCOA103Tgx",
            "2WfaOiMkCvy7F5fcp2zZ8L",
            "1EjxJHY9A6LMOlvyZdwDly"]
}