from datetime import datetime
from lxml.html import fromstring 
import requests

SOURCE = 'https://python.org'
EVENT_ITEM = './/li'
WIDGET = './/div[@class="medium-widget event-widget last"]'
TIME = './time'
EVENT_LINK = './a'


class Event:
	def __init__(self, source):
		self.source = source

	def parse_list_item(self, event):
		self.event = event
		self.event_date = datetime.fromisoformat(self.event.xpath(self.time)[0].get('datetime'))
		self.event_info = (event.xpath(self.event_link)[0].get('href'))
		self.event_name = (event.xpath(self.event_link)[0].text_content())
		return (self.event_date, self.event_name, self.event_info)

	def get_events(self, widget, event_item, event_link, time):
		page = requests.get(self.source)

		self.widget = widget
		self.event_item = event_item
		self.event_link = event_link
		self.time = time

		self.tree = fromstring(page.content).xpath(self.widget)[0]
		self.events =[self.parse_list_item(event) for event in self.tree.xpath(self.event_item)]

	def _print(self):
		for event in self.events:
			print(f'{event[0]} {event[1]} {self.source}{event[2]}')


if __name__ == '__main__':
	events = Event(SOURCE)
	events.get_events(WIDGET, EVENT_ITEM, EVENT_LINK, TIME)
	events._print()