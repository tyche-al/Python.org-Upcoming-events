from datetime import datetime
from lxml.html import fromstring 
import requests


SOURCE = 'https://python.org'
EVENT = './/li'
WIDGET = './/div[@class="medium-widget event-widget last"]'
TIME = './time'
EVENT_LINK = './a'


class Event:
	def __init__(self, event):	
		self.event = event

	def parse(self):
		self.event_date = datetime.fromisoformat(self.event.xpath(TIME)[0].get('datetime'))
		self.event_name = (self.event.xpath(EVENT_LINK)[0].text_content())
		self.event_info = (self.event.xpath(EVENT_LINK)[0].get('href'))

	def __str__(self):
		return f'{self.event_date} {self.event_name} {SOURCE}{self.event_name}'

	def __repr__(self):
		return f'{self.event_date} {self.event_name} {SOURCE}{self.event_name}'


def get_events():
	page = requests.get(SOURCE)
	return fromstring(page.content).xpath(WIDGET)[0].xpath(EVENT)


if __name__ == '__main__':
	for item in get_events():
		event = Event(item)
		event.parse()
		print(event)
