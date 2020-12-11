import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)


def set_song_per_id(author, mp3):
    if author in data.keys():
        flag = True
    else:
        flag = False

    data[author] = mp3
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    return flag


def drop_song(author):
    data.pop(author, None)
