from .models import *

def adminEdit(request):
    try:
        return {
            "adminEdit": AdminPanelEdit.objects.all()[::-1][0]
        }
    except:
        return {"adminEdit": None}