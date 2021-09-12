from django.shortcuts import redirect, render
import random
from urlapp.models import UrlModel
# Create your views here.



def createUrl(req):
    if req.method == 'POST':
        full_url = req.POST.get('link')
        short_url = ""

        alpha = [
            "a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1"
            "2","3","4","5","6","7","8","9","0"
            ]

        url = UrlModel.objects.all()

        for i in url:
            if i.full_url == full_url:
                short_url = i.short_url
                break
        else:
            for i in range(1,7):
                letters = random.randint(1, len(alpha) - 1)
                let = alpha[letters]
                short_url += let 

            url = UrlModel(full_url = full_url , short_url =short_url)
            url.save() 

        new_url = "https://django-url-shortner-app.herokuapp.com/" + short_url
        return render(req, 'urlapp/index.html', {"new_url": new_url})             



    return render(req , 'urlapp/index.html')    


def routeLinkUrl(req, id):
    url = UrlModel.objects.filter(short_url=id)
    full_url = ""
    for i in url:
        full_url = i.full_url

    return redirect(full_url)


# def routeLinkUrl(req,id):
#     try:
#         obj = UrlModel.objects.get(short_url = id)
#         return redirect(obj.full_url)
#     except:
#         return redirect(createUrl)
