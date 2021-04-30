import requests
import json
import urllib.request

access_token = 'access_token='	
versions = 'v=5.52'
owner_id = 'owner_id=155216956'
method = 'friends.getOnline'
data = json.loads(requests.get('''https://api.vk.com/method/{method}?{token}&{versions}&{owner_id}
							   '''.format(method = method,token = access_token,versions=versions,owner_id=owner_id)).text)
print(data)

#Получаем id всех альбомов
def get_id_alboms(data):
	id_alboms = []
	for i in data['response']['items']:

		id_alboms.append('album_id='+str(i['id']))
	
	return id_alboms	


def get_photos(id_alboms):
	method = 'photos.get'
	all_links = []
	num = 0
	for p in range(0,len(id_alboms)):
		
		data = json.loads(requests.get('''https://api.vk.com/method/{method}?count=1000&{token}&{versions}&{owner_id}&{album_id}&
			'''.format(album_id=id_alboms[p],method = method,token = access_token,versions=versions,owner_id=owner_id)).text)
		
		for i in range(0,len(data['response']['items'])):
			if 'photo_1280' in data['response']['items'][i]:
				all_links.append(data['response']['items'][i]['photo_1280'])
			elif 'photo_807' in data['response']['items'][i]:
				all_links.append(data['response']['items'][i]['photo_807'])
			elif 'photo_604' in data['response']['items'][i]:
				all_links.append(data['response']['items'][i]['photo_604'])
	
	
	data = json.loads(requests.get('''https://api.vk.com/method/{method}?count=1000&{token}&{versions}&{owner_id}&{album_id}&
		'''.format(album_id='album_id=profile',method = method,token = access_token,versions=versions,owner_id=owner_id)).text)
	respoce = data['response']['items']
	
	for i in range(0,len(data['response']['items'])):
		if 'photo_1280' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_1280'])
		elif 'photo_807' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_807'])
		elif 'photo_604' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_604'])	


	data = json.loads(requests.get('''https://api.vk.com/method/{method}?count=1000&{token}&{versions}&{owner_id}&{album_id}&
		'''.format(album_id='album_id=wall',method = method,token = access_token,versions=versions,owner_id=owner_id)).text)
	respoce = data['response']['items']
	
	for i in range(0,len(data['response']['items'])):
		if 'photo_1280' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_1280'])
		elif 'photo_807' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_807'])
		elif 'photo_604' in data['response']['items'][i]:
			all_links.append(data['response']['items'][i]['photo_604'])	
	
	return all_links

def download_photos(all_links):
	for i in range(0,len(all_links)):
		img = urllib.request.urlopen(all_links[i]).read()
		out = open("hruashevak/img{i}.jpg".format(i=i), "wb")
		out.write(img)
		out.close

def main():
	download_photos(get_photos(get_id_alboms(data)))


