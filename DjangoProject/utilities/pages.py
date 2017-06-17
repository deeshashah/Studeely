import acg
from collections import OrderedDict

class Pages(object):
	finalpages = OrderedDict()

	def __init__(self,topicUrl):
		c = {}
		c = acg.myClass(topicUrl)
		temp = {}
		temp = c.get_paras()
		self.finalpages['totalpara'] = len(temp)
		#self.finalpages['para'] = temp
		pages = OrderedDict()
		singlepage = OrderedDict()
		tempdict = OrderedDict()
		pagenum = 1
		# print temp
		# for key in temp:
		#   print key

		#paragraph must be biger than 800 letters minimum
		#also one page must be devided into points
		items = temp.iteritems()

		for key,value in items:
			tempdict = OrderedDict()
			singlepage = OrderedDict()
			if not key:
				key = "Lesson"
			# singlepage['pagepara'] = '1'
			length = len(value)
			print length
			
			# if length < 800 and key is not temp.keys()[-1]:
			# 	singlepage['pagepara'] = '2'
			# 	tempdict['heading'] = key
			# 	tempdict['para'] = value
			# 	tempdict['teaser'] = value[0:50]+"..."
			# 	singlepage['1'] = tempdict
			# 	try:
			# 		key,value = next(items)
			# 	except StopIteration:
			# 		break
			# 	print key
			# 	tempdict['heading'] = key
			# 	tempdict['para'] = value
			# 	tempdict['teaser'] = value[0:50]+"..."
			# 	singlepage['2'] = tempdict
			# else:
			print key
			tempdict['heading'] = key
			tempdict['para'] = value
			tempdict['teaser'] = value[0:50]+"..."
			singlepage['1'] = tempdict
			print "+++++++++++"
			# print singlepage
			pages[pagenum] = singlepage
			pagenum = pagenum+1

		self.finalpages['pagenum'] = pagenum
		self.finalpages['pages'] = pages

		# finalpages = 
		#           {
					#   'totalpara'  : 6,
					#   'para' = {
					#               'heading1' : 'para1',
					#               'heading2' : 'para2',
					#           }
					#   'pages' = {
					#                   '1' = {
			                                        # removed 'pagepara' : 2,
					#                                   '1' : {
					#                                           'heading' : 'heading',
					#                                           'teaser'  : 'teaserline',
					#                                           'para' : 'para1'
					#                                       }
					#                           }
					#               }
					#   }




	def get_pages(self):
		return self.finalpages