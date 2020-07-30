from colendars import Colendar
from time import sleep
import requests

c=Colendar('copypasta')
api_url = 'https://www.publicpasta.com/api/pastas/'
print('Checking reddit every 3 minutes')

last = ''
current = ''
while True:
	c.get_links(False)
	current = c.open_post(c.hrefs[0])
	if current != last:
		requests.post(api_url, json=current, headers={'Authorization': 'Token abf63274994a88eb4425fab5d195c5200abe4c68'})
		print(current)
		last = current
	else:
		print('.', end="", flush=True)
	sleep(180)
