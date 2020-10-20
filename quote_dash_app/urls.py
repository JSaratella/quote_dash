from django.urls import path

from . import views

urlpatterns =[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('quotes',views.quotes),
    path('add_quote',views.add_quote),
    path('like/<int:quote_id>/<int:user_id>',views.like),
    path('show_user/<int:user_id>',views.user_view),
    path('logout',views.logout),
    path('delete_quote/<int:quote_id>',views.delete_quote),
    path('edit_user',views.edit_user),
    path('update_user',views.update_user),
]