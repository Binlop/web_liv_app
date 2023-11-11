from Processing_DNA.models import MyFiles

def user_files(request):
    if request.user.is_authenticated:
        user_files = MyFiles.objects.filter(user=request.user)
    else:
        user_files = None

    return {
        'username': request.session.get('username', None),
        'user_files': user_files
    }
