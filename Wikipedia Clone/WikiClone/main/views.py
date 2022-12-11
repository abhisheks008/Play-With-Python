from django.shortcuts import render,HttpResponse
import wikipedia
  
  
# Create your views here.
def home(request):
    if request.method == "POST":
        search = request.POST['search']
        search=search.replace(' ','')
        
        result = wikipedia.page(search).content #No of sentences that you want as output
        return render(request,"main/index.html",{"result":result})
    return render(request,"main/index.html")

# Create your views here.
