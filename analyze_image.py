import os
import io
from google.cloud import vision
from flask import redirect, render_template
import number_maps as GoogleToSpotify
import spotipy_calls
import random as r


def facesearch(filepath, artist):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'service-account-token.json'

    client = vision.ImageAnnotatorClient()

    # image file
    image_location = filepath

    with io.open(image_location, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Numerical definition for calc
    likelihood_name = (-1, 1, 2, 3, 4, 5)

    emotions = {'joy': [],
                'anger': [],
                'sorrow': [],
                'surprise': []
                }

    num_faces = len(faces)

    if num_faces > 1:

        for face in faces:
            emotions['joy'].append(likelihood_name[face.joy_likelihood])
            emotions['anger'].append(likelihood_name[face.anger_likelihood])
            emotions['sorrow'].append(likelihood_name[face.sorrow_likelihood])
            emotions['surprise'].append(likelihood_name[face.surprise_likelihood])

        joy = sum(emotions['joy'])/len(emotions['joy'])
        anger = sum(emotions['anger'])/len(emotions['anger'])
        sorrow = sum(emotions['sorrow'])/len(emotions['sorrow'])
        surprise = sum(emotions['surprise'])/len(emotions['surprise'])

        emotions = {'joy' : joy,
                'anger' : anger,
                'sorrow' : sorrow,
                'surprise' : surprise
                }
    elif num_faces == 1:
        emotions = {'joy' : likelihood_name[faces[0].joy_likelihood],
                'anger' : likelihood_name[faces[0].anger_likelihood],
                'sorrow' : likelihood_name[faces[0].sorrow_likelihood],
                'surprise' : likelihood_name[faces[0].surprise_likelihood]
                }



    names = ['Prunk', 'Drake', 'Paramore', 'Kartell', 'Linkin Park', 'Mac Miller', 'Darius', 'Moon Boots', 'Claire', 'KAYTRANADA', 'Smino', 'Joe Hertz', 'Cheekface', 'Still Woozy', 'Talking Heads', 'Chvrches']
    uri_ids = []

    for i in range(0,2):
        result = spotipy_calls.get_artist(r.choice(names))
        uri_ids.append(result['id'])

    artistobj = spotipy_calls.get_artist(artist)

    uri_ids.append(artistobj['id'])
    recoobj = GoogleToSpotify.spotifySliders(emotions)
    tracks = spotipy_calls.songReco(uri_ids, recoobj)

    artist_list = []
    track_list = []
    links = []

    for track in tracks['tracks']:
        artist_list.append(track['artists'][0]['name'])
        track_list.append(track['name'])
        links.append(track['external_urls']['spotify'])

    final_list = []
    for i in range(0, len(track_list)):
        final_list.append(track_list[i])
        final_list.append(artist_list[i])
        final_list.append(links[i])

    return render_template('results.html', title='results', value=final_list)