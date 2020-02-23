from .crud_users import *

""" the following views are to control users and admins 
    all the functions called here are implemented in crud_users.py file
    @author AbdAllah Zidan """

def users(request):
    return manager_show_normal_users(request)  

def admins(request):
    return manager_show_admins(request) 

def show(request,id):
    return manager_show_user(request,id) 

def lock(request , id):
    return manager_lock_user(request , id)
    
def delete(request,id):
    return manager_delete_user(request,id)

def unlock(request , id):
    return manager_unlock_user(request , id)

def promote(request , id):
    return manager_promote_user(request,id)

def demote(request , id):
    return super_demote_admin(request , id)

def lock_admin(request,id):
    return super_lock_admin(request,id)

def unlock_admin(request , id):
    return super_unlock_admin(request , id)

def delete_admin(request , id):
    return super_delete_admin(request , id)

""" end of users control views """ 
