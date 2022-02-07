from decouple import config
import requests
import base64
from tqdm import tqdm
import time
import shutil
# ---------------------------------- client credentials retrieving for .env ----------------------------------

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
b64_auth_str = base64.urlsafe_b64encode((client_id +':'+ client_secret).encode()).decode() # Base64 encoded string for authorization header parameter

# ---------------------------------- Function for client authentication ----------------------------------
def auth():
    headers = {
        "Authorization": "Basic {}".format(b64_auth_str),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "client_credentials" # This is to define the way an application gets an access token
    }
    res = requests.post(
        'https://accounts.spotify.com/api/token',
        data=body,
        headers=headers
    )
    return res.json()['access_token'] # returns new access token after every 60mins which allows you to make requests to the Spotify Web API
token = auth()
header = {"Authorization" : "Bearer {}".format(token),"Content-Type": "application/json","Accept" : "application/json"} # This is a header required for any type of request to Spotify Web API

# ---------------------------------- Function to get ArtistID ----------------------------------
def getArtistID(artistName):
    res = requests.get(
        f"https://api.spotify.com/v1/search?q={artistName}&type=artist&limit=1",
        headers=header
    )
    item_dict = res.json()['artists']['items'][0] # getting item dictionary from the json response
    url = item_dict['external_urls']['spotify'] # parsing the url from the dictionary
    id = url.split('/')[-1] # now parsing the id from the url
    return id

# ---------------------------------- Function to get <date : Artist's albums> ----------------------------------
def getAlbums(artistName):
    albums = []
    temp = [] # to temporarily store the artist album, this will help in checking any redundancy
    res = requests.get(
                        f"https://api.spotify.com/v1/artists/{getArtistID(artistName)}/albums?limit=40&include_groups=album&market=IN",
                        headers=header
    )
    for item_dict in res.json()['items']: # for loop to traverse through all the item dictionaries in the json response
        if (int(item_dict['release_date'][0:4]) >= 1975) and (item_dict['name'] not in temp): # checking that the release date should be greater that 1975 and if the album is repeated or not
            temp.append(item_dict['name'])
            albums.append({
                item_dict['release_date'][0:4]:item_dict['name'],
                'albumID':item_dict['uri'].split(':')[-1] # this extracts albumID from URI key in item dictionary
                }) 

    return albums # This gives the response in the format of [{<release_date> : <Album name> , 'albumID' : <id>},{},{}....]

# ---------------------------------- Function to get Artist albums's songs ----------------------------------
def getAlbumsSongs(artistName):
    artistName = ' '.join(artistName.split('%20')) # this is just to modify artistName appearance
    albums_list = getAlbums(artistName)[::-1] # stores list in reverse order
    for album_dict in albums_list:
        res = requests.get(
            f"https://api.spotify.com/v1/albums/{album_dict['albumID']}/tracks?market=IN&limit=40",
            headers=header
        )
        print(list(album_dict.keys())[0]) # this prints the year
        print(f'    |----------{artistName}') # this prints artist's name
        print(f'        |----------{album_dict[list(album_dict.keys())[0]]}') # this gives album's name
        for song_dict in res.json()['items']:
            print(f"            |----------{song_dict['name'].split(' - ')[0]}") #this gives all the songs of the artist

# ---------------------------------- Main Function which calls other functions ----------------------------------
def main():
    ascii_logo = '''

░██████╗██████╗░░█████╗░████████╗██╗███████╗██╗░░░██╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚██╗░██╔╝
╚█████╗░██████╔╝██║░░██║░░░██║░░░██║█████╗░░░╚████╔╝░
░╚═══██╗██╔═══╝░██║░░██║░░░██║░░░██║██╔══╝░░░░╚██╔╝░░
██████╔╝██║░░░░░╚█████╔╝░░░██║░░░██║██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░

██████╗░██╗░██████╗░█████╗░░█████╗░░██████╗░██████╗░░█████╗░██████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░██║╚██╗░██╔╝
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██║░░██╗░██████╔╝███████║██████╔╝███████║░╚████╔╝░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██╔═══╝░██╔══██║░░╚██╔╝░░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░░░░░██║░░██║░░░██║░░░
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░
        '''
    for line in ascii_logo.split('\n'): # this is just to print the ascii_art in the center of the command line window
        print(line.center(shutil.get_terminal_size().columns))
    numberOfArtists = int(input('ENTER NUMBER OF ARTISTS ----------> '))
    for i in range(numberOfArtists):
        artistName = input('ENTER ARTIST\'s NAME ----------> ').split(' ')
        for i in tqdm(range (100),desc="Fetching…",ascii=False, ncols=75): # this displays the progress bar
            time.sleep(0.02)
        getAlbumsSongs('%20'.join(artistName))

if __name__ == '__main__':
    main()