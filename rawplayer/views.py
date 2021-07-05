from django.shortcuts import render
from .models import Song, Watchlater, History
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Case, When
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


def spotify(request):
    if request.method == "POST":
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='8c3fc57d3350441d863127b99923691b', client_secret='93a61c4d871c44f39afe49c148a86a51',))
        results = spotify.artist_top_tracks(artist_uri)
        output=results['tracks'][:8]
        return render(request,'rawplayer/spotify.htm', {"results":output})
    else:
        return render(request,'rawplayer/spotify.htm',)
    

def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    str1 = query
    qs = []
    word = str1.split()
    word2 = []

    for i in song:
        word2 = i.name.split()

        for j in word:
            if j in word2 or j.capitalize() in word2 or j.upper() in word2:
                qs.append(i)

    return render(request, 'rawplayer/search.htm', {"songs": qs, "query": query})


def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/rawplayer/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'rawplayer/history.htm', {"history": song})


def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "This track is in your checklist already"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "You have successfully added this track in checklist"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"rawplayer/songpost.htm", {'song': song, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "rawplayer/watchlater.htm", {'song': song})

def index(request):
    song = Song.objects.all()
    print(song)
    li1 =[]
    for i in song:
        li1.append(i.trend)
        
        print(i.name, i.trend)
    return render(request, 'index.htm', {'song': song},{'çontext1':li1})


def songs(request):
    song = Song.objects.all()
    
    return render(request, 'rawplayer/songs.htm', {'song': song})


def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'rawplayer/songpost.htm', {'song': song})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)   
        return redirect('/')

    return render(request, 'rawplayer/login.htm')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        user = authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)

        return redirect('/')
    return render(request, 'rawplayer/signup.htm')


def logout_user(request):
    logout(request)
    return redirect("/")

def contact(request):
    return render(request, 'rawplayer/contact.htm')


