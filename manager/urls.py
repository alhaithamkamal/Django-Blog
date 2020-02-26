from django.urls import path
from . import views


"""the part of urls begins with users/ or admins/ is to handle all crud operations on users and admins
    @ author: AbdAllah Zidan """
    
urlpatterns = [
        path("users/",views.users , name="users"),
        path("admins/",views.admins , name="admins"),
        path("users/delete/<int:id>/",views.delete , name="delete"),
        path("users/lock/<int:id>/",views.lock,name="lock"),
        path("users/show/<int:id>/" , views.show,name="show"),
        path("users/unlock/<int:id>/" , views.unlock , name ="unlock"),
        path("users/promote/<int:id>/" , views.promote , name ="promote"),
        path("admins/demote/<int:id>",views.demote , name="demote"),
        path("admins/lock/<int:id>" , views.lock_admin , name="lock_admin" ),
        path("admins/unlock/<int:id>",views.unlock_admin , name="unlock_admin"),
        path("admins/delete/<int:id>" , views.delete_admin , name="delete_admin"),
        path("admins/show/<int:id>",views.show , name="show_admin"),
    ]