import random as r
import math

# Sigmoid
def sigmoid(x):
    return 1/(1 + math.exp(-x))

# softmax
def softmax(x):
    return x/(math.fabs(x) + 1)


# return tag for low energy, neutral, upbeat, ambivalent
def mood_spectrum(jassObject):
    if jassObject['joy'] > 3 and jassObject['sorrow'] < 3:
        return 'upbeat'
    if jassObject['sorrow'] > 2 or jassObject['joy'] < 4:
        return 'neutral'
    if jassObject['anger'] > 3 or jassObject['joy'] > 3:
        return 'phase'
    else:
        return 'ambivalent'

# mood factor -- multiplier for spotify levels  (0 - 1); 1 = positive
def mood_factor(tag):
    if tag == 'upbeat':
        return 0.5
    if tag == 'neutral':
        return (.01 * r.randint(0,10))
    if tag == 'phase':
        return (.0069 * r.randint(1,5))
    if tag == 'ambivalent':
        return (.00042069 * r.randint(1,69))

# direct multipliers
#step 1
def spotifySliders(jassObject):
    
    joy, anger, sorrow, surprise = jassObject.values()
    trackParameters = { 'danceability' : 0,
                    'energy' : 0,
                    'valence' : 0,
                    'acoustic' : 0,
                    'liveness' : 0
                    }

    mFactor = mood_factor(mood_spectrum(jassObject)) * r.randint(-1,1)
    print('mFactor : ', mFactor)
    trackParameters['danceability'] = r.uniform(sigmoid(joy/5 + softmax(anger * mFactor)), .9) + mFactor * 1/sorrow * 0.5
    
    trackParameters['energy'] = math.fabs(r.uniform((0.8 * (joy/5 + anger/5) + mFactor * (anger/joy)) * .7, .99))

    trackParameters['valence'] = math.fabs(((sorrow/5) * .5) + ((1/joy) * .3) + r.uniform(softmax(anger), 1) * mFactor)
    trackParameters['acoustic'] = r.uniform((math.fabs(sorrow/5 + .2 * joy/5)* 0.75), .9)

    trackParameters['liveness'] = r.uniform(math.fabs(softmax(sorrow)), .8) + mFactor * r.uniform(sigmoid(joy) * 0.4, .7)

    # goes into spotify's api call
    return trackParameters