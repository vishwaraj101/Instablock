# Instablock
Simple tool to check weak /api/enpoints of instagram affected by block feature
This code was the part of my proof of concept reported to instagram security team by which any blocked user can call api with his access_token to see victim comments,likes,photos, etc now it has been patched by team but still can be useful in basic recon.


### Version
1.0

###Parts 
It consist of 2 scripts
* A php script to fetch userid 
* A python script to fetch the likes,photos,comments

###Before using 
####Install instagram api 
```sh
$ pip install python-instagram
```
###2.)You will need the access_token of your own account + client_secret 
* to generatefollow https://www.instagram.com/developer/authentication/

* access_token = "1931492888.1677ed0.8f098298b22a4ad3ae82709dfcb712c0"
* client_secret = "55f1524c1af34108ad2b03bf83d6bdc6"

### Usage

```sh
$ python starthack.py
$Enter user id >>>509823
fetching...

```

### Imports

* InstagramAPI


###Demo: https://www.youtube.com/watch?v=0ZUeQ_fG_BA 


###Blog Post: https://vishwarajbhattrai.wordpress.com/2016/07/13/hacking-instagram-apis/


### Development

Want to contribute? Great!

Feel free to use or edit the code



License
----

MIT


**Free Software, Hell Yeah!**



### Note :
####This tool is just built for security test or consistency purpose don't misuse it author  will not be responsible for your actions .
  
