from django.shortcuts import render
from online.models import Online
from online.forms import onlineform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     m = Online.objects.all()
#     return render (request,'movielist.html',{'h':m})
class MovieList(ListView): #ListView Diplays all objects/records retriving from a model
    model=Online
    template_name="movielist.html"
    context_object_name="h"
# def insertion(request):
#     m=Online.objects.all()
#     if (request.method=="POST"):
#         i=request.FILES['i']
#         t=request.POST['t']
#         s=request.POST['s']
#         y=request.POST['y']
#         m=Online.objects.create(image=i,title=t,subtitle=s,year=y)
#         m.save()
#         return home(request)
#     return render(request,'insertion.html',{'h':m})
class MovieAdd(CreateView):#CreateView displays a  form for adding new objects and handles form submission
    model=Online
    template_name='insertion.html'
    fields='__all__'
    success_url=reverse_lazy('home')

# def more(request,p):
#     d=Online.objects.get(title=p)
#     return render(request,'more.html',{'h':d})
class MovieDetail(DetailView):#DetailView displays a particular object retriving from a model.
    model=Online
    template_name='more.html'
    context_object_name="h"

# def update(request,p):
#     d = Online.objects.get(title=p)
#     if (request.method=="POST"):
#         form = onlineform(request.POST,request.FILES,instance=d)
#         if form.is_valid():
#             form.save()
#             return home(request)
#         form=onlineform(instance=d)
#        return render(request, 'update.html', {'form':form})

class MovieUpdate(UpdateView):  # CreateView displays a  form for adding new objects and handles form submission
            model = Online
            template_name ='update.html'
            fields ='__all__'
            success_url =reverse_lazy('home')


# def delete(request,p):
#     d=Online.objects.get(title=p)
#     d.delete()
#     return home(request)

class MovieDelete(DeleteView):
    model=Online
    success_url=reverse_lazy('home')
    template_name="delete.html"