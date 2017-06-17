from bs4 import BeautifulSoup
import requests
from utilities import acg,tg,pages
from django.shortcuts import render_to_response,render
from collections import OrderedDict
from django.core.context_processors import csrf #protect against csrf
from .models import ListOfTopic
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def lot(request, anystring = None):
    all_topics = ListOfTopic.objects.all()
    if not anystring:
        print type(all_topics)
        print all_topics
        tempdict = {}
        args = {}
        index = 0
        for e in all_topics:
            temp = {}
            temp['topicName'] = str(e.topicName)
            temp['topicUrl'] = str(e.topicUrl)
            temp['topicSlug'] = str(e.topicSlug)
            tempdict[str(index)] = temp
            index = index + 1
        args['full_name'] = request.user.username
        args['lot'] = tempdict
        return render_to_response('listoftopics.html',args)
    # dictionary = {
    #                 '1' = {
    #                         'topicName' : 'ray optics',
    #                         'topicUrl'  : 'url',
    #                         'topicSlug' : 'slug'
    #                     }
    #                 '2' = {
    #                         ...
    #                 }
    #                 ...
    #             }
    else:
        #anystring is slug
        #get link and send link to acg
        temp = {}
        temp = ListOfTopic.objects.get(topicSlug = anystring)
        args = OrderedDict()
        args['topicUrl'] = temp.topicUrl
        args['topicName'] = temp.topicName
        p = pages.Pages(temp.topicUrl)
        args['finalpages'] = p.get_pages()
        args['full_name'] = request.user.username
        # return render_to_response('content/contentPage.html',args)
        return render_to_response('content/contentPage.html',args)

    # args = {

    #     'paranum' : 5,
    #     'deesha'  : 'riken',
    #     'para'    : {
    #                     'heading1' : 'para1',
    #                     'heading2' : 'para2'
    #                 }

    # }

@login_required  
def test(request,anystring=None):
    if request.method == 'POST':
        if anystring:
            resultdict = OrderedDict()
            shared_obj = request.session.get('myobj')
            givenans = OrderedDict()
            for key,value in request.POST.items():
                key = key[4:]
                givenans[key] = value
                
            quesdict = OrderedDict()
            quesdict =  request.session['test']
            for key,value in quesdict.items():
                tempdict = OrderedDict()
                tempdict['ques'] = value['ques']
                tempdict['option1'] = value['options']['option1']
                tempdict['option2'] = value['options']['option2']
                tempdict['option3'] = value['options']['option3']
                tempdict['option4'] = value['options']['option4']
                tempdict['correctans'] = value['ans']
                temp = "option"+str(givenans[key])
                tempdict['givenans'] = value['options'][temp]
                #checking results
                result = 'wrong'
                result_id = '0'
                if key in givenans.keys():
                    if str(value['correctans_id']) == str(givenans[key]):
                        result = 'correct'
                        result_id = '1'

                tempdict['result_id'] = result_id
                tempdict['result'] = result
                print tempdict
                print "___________---"
                resultdict[key] = tempdict
            
            temp = ListOfTopic.objects.get(topicSlug = anystring)
            args = {}
            args['full_name'] = request.user.username
            args['resultdict']  = resultdict
            args['topicName'] = temp.topicName
            del request.session['myobj']
            del request.session['test']
            request.session.modified = True
            return render_to_response('testresults.html',args)
            # dictionary = {
            #                 '1' :{
            #                         'ques' : '<<questiontext>>',
            #                         'option1' : '<<option1>>',
            #                         'option2' : '<<option1>>',
            #                         'option3' : '<<option1>>',
            #                         'option4' : '<<option1>>',
            #                         'givenans' : '<<givenans>>',
            #                         'correctans' : '<<correctans',
            #                         'result_id' :'1(correct)/2(wrong)',
            #                         'result' : 'correct/wrong',
            #                     }
            #                 '2' :{
            #                       ...
            #                       }
            #                 .
            #                 .
            #                 .
            #             }
        else:
            return HttpResponse('<html>Wrong Url</html>')

    else:
        if anystring:
            args = OrderedDict()
            shared_obj = {}
            args['full_name'] = request.user.username
            request.session.get('myobj',{})
            temp = ListOfTopic.objects.get(topicSlug = anystring)
            t = tg.TestModule(temp.topicUrl)
            args.update(csrf(request))
            args['topicName'] = temp.topicName
            args['topicSlug'] = temp.topicSlug
            args['testdict'] = t.get_test()
            request.session['test'] = args['testdict']
            for key,value in args['testdict'].items():
                shared_obj[str(key)] = value['correctans_id']

            args['para'] = t.get_imp_words()
            # myobj = {
            #     'correctans' :{           
            #                 '1' : '0',
            #                 '2' : '1',
            #                 .
            #                 .
            #                 '9' : '1'}
            # }
            request.session['myobj'] = shared_obj
            return render_to_response('testpage.html',args)
        else:
            return HttpResponseRedirect('/magic/topics')
