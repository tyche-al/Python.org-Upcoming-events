from datetime import datetime
from lxml.html import fromstring 
import requests

SOURCE = 'https://python.org'
EVENT_ITEM = './/li'
WIDGET = './/div[@class="medium-widget event-widget last"]'
TIME = './time'
EVENT_LINK = './a'


class Events:
	def __init__(self, events=[]):
		self.events = events

	def parse_list_item(self, event):
		event_date = datetime.fromisoformat(event.xpath(TIME)[0].get('datetime'))
		event_name = (event.xpath(EVENT_LINK)[0].text_content())
		event_info = (event.xpath(EVENT_LINK)[0].get('href'))

		return f'{event_date} {event_name} {SOURCE}{event_info}'

	def get_events(self):
		page = requests.get(SOURCE)
		tree = fromstring(page.content).xpath(WIDGET)[0]
		self.events =[self.parse_list_item(event) for event in tree.xpath(EVENT_ITEM)]
			

if __name__ == '__main__':
	e = Events()
	e.get_events()
	for event in e.events:
		print(event)
