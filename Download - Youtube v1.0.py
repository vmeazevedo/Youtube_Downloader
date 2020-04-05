import pytube
from pytube import YouTube

entrada = str(input('Cole aqui a URL que você quer realizar o download: '))
video_url = "'" +  entrada + "'"
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:\\Users\\pqcir\\Downloads\\video')
print('Seu video já está na pasta selecionada.')
