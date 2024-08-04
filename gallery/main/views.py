from django.shortcuts import render,redirect

from .models import Add_img




def home(request):
    return render(request,"home.html")


# ============== photos gallery ==================



def gallery(request):

    img = Add_img.objects.all()
    
    parameter = {
        "img" : img
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


def delete(request,image_id):
    image = Add_img.objects.get(id = image_id)
    
    image.delete()
    return redirect("gallery")


# =========================== category ======================


def category(request):
    categories = Add_img.objects.values_list('category', flat=True).distinct()
    category_images = [{'category': category, 'image': Add_img.objects.filter(category=category).first()} for category in categories]

    context = {
        'category_images': category_images
    }
    
    return render(request, 'category.html', context)



# ============================ sub category ======================


def sub_category(request, imgs_category):

    img = Add_img.objects.filter(category = imgs_category)

    parameter = {
        "images" : img,
        "category": imgs_category
    }
    
    return render(request,"sub_category.html",parameter)








