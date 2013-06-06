# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from tabTrunkApp.models import Tab
from django.contrib.auth.models import User

# Users
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tab_list = Tab.objects.filter(username=request.user.username).order_by('-addedDate')
    #if tab_list.count() = 0
    return render(request, 'tabTrunkApp/index.html',
                  {'tab_list': tab_list},
                  context_instance=RequestContext(request),)
@login_required
def detail(request, tab_id):
    # TODO: Add user specific protections (ie if tab.username = request.username)
    tab = get_object_or_404(Tab, pk=tab_id)
    return render(request, 'tabTrunkApp/view.html', {'tab': tab},
                  context_instance=RequestContext(request),)

@login_required
def edit(request, tab_id):
    # TODO: Add user specific protections (ie if tab.username = request.username)
    tab = get_object_or_404(Tab, pk=tab_id)
    tabAbility = tab.get_ability_display()

    if request.POST:
        if request.POST['submit'] == 'save':
            tab.songTitle = request.POST['songTitle']
            tab.artist = request.POST['artist']
            tab.tabURL = request.POST['tabURL']
            tab.content = request.POST['content']
            tab.save()
        return render(request, 'tabTrunkApp/view.html', {'tab':tab},
                      context_instance=RequestContext(request),)

    return render(request, 'tabTrunkApp/edit.html', {'tab': tab, 'tabAbility': tabAbility},
                  context_instance=RequestContext(request),)

@login_required
def new(request):
    return render(request, 'tabTrunkApp/new.html',
                  {'abilityChoices': getattr(Tab, "abilityChoices") },
                  context_instance=RequestContext(request),)
@login_required
def create(request):

    if request.POST:
        if request.POST['submit'] == 'create':
            tab = Tab(
                songTitle=request.POST['songTitle'],
                artist=request.POST['artist'],
                tabURL=request.POST['tabURL'],
                content=request.POST['content'],
                ability=request.POST['ability'],
                addedDate=timezone.now(),
                username=request.user.username)

            tab.save()
            return render(request, 'tabTrunkApp/view.html', {'tab': tab},
                          context_instance=RequestContext(request),)
    return index(request)

@login_required
def delete(request, tab_id):
    # TODO: Add user specific protections (ie if tab.username = request.username)
    tab = get_object_or_404(Tab, pk=tab_id)

    if request.POST:
        if request.POST['submit'] == 'delete':
            tab.delete()
            return index(request)
        return detail(request, tab_id)

    return render(request, 'tabTrunkApp/confirmDelete.html', {'tab': tab},
                  context_instance=RequestContext(request),)


def register(request):
    if request.POST:
        if request.POST['register'] == 'register':
            if request.POST['inputPassword'] == request.POST['inputPasswordConfirm']:
                if request.POST['inputRegistrationCode'] == 'r2d2':
                    user = User.objects.create_user(username=request.POST['inputUsername'],
                                                    email=request.POST['inputEmail'],
                                                    password=request.POST['inputPassword'])
                    user.save()
    return index(request)