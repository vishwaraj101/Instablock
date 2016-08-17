print """ _ _|               |           |      |               |    
   |   __ \    __|  __|   _` |  __ \   |   _ \    __|  |  / 
   |   |   | \__ \  |    (   |  |   |  |  (   |  (       <  
 ___| _|  _| ____/ \__| \__,_| _.__/  _| \___/  \___| _|\_\ 
                                                            
[+]coded by Vishwaraj Bhattrai -@vishwaraj101                                                            """                                                           
 

id=input("user_id>>>> ")

from instagram.client import InstagramAPI


access_token = "1931492888.1677ed0.8f098298b22a4ad3ae82709dfcb712c0"
client_secret = "55f1524c1af34108ad2b03bf83d6bdc6"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id=id, count=10)
for media in recent_media:
    print"FETCHING RELATIVE DATA ...\n"
    
    
    print "FETCHED MEDIA ID"
    print   media.id
    
    print "\n"
   
    print "FETCHED MEDIA LINKS... \n"
    
    print media.images['standard_resolution'].url
    
    print "FETCHED MEDIA COMMENTS \n"
    
    print media.comments
    print "TAGS ASSOCIATED WITH IT \n"
    print media.tags
    
    print "NUMBER OF LIKES \n"
    print media.like_count
    
    
    print "FETCHING COMPLETED\n"




