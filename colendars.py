from bs4 import BeautifulSoup
import requests

class Colendar:
	"""
	Takes a subreddit and returns an object tool-kit for scraping posts.
	"""
	def __init__(self, subreddit):
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		self.base = f'https://old.reddit.com/r/{subreddit}/new/'
		self.next_page = ''
		self.hrefs = []
		self.posts = []

	# Opens a page with assigned user_agent
	def open_page(self, link):
		return requests.get(link, headers={'User-Agent': self.user_agent})

	# Filled hrefs with 25 post links and next-page link.
	def get_links(self, autostep=True):
		if autostep == False:
			self.next_page = ''
		if not self.next_page:
			r = self.open_page(self.base)
		elif self.next_page == 'no_next':
			return 'no_next'
		else:
			r = self.open_page(self.next_page)
		soup = BeautifulSoup(r.text, features="html.parser")
		posts = soup.find(id='siteTable').find_all("a", {"class": "title"})
		self.hrefs = [ 'https://old.reddit.com' + p['href'] for p in posts ]
		try:
			self.next_page = soup.find('span', {'class': 'next-button'}).a['href']
		except:
			self.next_page = 'no_next'

	def open_post(self, link):
		r = self.open_page(link)
		soup = BeautifulSoup(r.text, features="html.parser")
		title = soup.find('p', {'class': 'title'}).a.text
		try:
			paragraphs = soup.find('div', {'class': 'entry'}).find('div', {'class': 'md'}).find_all('p')
			post = '\n'.join([ p.text for p in paragraphs ])
		except:
			post = title
		return {'name': title, 'text': post}

	def get_posts(self, clear=False):
		counter = 1
		if clear:
			self.posts = []
		for ref in self.hrefs:
			print(f'{counter}/25', end="\r", flush=True)
			self.posts.append(self.open_post(ref))
			counter +=1
	
	def scrape(self, limit=0):
		counter = 1
		if limit == 0:
			while True:
				l = self.get_links()
				if l == "no_next":
					break
				print(f'Page {counter}')
				self.get_posts()
				counter+=1
		else:
			for x in range(limit):
				l = self.get_links()
				if l == "no_next":
					break
				print(f'Page {counter}')
				self.get_posts()
				counter+=1
		print("Done!")

	def count_posts(self):
		return len(self.posts)