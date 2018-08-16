from django.db import models
from django.utils.crypto import get_random_string
#from stringfield import StringField
#from encrypted_model_fields.fields import EncryptedCharField
#import crypt

def file1(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), filename)
def file2(instance, filename):
    return 'pics/{0}{1}'.format(get_random_string(length=10), filename)
def file3(instance, filename):
    return 'photos/{0}{1}'.format(get_random_string(length=10), filename)
def file4(instance, filename):
    return 'file4images/{0}{1}'.format(get_random_string(length=10), filename)
def file5(instance, filename):
    return 'file5images/{0}{1}'.format(get_random_string(length=10), filename)

class Roles(models.Model):
    name           = models.CharField(max_length = 30)
    status         = models.BooleanField()
    created_at     = models.DateTimeField(auto_now = True)
    updated_at     = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%d %s" % (self.id,self.name)


class Users(models.Model):
    first_name    = models.CharField(max_length=30)
    last_name     = models.CharField(max_length=30)
    mobile        = models.CharField(max_length = 10)
    email         = models.EmailField(blank = True,default="",unique=True)
    password      = models.CharField(max_length=500)
    address       = models.TextField(max_length = 80)
    role          = models.ForeignKey(Roles,on_delete = models.CASCADE,default = None)
    status        = models.BooleanField()
    created_at    = models.DateTimeField(auto_now = True)
    updated_at    = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "%d"% (self.id)
        #self.first_name+ " "+ self.last_name

class MainpageCarousel(models.Model):
    name          = models.CharField(max_length = 40)
    user          = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    status        = models.BooleanField()
    created_at    = models.DateTimeField(auto_now = True)
    updated_at    = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%d %s" % (self.id,self.name)

class Carousel(models.Model):
    image   = models.ImageField(upload_to = file1,
                              blank=True,
                              null=True)
    user     = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    mainpage = models.ForeignKey(MainpageCarousel,on_delete = models.CASCADE,default = None)
    status   = models.BooleanField()
    created  = models.DateTimeField(auto_now = True)
    updated  = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "%d %s" % (self.id,self.user.name)


class Categories(models.Model):
    name       = models.CharField(max_length=30)
    image      = models.ImageField(upload_to = file2,
                              blank=True,
                              null=True)
    user       = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    status     = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "%d %s" % (self.id,self.name)

class Categoriecarousel(models.Model):
    category      = models.ForeignKey(Categories,on_delete = models.CASCADE,default = None)
    image         = models.ImageField(upload_to = file3,
                              blank=True,
                              null=True)
    user          = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    status        = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now = True)
    updated_at    = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%d %s" % (self.id,self.user)

class Listings(models.Model):
    name          = models.CharField(max_length=30)
    address       = models.TextField(max_length = 80)
    mobile        = models.CharField(max_length = 10)
    email         = models.EmailField(blank = True,default="",unique=True)
    categorie     = models.ForeignKey(Categories,on_delete = models.CASCADE,default = None)
    image         = models.ImageField(upload_to = file4,
                              blank=True,
                              null=True)
    user          = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    description   = models.TextField(max_length=500)
    status        = models.BooleanField()
    created_at    = models.DateTimeField(auto_now = True)
    updated_at    = models.DateTimeField(auto_now = True)



    def __str__(self):
        return "%d %s" % (self.id,self.name)

class Listing_images(models.Model):
    listing        = models.ForeignKey(Listings,on_delete = models.CASCADE,default = None)
    image          =  models.ImageField(upload_to = file5,
                              blank=True,
                              null=True)
    user           = models.ForeignKey(Users,on_delete = models.CASCADE,default = None)
    status         = models.BooleanField()
    created_at     = models.DateTimeField(auto_now = True)
    updated_at     = models.DateTimeField(auto_now = True)



    def __str__(self):
        return "%d %s" % (self.id,self.user)
