# **SPOTIFY DISCOGRAPHY** 

Seriously, all thanks to [Spotify Web API docs](https://developer.spotify.com/documentation/web-api/)

## Choose OAuth-Flow
---
![](.\img/1.jpg)

> In my case I chose Client Credential flow
> 
## Client Credential Flow
---
![](.\img/2.jpg)

Clearly from the diagram we can see we that for authorization process one requires valid client credentials: CLIENT_ID and CLIENT_SECRET

We can get Client Credentials from [Dashboard](https://developer.spotify.com/dashboard/applications) :

- First create an App and then click on it
  
  ![](.\img/3.jpg)

- Then you can just see your credentails

  ![](.\img/4.jpg)


## Setup
---
- Update .env file by adding your own credentials
  ![](.\img/5.jpg)

- Install all the dependencies 
```
pip install -r requirements.txt
```
## Additional Resources
--- 
If you want to just want to explore all the things you can do using Spotify Web API, checkout [Endpoints for API](https://developer.spotify.com/documentation/web-api/reference/#/)