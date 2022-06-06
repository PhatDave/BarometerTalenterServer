import json

from django.http import HttpResponse
from django.shortcuts import render

from TalentManager.TalentManager import TalentManager

talentManager = None


# Create your views here.
def index(request):
	return render(request, 'index.html')


def getTalents(request):
	global talentManager
	talentManager = TalentManager(request.POST['path'])
	# talentManager.move('engineer:weaponsengineer:1:militaryapplications->mechanic:machinist:1')
	return HttpResponse(json.dumps(talentManager.serialize()), content_type="application/json")
