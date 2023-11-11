from app_users.models import UserProfileInfo  

def profile_image(request):
    profile_image_url = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfileInfo.objects.get(user=request.user)
            profile_image_url = user_profile.profile_pic.url
        except UserProfileInfo.DoesNotExist:
            pass

    return {'profile_image_url': profile_image_url}
