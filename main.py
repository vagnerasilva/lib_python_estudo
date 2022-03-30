from twitter import Twitter
import time

consumer_key    = 'XX'
consumer_secret = 'XX'

token_key       = 'XX'
token_secret    = 'XX'


twitter = Twitter(consumer_key, consumer_secret, token_key , token_secret)

#resp= twitter.tweet('Vamos testar nossa lib')


pesquisa =  twitter.search('solyd', 'pt' )
