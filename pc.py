from colendars import Colendar
c=Colendar('copypasta')
c.scrape(1)
print('\n')
print(c.count_posts())
print(c.posts[0])