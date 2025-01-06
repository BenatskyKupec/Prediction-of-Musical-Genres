# This scripts generates data with 

import pandas as pd

path = "spotify_data.csv"


try:
    with open(path, 'r'): pass

except OSError:     # no data, lets download them
    import kagglehub
    # run if data were not downloaded yet
    path = kagglehub.dataset_download("amitanshjoshi/spotify-1million-tracks")      #only to dir
    path = path + "/spotify_data.csv"



data = pd.read_csv(path)

# get rid of the index in csv
data = data.loc[:, data.columns != 'Unnamed: 0']


replace_dict = {
    'black-metal' : 'metal',
    'metalcore' : 'metal',
    'heavy-metal' : 'metal',
    'death-metal' : 'metal',
    'grindcore' : 'metal',

    'rock-n-roll' : 'rock',
    'alt-rock' : 'rock',
    'punk-rock' : 'rock',
    'psych-rock' : 'rock',
    'hard-rock' : 'rock',
    'goth' : 'rock',
    'emo' : 'rock',

    'k-pop' : 'pop',
    'cantopop' : 'pop',
    'power-pop' : 'pop',
    'pop-film' : 'pop',
    'indie-pop' : 'pop',

    'new-age' : 'ambient',
    'sleep' : 'ambient',
    'chill' : 'ambient',

    'dubstep' : 'electro',
    'electronic' : 'electro',
    'edm' : 'electro',
    'detroit-techno' : 'electro',
    'party' : 'electro',
    'dance' : 'electro',
    'techno' : 'electro',
    'garage' : 'electro',
    'disco' : 'electro',
    'trance' : 'electro',
    'hardstyle' : 'electro',
    'drum-and-bass' : 'electro',
    'breakbeat' : 'electro',
    'minimal-techno' : 'electro',
    'dub' : 'electro',
    'hardcore' : 'electro',

    'dancehall' : 'dance',
    'tango' : 'dance',
    'club' : 'dance',
    'salsa' : 'dance',
    'samba' : 'dance',

    'piano' : 'classical',

    'trip-hop' : 'hip-hop',

    'soul' : 'blues',
    'jazz' : 'blues',
    'afrobeat'  : 'blues',
    'ska' : 'blues',

    'guitar' : 'country',
    'acoustic' : 'country',
    'folk' : 'country',
    'sertanejo'  : 'country',

    'gospel' : 'opera',

    'indian' : 'national',
    'spanish' : 'national',
    'french' : 'national',
    'german' : 'national',
    'swedish' : 'national',
    'forro' : 'national',

    'progressive-house' : 'house',
    'chicago-house' : 'house',
    'deep-house' : 'house'
}


data = data.replace(replace_dict)

#list of genres we decided to omit completely
remove_list = ['comedy', 'funk', 'groove', 'industrial', 'punk', 'romance', 'sad', 'show-tunes', 'singer-songwriter', 'songwriter']
data = data[~data['genre'].isin(remove_list)]       #omit selected data

# save the file
data.to_csv('less_genres.csv', index=False)