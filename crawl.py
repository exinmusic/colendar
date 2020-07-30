from colendars import Colendar
from termcolor import cprint
import requests
from time import sleep

c=Colendar('copypasta')
api_url = 'http://www.publicpasta.com/api/pastas/'
headers = {'Authorization': 'Token 9737808d946a0118b3b03d726ee0b03fced11b47'}

def crawler():
	counter = 1
	while True:
		try:
			cprint(f'Page {counter} of content.\n', 'white')
			result = c.get_links()
			if result == 'no_next':
				break
			c.get_posts(True)
			for post in c.posts:
				r = requests.post(api_url, json=post, headers=headers)
				if r.status_code == 400:
					cprint(f"FAILED TO ADD {post['name']}, LIKELY DUE TO SIZE.", 'red')
				elif r.status_code == 201:
					cprint(f"ADDED {post['name']} TO PublicPasta!", 'green')
			counter+=1
		except:
			break
	print(f'DONE! Scraped {counter} pages!')

if __name__ == "__main__":
	crawler()