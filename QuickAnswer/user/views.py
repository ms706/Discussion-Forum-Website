from django.shortcuts import render
from .forms import UserProfileForm
from .models import UserProfile
# Create your views here.

def editprofile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        ins=UserProfile.objects.filter(user=request.user)
        if ins:
            ins.delete()

        if form.is_valid():
        	form.instance.user = request.user
        	form.save()
        	return render(request, 'user/editprofile.html', {'form': form})
    else:
        form = UserProfileForm()
    return render(request, 'user/editprofile.html', {'form': form})