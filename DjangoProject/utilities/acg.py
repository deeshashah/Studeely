#this is extracting from remomte links

#import statements
from bs4 import BeautifulSoup
import requests
import sys
from collections import OrderedDict


class myClass(object):
	actuallinks = None
	ithparacode = None
	ithpara = OrderedDict()
	finalparas = OrderedDict()
	topicUrl = ""
	def __init__(self,topicUrl):
		if self.actuallinks is None:
			self.actuallinks = []
		else:
			self.actuallinks[:] = []

		if self.ithparacode is None:
			self.ithparacode = []
		else:
			self.ithparacode[:] = []

		self.ithpara.clear()
		self.finalparas.clear()

		#getting a source of remote page
		r = ""
		r = requests.get(topicUrl)
		# r = requests.get('https://en.wikipedia.org/wiki/Ray_%28optics%29')
		# r = requests.get('https://en.wikipedia.org/wiki/Electric_current')
		# r = requests.get('https://en.wikipedia.org/wiki/Physics')
		# r = requests.get('https://en.wikipedia.org/wiki/Magnetism')
		# r = requests.get('https://en.wikipedia.org/wiki/Electromagnetic_radiation')
		page = r.text
		soupfirst = BeautifulSoup(page,'html.parser')	

		#first set of modifications removing table of contents from raw
		if soupfirst.find("div", {'class':'toc'}):
			soupfirst.find("div", {'class':'toc'}).decompose()
		textNoToc = str(soupfirst)
		soupsecond = BeautifulSoup(textNoToc,'html.parser')

		#latest soup is soupsecond
		#getting all useful hyperlinks fromhatnote class and removing them
		contentlinks = soupsecond.findAll('div', attrs={'class':'hatnote'})
		for division in contentlinks:
			temp = division.findAll('a')
			for links in temp:
				self.actuallinks.append("https://en.wikipedia.org"+links['href'])
			division.decompose()

		soupthird = BeautifulSoup(str(soupsecond),'html.parser')


		## Making a new soup a bit more concise
		#this is the main text starting
		maintextsoup = soupthird.find('div',attrs={'class':'mw-content-ltr'})
		#defining an end and thus making a new soup
		temp2 = str(maintextsoup.find('span',attrs={'id':'See_also'}))
		temp = str(maintextsoup)
		end = temp.find(temp2)
		temptext = temp[0:end]
		soupfour = BeautifulSoup(temptext,'html.parser')

		##removing images do it later
		# images = soupfour.findAll('div',attrs={'class':'thumb tright'})
		# for i in images:
		# 	#i.find_previous('span',attrs={'class':'mw-headline'}).decompose()
		# 	i.decompose()
		##making small paras
		#soupfour is the latest soup
		# f = open('out.html', 'w')
		# print >> f, 'Filename:', soupfour  # or f.write('...\n')
		# f.close()
		# sys.exit()
		parastarts = soupfour.findAll('span',attrs={'class':'mw-headline'})
		for index,starts in enumerate(parastarts):
			if index==0:
				start = 0
				end = temptext.find(str(parastarts[index]))
				paratext = temptext[start:end]
				ithparasoup = BeautifulSoup(paratext,'html.parser')
				self.ithparacode.append(ithparasoup)
				self.get_neat_paras(ithparasoup)
				continue
			start = temptext.find(str(parastarts[index-1]))
			end = temptext.find(str(starts))
			paratext = temptext[start:end]
			ithparasoup = BeautifulSoup(paratext,'html.parser')
			self.ithparacode.append(ithparasoup)
			self.get_neat_paras(ithparasoup)

		start = temptext.find(str(starts))
		paratext = temptext[start:]
		ithparasoup = BeautifulSoup(paratext,'html.parser')
		self.ithparacode.append(ithparasoup)
		self.get_neat_paras(ithparasoup)
		##paras done

	def get_links(self):
		return self.actuallinks

	def get_paras(self):
		return self.ithpara

	def get_paracode(self):
		return self.ithparacode

	def get_neat_paras(self,ithparasoup):
		headingcode = ithparasoup.find('span',attrs={'class':'mw-headline'})
		if headingcode:
			heading = headingcode.get_text()
			headingcode.decompose()
		else:
			heading = ""
		self.ithpara[heading] = ithparasoup.get_text()
		for i in range(0,100):
			temp = "["+str(i)+"]"
			heading = heading.replace(temp," ")
			self.ithpara[heading] = self.ithpara[heading].replace(temp," ")
		heading = heading.replace("[edit]"," ")
		self.ithpara[heading] = self.ithpara[heading].replace("[edit]"," ")

