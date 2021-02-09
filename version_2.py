import requests
import json
import urllib.request
import main

# p = main.get_id_alboms(main.data)
access_token = 'access_token=c2b7d8acc2b7d8acc2b7d8acc3c2c3737acc2b7c2b7d8ac9d1b1a7e35cec994a9009a8d'
versions = 'v=5.52'
owner_id = 'owner_id=409122506'
method = 'photos.getAlbums'
data = json.loads(requests.get('''https://api.vk.com/method/{method}?count=1000&{token}&{versions}&{owner_id}&{album_id}&
		'''.format(album_id='album_id=277205857',method = method,token = access_token,versions=versions,owner_id=owner_id)).text)

def get_id_alboms(data):
	id_alboms = []
	for i in data['response']['items']:
		id_alboms.append(i['id'])
	
	return id_alboms

def get_all_photos(id_alboms):
	all_links = []
	for i in id_alboms:
		data = json.loads(requests.get('''https://api.vk.com/method/{method}?count=1000&{token}&{versions}&{owner_id}&album_id={i}&
		'''.format(i=i,method = 'photos.get',token = access_token,versions=versions,owner_id=owner_id)).text)
		for i in data['response']['items']:
			try:
				
				 if 'photo_1280' in i.keys():
				 	all_links.append(i['photo_1280'])
				 elif 'photo_1280' in i.keys():
				 	all_links.append(i['photo_1280'])
				 elif 'photo_807' in i.keys():
				 	all_links.append(i['photo_807'])
				 else:
				 	all_links.append(i['photo_604'])
			except:
				print(i)
	return all_links




def download_photos(all_links):
	for i in range(0,len(all_links)):
		img = urllib.request.urlopen(all_links[i]).read()
		out = open("hruashevak/img{i}.jpg".format(i=i), "wb")
		out.write(img)
		out.close
def main():		
	download_photos(get_all_photos(get_id_alboms(data)))
if __name__ == '__main__':
	main()