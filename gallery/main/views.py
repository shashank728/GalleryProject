from django.shortcuts import render,redirect

from .models import Add_img

# Create your views here.

def home(request):
    return render(request,"home.html")


# ============== photos gallery ==================
def gallery(request):

    img = Add_img.objects.filter(category="nature")
    
    parameter = {
        "img" : img,

    }
    
    return render(request,"gallery.html",parameter)


# ============= add img =======================
def add_img(request):
    if request.method == "POST":
        user_img = request.FILES["img"] 
        category = request.POST.get("category")
        

        
        new_user = Add_img(
            img = user_img,
            category = category
            
        )
        new_user.save()
        
        return redirect("gallery")
    
    return render(request,"add_img.html")


# ================= Delete =========================

def delete(request,imgs_id):
    image = Add_img.objects.get(id = imgs_id)
    
    image.delete()
    return redirect("gallery")
    
    
# ================= category ======================

def category(request):

    category = Add_img.objects.all()

    parameter = {
        "category": category
    }

    return render(request,"category.html", parameter)





