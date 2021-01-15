import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random as r
from flask import render_template
import number_maps as googleToSpotify

# testing
clientID = 'PLACEHOLDER_SPOTIFY_CLIENTID'
clientSecret = 'PLACEHOLDER_SPOTIFY_CLIENTSECRET'

client_creds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_creds)

#recoObj = googleToSpotify.spotifySliders(emotions)

def songReco(artistObj, recoObj):
    results = sp.recommendations(limit=3,
                                seed_artists=artistObj,
                                min_danceability=float("{0:.2f}".format(r.uniform(recoObj['danceability'] * .5, recoObj['danceability']))),
                                max_danceability=float("{0:.2f}".format(r.uniform(recoObj['danceability'] * .8, .9))),
                                min_energy=float("{0:.2f}".format(r.uniform(recoObj['energy'] * .6, recoObj['energy']))),
                                max_energy=float("{0:.2f}".format(r.uniform(recoObj['energy'] * .8, .9))),
                                min_valence=float("{0:.2f}".format(r.uniform(recoObj['valence'] * .6, recoObj['valence']))),
                                max_valence=float("{0:.2f}".format(r.uniform(recoObj['valence'] * .8, .9))),
                                min_acoustic=float("{0:.2f}".format(r.uniform(recoObj['acoustic'] * .6, recoObj['acoustic']))),
                                max_acoustic=float("{0:.2f}".format(r.uniform(recoObj['acoustic'] * .8, .9))),
                                min_liveliness=float("{0:.2f}".format(r.uniform(recoObj['liveness'] * .6, recoObj['liveness']))),
                                max_liveliness=float("{0:.2f}".format(r.uniform(recoObj['liveness'] * .8, .9)))
                                )
    return results


def get_artist(artist):
    results = sp.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None



def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])


if __name__ == '__main__':
    
    names = ['Prunk', 'El Funkador', 'Prodot']
    uri_ids = []

    for name in names:
        result = get_artist(name)
        uri_ids.append(result['id'])

    tmp = songReco(uri_ids)
    
    for track in tmp['tracks']:
        print(track['artists'][0]['name'], ' - ', track['name'], '\n\t ', 'Spotify : ', track['external_urls']['spotify'])