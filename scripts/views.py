from django.shortcuts import render, redirect, get_object_or_404
from .forms import WriteScriptForm
from django.contrib.auth.decorators import login_required
from .models import Script

# Create your views here.
@login_required
def write(request):
    if request.method == 'POST':
        form = WriteScriptForm(request.user, request.POST)
        if form.is_valid():
            script = form.save(commit=False)
            script.author = request.user
            script.save()
            return redirect('profile')
    else:
        form = WriteScriptForm(request.user)

    return render(request, 'scripts/write.jinja', context={
        'form':form
    })

@login_required
def delete_script(request, script_id):
    script = get_object_or_404(Script, id=script_id)
    script.delete()
    return redirect('profile')

def script_detail(request, script_slug):
    script = get_object_or_404(Script, slug=script_slug)
    return render(request, 'scripts/detail.jinja', context={
        'script':script
    })