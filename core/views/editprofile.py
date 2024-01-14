from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import EditProfileForm

@login_required(login_url='/')
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'core/edit.jinja', context={
        'form':form
    })