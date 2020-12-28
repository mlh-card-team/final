from django.urls import path
from . import views

app_name = 'card_maker'


urlpatterns = [
path ('',views.homepage, name='homepage'),
path ('holidays',views.post_list, name='holidays'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',
views.post_detail, name='post_detail'),
path('cards',views.card_view,name='cards'),
path('about',views.about,name='about'),
path('contact',views.contact,name='contact'),
path('search',views.post_search,name='search'),
path('christmas_cards',views.christmas_cards,name='christmas_cards'),
path('hanukkah_cards',views.hanukkah_cards,name='hanukkah_cards'),
path('kwanzaa_cards',views.kwanzaa_cards,name='kwanzaa_cards'),
path('boxing_day_cards',views.boxing_day_cards,name='boxing_day_cards'),
path('omisoka_cards',views.omisoka_cards,name='omisoka_cards'),
path('saint_nickolas_day_cards',views.saint_nickolas_day_cards,name='saint_nickolas_day_cards'),
path('winter_solstice_cards',views.winter_solstice_cards,name='winter_solstice_cards'),
path('mardi_gras_cards',views.mardi_gras_cards,name='mardi_gras_cards'),

]
