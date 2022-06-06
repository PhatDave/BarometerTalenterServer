from django.shortcuts import render

from TalentManager.TalentManager import TalentManager

talentManager = None


# Create your views here.
def index(request):
	return render(request, 'index.html')


def submitFileName(request):
	global talentManager
	talentManager = TalentManager(request.POST['path'])
	print(str(talentManager))
	pass
