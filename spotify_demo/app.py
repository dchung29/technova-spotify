from flask import Flask, request, url_for, session, redirect
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

technova_demo = Flask(__name__)

technova_demo.secret_key = "qvudb83q7dgbadxn"
technova_demo.config['SESSION_COOKIE'] = 'randomcookie'


@technova_demo.route('/')
def login():
    sp_oauth = spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@technova_demo.route('/authorize')
def authorize():
    sp_oauth = spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_code = sp_oauth.get_access_token(code)
    session["token_code"] = token_code
    return redirect('/get_favourites')

@technova_demo.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

@technova_demo.route('/get_favourites')
def get_favourites():
    session['token_code']
    authorized = get_token()
    session.modified = True
    if not authorized:
        return redirect('/')

    sp = spotipy.Spotify(auth=session.get('token_code').get('access_token'))

    user_id = sp.current_user()["id"]
    sp.user_playlist_create(user_id, "Music Therapy", public=False, description="A playlist to help you relax")

    playlist_id = sp.current_user_playlists(limit=50, offset=0)['items']
    true_playlist_id = ""
    for y, item2 in enumerate(playlist_id):
        name12 = item2["name"]
        if name12 == "Music Therapy":
            true_playlist_id = item2["id"]


    it = 0

    sp_list = []
    sp_list1 = []
    sp_list2 = []
    sp_list3 = []
    sp_list4 = []
    sp_list5 = []
    sp_list6 = []
    sp_list7 = []
    sp_list8 = []
    sp_list9 = []
    sp_list10 = []

    while it<100:
        offset = it * 50
        it += 1
        songs = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
        for i, item in enumerate(songs):
            track = item['track']
            song = track['id']
            sp_list.append(song)

    for num in range(0, 99):
        sp_list1.append(sp_list[num])
    if len(sp_list) > 200:
        for num1 in range(100, 199):
            sp_list2.append(sp_list[num1])
    if len(sp_list) > 300:
        for num2 in range(200, 299):
            sp_list3.append(sp_list[num2])
    if len(sp_list) > 400:
        for num3 in range(300, 399):
            sp_list4.append(sp_list[num3])
    if len(sp_list) > 500:
        for num4 in range(400, 499):
            sp_list5.append(sp_list[num4])
    if len(sp_list) > 600:
        for num5 in range(500, 599):
            sp_list6.append(sp_list[num5])
    if len(sp_list) > 700:
        for num6 in range(600, 699):
            sp_list7.append(sp_list[num6])
    if len(sp_list) > 800:
        for num7 in range(700, 799):
            sp_list8.append(sp_list[num7])
    if len(sp_list) > 900:
        for num8 in range(800, 899):
            sp_list9.append(sp_list[num8])
    if len(sp_list) > 1000:
        for num9 in range(900, 999):
            sp_list10.append(sp_list[num9])

    therapy1 = sp.audio_features(tracks=sp_list1)
    therapy2 = sp.audio_features(tracks=sp_list2)
    therapy3 = sp.audio_features(tracks=sp_list3)
    therapy4 = sp.audio_features(tracks=sp_list4)
    therapy5 = sp.audio_features(tracks=sp_list5)
    therapy6 = sp.audio_features(tracks=sp_list6)
    therapy7 = sp.audio_features(tracks=sp_list7)
    therapy8 = sp.audio_features(tracks=sp_list8)
    therapy9 = sp.audio_features(tracks=sp_list9)
    therapy10 = sp.audio_features(tracks=sp_list10)

    therapy0 = []
    for key in therapy1:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy2:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy3:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy4:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy5:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy6:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy7:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy8:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy9:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy10:
        if key["danceability"] > 0.7 and key["energy"] > 0.7 and key["valence"] > 0.7 and key["tempo"] > 100:
            therapy0.append(key['id'])
    for key in therapy1:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy2:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy3:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy4:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy5:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy6:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy7:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy8:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy9:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy10:
        if key["danceability"] <= 0.7 and key["danceability"] > 0.5 and key["energy"] <= 0.7 and key["energy"] > 0.5 and key["valence"] <= 0.9 and key["valence"] > 0.5 and key["tempo"] <= 100 and key["tempo"] > 70:
            therapy0.append(key['id'])
    for key in therapy1:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy2:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy3:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy4:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy5:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy6:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy7:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy8:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy9:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.7 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy10:
        if key["danceability"] <= 0.5 and key["danceability"] > 0.2 and key["energy"] <= 0.5 and key["energy"] > 0.2 and key["valence"] <= 0.5 and key["valence"] > 0.4 and key["tempo"] <= 70 and key["tempo"] > 40:
            therapy0.append(key['id'])
    for key in therapy1:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy2:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy3:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy4:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy5:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy6:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy7:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy8:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy9:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])
    for key in therapy10:
        if key["danceability"] <= 0.2 and key["danceability"] > 0.0 and key["energy"] <= 0.2 and key["energy"] > 0.0 and key["valence"] <= 0.7 and key["valence"] > 0.2 and key["tempo"] <= 40:
            therapy0.append(key['id'])



    sp.playlist_add_items(true_playlist_id, therapy0, position=None)
    print(therapy0)
    return "Your music therapy playlist has been created!"


def get_token():
    token_valid = False
    token_code = session.get("token_code", {})

    if not (session.get('token_code', False)):
        token_valid = False
        return token_code, token_valid

    now = int(time.time())
    is_token_expired = session.get('token_code').get('expires_at') - now < 60

    if (is_token_expired):
        sp_oauth = spotify_oauth()
        token_code = sp_oauth.refresh_access_token(session.get('token_code').get('refresh_token'))

    token_valid = True
    return token_code, token_valid


def spotify_oauth():
    return SpotifyOAuth(
    client_id = 'fb7c72d2df014306b147b5c36053c8d5',
    client_secret = 'e3b7876e53254e149be847ced22e2e3a',
    redirect_uri = url_for('authorize', _external=True),
    scope = 'user-top-read playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-modify user-library-read user-read-private'
    )
