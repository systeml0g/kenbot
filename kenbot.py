import tweepy
import os
import sys




class Kenbot:
	def __init__(self):
		self.conkey=''
		self.consec=''
		self.token=''
		self.toksec=''

		with open('keys.asc') as f:
			self.conkey=f.readline().split('=')[1]
			self.consec=f.readline().split('=')[1]
			self.token=f.readline().split('=')[1]
			self.toksec=f.readline().split('=')[1]
		
	#Creacion de la base de datos si no existe

	#Autenticacion con archivo de claves
	def auth(self):
		auth = tweepy.OAuthHandler(self.conkey, self.consec)
		auth.set_access_token(self.token, self.toksec)
		api = tweepy.API(auth)
		return api

	#Persistencia de un tuit a base de datos

	#Temporal: Listar tuits de autor
	def userTuits(self, api):
		tuits=api.API.user_timeline(screen_name='barbijaputa',count = 100, include_rts=True)

		for tuit in tuits:
			print tuit._json


if __name__=="__main__":
	a=Kenbot()
	api=a.auth()
	#a.userTuits(api)
	
