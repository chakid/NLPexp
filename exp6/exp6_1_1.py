from urllib.request import urlopen

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
raw = urlopen(url).read()
type(raw)