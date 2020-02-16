from colendars import Colendar
from time import sleep
import requests

c=Colendar('copypasta')
api_url = 'http://127.0.0.1:8000/pastas/'


last = ''
current = ''
while True:
	c.get_links(False)
	current = c.open_post(c.hrefs[0])
	if current != last:
		requests.post(api_url, json=current, headers={'Authorization': 'Token b4f2230b42d4dc706669abffbbd3b6a6dd13f765'})
		print(current)
		last = current
	else:
		print('.', end="", flush=True)
	sleep(60)
