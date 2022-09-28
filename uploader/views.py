# from multiprocessing import context
from django.shortcuts import render,HttpResponseRedirect
# from .forms  import ImageForm
from .form import ImageForm
from .models import Image
from django.urls import reverse


# Create your views here.

# def index(request):
#     if request.method == "POST":
#         img=Image.objects.all() 
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#          cd = form.cleaned_data
#          form.save()
#          shout = Image(photo = cd['photo'],caption=cd['caption'])
#          shout.save()
#         # obj = form.instance 
#          return HttpResponseRedirect(reverse("views.index"))
        
#         #  return render(request, "index.html", {'form':form,'img':img})
    
    
#     # context = {
#     #     'form': form,
#     #     'img' :img,
#     #     'obj': obj
#     # }
      
#     else:
#          form = ImageForm()
#         #  img=Image.objects.all()

#     return render(request, "index.html",{ 'form':form })










def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
        # obj = form.instance 
        img=Image.objects.all()
        return render(request, "index.html", {'form':form,'img':img})
    
    
    # context = {
    #     'form': form,
    #     'img' :img,
    #     'obj': obj
    # }
      
    else:
         form = ImageForm()
        #  img=Image.objects.all()

    return render(request, "index.html",{ 'form':form })

    # return render (request, "index.html", )
