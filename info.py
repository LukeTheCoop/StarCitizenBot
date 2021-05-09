#info.py
from bs4 import BeautifulSoup
import asyncio
from selenium import webdriver
import requests
from time import sleep
import re

def update_news(dict): #update the bot
	link = dict['url']

	if 'robertsspaceindustries' in link:
		Update = RsiUpdate(dict)
		Update.get_info()
	elif 'reddit' in link:
		pass

	return f'**{Update.title}**\n{Update.url}\n\n{Update.description}'


class RsiUpdate():
	def __init__(self, dict):
		self.url, self.title = dict['url'], dict['title']

		if 'reply' in dict['description'].lower():
			news_type = 'reply'
		elif 'cig' in dict['description'].lower():
			news_type = 'post'
		elif 'comm' in self.url:
			news_type = 'comm-link'

		self.news_type = news_type


		request_link = requests.get(self.url)
		self.soup = BeautifulSoup(request_link.text, 'lxml')

	def get_info(self):
		news_type = self.news_type

		driver = webdriver.Chrome()
		url = self.url
		driver.get(url)
		sleep(3)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		driver.quit()

		if news_type == 'reply':
			dev_info = ''
			reply_thread = soup.find_all('div', class_='forum-thread-item')
			member_info = reply_thread[1].find('div', class_='forum-thread-member-info')
			for reply in reply_thread:
				reply_users = reply.find('span', class_='nickname').text
				if 'cig' in reply_users.lower():
					dev_info = reply
					break
			
			description = ''
			print(dev_info.find('span', class_='nickname'))

		elif news_type == 'post':
			
			content_soup = soup.find('div', class_='content-block text')
			description = content_soup.find('div').text
			description = re.sub(r"([\.?!,])([^\s])", "\\1 \\2", description)
			if description[:200].endswith('.') or description[:200].endswith('!') or description[:200].endswith('?'):
				description = description
			else:
				for i in range(100):
					if description[:200+i].endswith('.') or description[:200+i].endswith('!') or description[:200+i].endswith('?'):
						description = description[:200+i]
						break
					else:
						pass

		elif news_type == 'comm-link':
			description = ''
		else:
			description = ''

		self.description = description

temp_dict = {
    'footer': {'text': 'https://www.trackersc.com'}, 
    'thumbnail': 
        {'width': 1200, 'url': 'https://robertsspaceindustries.com/rsi/static/tavern/opengraph.png', 'proxy_url': 'https://images-ext-2.discordapp.net/external/K0M9yjAMK_bAemNNhEB2vg_p0m27AbzMdUGS6b7bh4M/https/robertsspaceindustries.com/rsi/static/tavern/opengraph.png', 'height': 630}, 
    'author': 
        {'url': 'https://www.trackersc.com', 'proxy_icon_url': 'https://images-ext-2.discordapp.net/external/nBfowGy9HcFf3mENC2IbAR16UN3WAqRCPGxAjehbtbw/https/www.trackersc.com/images/website-logo-250.png', 'name': 'Dev Tracker - TrackerSC.com', 'icon_url': 'https://www.trackersc.com/images/website-logo-250.png'}, 
    'type': 'rich', 
    'description': 'YogiKlatt_CIG [Reply]', 
    'url': 'https://robertsspaceindustries.com/spectrum/community/SC/forum/4/thread/foip-headtracking/4008396', 
    'title': 'Foip headtracking'}

if __name__ == '__main__':
	Update = RsiUpdate(temp_dict)
	Update.get_info()
	
