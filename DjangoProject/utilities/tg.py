#import statements
from bs4 import BeautifulSoup
import acg
import re
from collections import OrderedDict
import random
from random import shuffle

class TestModule(object):
	paracode = None
	impwords = None
	questionBank = OrderedDict()
	generatedTest = OrderedDict()
	quesnum = 3;
	def __init__(self,anystring):
		self.questionBank.clear()
		self.generatedTest.clear()
		if self.paracode is None:
			self.paracode = []
		else:
			self.paracode[:] = []

		if self.impwords is None:
			self.impwords = []
		else:
			self.impwords[:] = []

		c = acg.myClass(anystring)
		self.paracode.extend(c.get_paracode())
		index = 0
		#m getting b and href to make a list of all imp words
		#there is scope for optimization, can be done in the p tags itself
		for ith in self.paracode:
		 	hrefs = ith.findAll('a',attrs={'href':re.compile('/wiki/.*')})
		 	bolds = ith.findAll('b')

		 	for i in hrefs:
		 		self.impwords.append(i.get_text())
		 	for i in bolds:
		 		self.impwords.append(i.get_text())
		 	
		 	wrongfullstops = ith.findAll('a',attrs={'href':re.compile('php(.*)|svg.*|org.*')})
		 	wrongfullstops2 = ith.findAll('img',attrs={'src':re.compile('png.*|org.*')})
		 	for i in wrongfullstops:
		 		i.decompose()
		 	for i in wrongfullstops2:
		 		i.decompose()

		 	headings = ith.findAll('span',attrs={'class':'mw-headline'})
		 	for i in headings:
		 		i.decompose()

		 	#print self.impwords
		 	#removing duplicate entries from the list
		 	self.impwords = list(set(self.impwords))
		 	del(self.impwords[0])

		 	#iterating through all sentences
		 	tempques = str(ith).split('.')
		 	for i in tempques:
		 		soup = BeautifulSoup(i,'html.parser')
		 		ans = soup.find('b')
		 		if ans is None:
		 			ans = soup.find('a',attrs={'href':re.compile('/wiki/.*')})
		 		singleq = soup.get_text().encode('ascii','ignore')
		 		if ans is not None:
		 			correctans = ans.get_text().encode('ascii','ignore')
		 			#neatufying the question text
		 			for i in range(0,100):
						temp = "["+str(i)+"]"
						singleq = singleq.replace(temp," ")
					singleq = singleq.replace("[edit]"," ")
					singleq = singleq.replace("[","")
					singleq = singleq.replace("]","")
					singleq = singleq.replace("\n","")
					#replacing ans witha blank
					singleq = singleq.replace(correctans,"________")
					# print singleq
					# print "\n"
					# print correctans
					# print "\n-----\n"
					temp = {}
					temp['ques'] = singleq
					temp['ans'] = correctans
					self.questionBank[index] = temp
					index = index+1


	def tp(self):
		return self.paracode

	def get_three_words(self):
		words = random.sample(self.impwords,3)
		return words

	def get_imp_words(self):
		print len(self.impwords)
		print self.impwords
		return self.impwords

	def get_question_bank(self):
		return self.questionBank

	def get_test(self):
		index = 1
		keys = random.sample(self.questionBank,self.quesnum)
		# self.generatedTest['quesnum'] = self.quesnum
		for k in keys:
			temp = OrderedDict()
			temp['id'] = k
			temp['ques'] = self.questionBank[k]['ques']
			ans = self.questionBank[k]['ans']
			temp['ans'] = ans
			#creating four ans choices
			three = self.get_three_words()
			while ans in three:
				three = self.get_three_words()
			three.append(ans)
			shuffle(three)
			temp['correctans_id'] = three.index(ans)+1
			print temp['correctans_id']
			opt1 = three[0]
			opt2 = three[1]
			opt3 = three[2]
			opt4 = three[3]
			temp['options'] = {
				'option1' : opt1,
				'option2' : opt2,
				'option3' : opt3,
				'option4' : opt4
			}
			self.generatedTest[index] = temp
			index = index+1

		return self.generatedTest


		# dictionary = {
		# 			'1' :{
		# 					'id' : 'questionid',
		# 					'ques' : 'questiontext',
		# 					'ans' : 'answerCorrect',
		#					'correctans_id' : 3,
		# 					'options' : {
		# 							'option1' : 'opt1',
		# 							'option2' : 'opt2',
		# 							'option3' : 'opt3',
		# 							'option4' : 'opt4',
		# 					}
		# 			}
		# }