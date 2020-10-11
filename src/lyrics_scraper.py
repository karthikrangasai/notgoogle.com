import re
import requests as r
from bs4 import BeautifulSoup

artists = ["Avicii"] #, "Eminem", "Kygo"]
base_url = "https://genius.com/artists/"


for artist in artists:
	url = base_url + artist
	req = r.get(url)

	webpage = BeautifulSoup(req.text, "html.parser")
	print(webpage.title)
	top_ten_songs = webpage.findAll("a", {"class": "mini_card"})

	for song in top_ten_songs:
		song_lyrics_url = song["href"]
		song_lyrics_req = r.get(song_lyrics_url)
		song_lyrics_webapge = BeautifulSoup(song_lyrics_req.text, "html.parser")
		print(song_lyrics_webapge.title)

		lyrics_spans = song_lyrics_webapge.find_all('span', {'class':'ReferentFragment__Highlight-oqvzi6-1'})
		# print(len(lyrics_spans))
		lyrics = ""
		for span in lyrics_spans:
			lyrics_lines = span.strings
			for line in lyrics_lines:
				lyrics = lyrics + "\n" + line
			# cleaned_lyrics = re.sub(r'\[[a-zA-Z0-9\s]*\]', ' ', div.text.strip())
			# lyrics += cleaned_lyrics
		print(lyrics)

