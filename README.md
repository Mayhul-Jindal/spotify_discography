# **SPOTIFY DISCOGRAPHY** 

Seriously, all thanks to [Spotify Web API docs](https://developer.spotify.com/documentation/web-api/)
## DEMO

https://user-images.githubusercontent.com/95216160/152760685-53dfed53-c4e8-4693-b0b6-2749322418c3.mp4

## Choose OAuth-Flow

![1](https://user-images.githubusercontent.com/95216160/152758188-3fe77e47-b1e0-444d-9bba-256d73d04fb4.jpg)

> In my case I chose Client Credential flow

## Client Credential Flow

![2](https://user-images.githubusercontent.com/95216160/152758290-2941d423-0858-40b2-a8ae-326b858d51b1.jpg)

Clearly from the diagram we can see we that for authorization process one requires valid client credentials: CLIENT_ID and CLIENT_SECRET

We can get Client Credentials from [Dashboard](https://developer.spotify.com/dashboard/applications) :

- First create an App and then click on it

  ![3](https://user-images.githubusercontent.com/95216160/152758339-4d2674b1-30cf-4047-9617-1c374c8e2059.jpg)

- Then you can just see your credentails

  ![4](https://user-images.githubusercontent.com/95216160/152758410-97e8c399-305b-40b9-ad84-891ace64ffb6.jpg)

## Setup

- Update .env file by adding your own credentials

  ![5](https://user-images.githubusercontent.com/95216160/152758503-0a86e6da-2aa7-4df6-b4da-41cffceab0e5.jpg)

- Install all the dependencies 
```
pip install -r requirements.txt
```
## Additional Resources

If you want to just want to explore all the things you can do using Spotify Web API, checkout [Endpoints for API](https://developer.spotify.com/documentation/web-api/reference/#/)
