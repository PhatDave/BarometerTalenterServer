import json

from django.http import HttpResponse
from django.shortcuts import render

import cache
from TalentManager.TalentManager import TalentManager

talentManager = None


# Create your views here.
def index(request):
	return render(request, 'index.html')


def getTalents(request):
	global talentManager
	talentManager = TalentManager(request.POST['path'])
	# talentManager.move('engineer:weaponsengineer:1:militaryapplications->mechanic:machinist:1')
	# print(json.dumps(talentManager.serialize()))
	# return HttpResponse(json.dumps(talentManager.serialize()), content_type="application/json")
	return HttpResponse(cache.get())
