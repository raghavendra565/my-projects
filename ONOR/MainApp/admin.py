"""from django.contrib import admin
from .models import Users,Categories,Carousel,Categoriecarousel,Listings,Listing_images



class UsersDetails(admin.ModelAdmin):
    list_display=('id','name','mobile','email')
admin.site.register(Users,UsersDetails)



class CategoriesDetails(admin.ModelAdmin):
    list_display = ('id','name','image')
admin.site.register(Categories,CategoriesDetails)



class CarouselDetails(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Carousel,CarouselDetails)



class CatcarouselDetails(admin.ModelAdmin):
    list_display = ('id','categorie')
admin.site.register(Categoriecarousel,CatcarouselDetails)

class ListingsDetails(admin.ModelAdmin):
    list_display = ('id','name','address','mobile','email','image','description','status')
admin.site.register(Listings,ListingsDetails)

class List_imagesDetails(admin.ModelAdmin):
    list_display = ('id','listing','images','status')
admin.site.register(Listing_images,List_imagesDetails)"""
