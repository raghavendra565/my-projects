from django.conf.urls import url
from MainApp.controllers.createcategories import createcategories
from MainApp.controllers.createusers import createusers
from MainApp.controllers.createcarousel import createcarousels
from MainApp.controllers.createlisting import createlistings
from MainApp.controllers.createroles import createroles
from MainApp.controllers.createmainpagecarousel import createmainpagecarousel
from MainApp.controllers.createcategoriecarousels import createcategoriecarousels
from MainApp.controllers.createlisting_images import createlisting_images
from MainApp.controllers.categorie import getupdatedeletecategories
from MainApp.controllers.user import getupdatedeleteusers
from MainApp.controllers.carousels import getupdatedeletecarousels
from MainApp.controllers.listing import getupdatedeletelistings
from MainApp.controllers.listing_images import getupdatedeletelisting_images
from MainApp.controllers.categoriecarousels import getupdatedeletecategoriecarousels
from MainApp.controllers.roles import getupdateroles
from MainApp.controllers.mainpagecarousel import getupdatedeletemainpagecarousels
from MainApp.views import users,send


urlpatterns=[
        url(r'^users',users),
        url(r'^send',send),
        url(r'^createcategories',createcategories.as_view()),
        url(r'^createcategoriecarousels',createcategoriecarousels.as_view()),
        url(r'^createusers',createusers.as_view()),
        url(r'^createroles',createroles.as_view()),
        url(r'^createmainpagecarousel',createmainpagecarousel.as_view()),
        url(r'^createcarousels',createcarousels.as_view()),
        url(r'^createlistings',createlistings.as_view()),
        url(r'^createlisting_images',createlisting_images.as_view()),
        url(r'^getupdatedeletecarousels/(?P<id>[0-99,-]+)',getupdatedeletecarousels.as_view()),
        url(r'^getupdatedeletecatcarousels/(?P<id>[0-99,-]+)',getupdatedeletecategoriecarousels.as_view()),
        url(r'^getupdatedeleteusers/(?P<id>[0-99,-]+)',getupdatedeleteusers.as_view()),
        url(r'^getupdatedeletecategories/(?P<id>[0-99,-]+)',getupdatedeletecategories.as_view()),
        url(r'^getupdatedeletelistings/(?P<id>[0-99,-]+)',getupdatedeletelistings.as_view()),
        url(r'^getupdatedeletelisting_images/(?P<id>[0-99,-]+)',getupdatedeletelisting_images.as_view()),
        url(r'^getupdatedeleteroles/(?P<id>[0-99,-]+)',getupdateroles.as_view()),
        url(r'^getupdatedeletemainpagecarousels/(?P<id>[0-99,-]+)',getupdatedeletemainpagecarousels.as_view())
]
