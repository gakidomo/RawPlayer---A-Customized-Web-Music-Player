# RawPlayer
## Music Utility Website for Casual Usage

RawPlayer is a music player and music utility based website .
Developed by Maruf Raihan Anannyo and Sayad Alam Siam .

- Basic Features for a Music website enabled
- Simplified UI Design
- ✨SpotiPy - Usage of Spotify API✨

## Features

- Listen to Music from our website
- Add music to checklist for later listening
- History record feature for enabling browsing past actions
- Use Spotify link of Artists to get music details and informations
- Get to know Trending and Recommendations from our website 

## Tech

RawPlayer's internal technological parameters are presented here - 

- [Django] - Python Framework used to develop the structure of our web application
- [HTML5] - For the webpage design and creating interrelation
- [BootStrap] - Using already provided open source html code snippets for smoother development
- [SpotiPY] - Spotify API for Python language integrated to our app 
- [MySQL] - Django provided Back-end Database


## Installation

RawPlayer needs first your system to install pip and Django simultaneously first.
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

To install Django  
```
pip install django
```
Then run the server on powershell or CMD and Type the given Cloned IP to preview the website
```
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

You need to install Spotify API for SpotiPY integration

```
pip install spotipy --upgrade
```
Go to https://developers.spotify.com and create a developer's account to get token ID for your application.



## Future Development Plans

- To Add more features like Playlist , TopChart etc.
- Integrating more established music libraries like Tidal, Deezer, YouTube Music etc.
- Make the UI more flashy and eye-catching
- Enhancing the site security by adding Captcha , Anti D-Dos precautions.
