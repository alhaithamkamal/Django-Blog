from .models import Profile
def promote_to_staff(user):
    user.is_staff = True
    user.save()

def promote_to_super_user(user):
    promote_to_staff(user)
    user.is_superuser= True
    user.save()
def lock_user(user):
    profile = Profile.objects.get(user=user)
    profile.is_locked = True
    profile.save()
def unlock_user(user):
    profile = Profile.objects.get(user=user)
    profile.is_locked = False
    profile.save()
def isLocked(user):
    profile = Profile.objects.get(user=user)
    return profile.is_locked

