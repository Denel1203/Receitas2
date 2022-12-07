from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('buchada/',views.buchada),
    path('inhoque/',views.inhoque),
    path('bolo/',views.bolo),
    path('formu/',views.formulario),
    path('dado/<int:id>',views.mostr),
    path('comen/',views.comentarios),
    path('coment/',views.comentar),
    path('sobre/',views.sobre),
    

]