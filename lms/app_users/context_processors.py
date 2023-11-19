from app_users.models import UserProfileInfo  

def profile_image(request):
    profile_image_url = 'https://example.com/path_to_default_image.png'
    if request.user.is_authenticated:
        try:
            user_profile = UserProfileInfo.objects.get(user=request.user)
            profile_image_url = user_profile.profile_pic.url
        except UserProfileInfo.DoesNotExist:
            pass

    return {'profile_image_url': profile_image_url}
