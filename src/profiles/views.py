from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model

User=get_user_model()


@login_required
def profile_list_view(request):
    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    
    return render(request, "profiles/list.html", context)


@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    user_groups = user.groups.all()
    print(
        user.has_perm("subscriptions.basic"),
        user.has_perm("subscriptions.pro"),
        user.has_perm("subscriptions.advanced"),
        )
    # print("User_Groups", user_groups)
    # if user_groups.filter(name__icontains='basic').exists():
    #     return HttpResponse("CONGRATULATIONS")
    
    # print(user.has_perm("Authentication and Authorization | user | Can view user"))
    # print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    # print('user.has_perm("visits.view_pagevisit")', user.has_perm("visits.view_pagevisit"))
    # user = get_object_or_404(User, username__iexact=username)
    
    #<app_label>.view_<model_name>
    #<app_label>.add_<model_name>
    #<app_label>.change_<model_name>
    #<app_label>.delete_<model_name>
    
    # profile_user_obj=User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me,
    }
    # if is_me:
    #     if user.has_perm("visits.view_pagevisits"):
    #         pass        
            #qs = PageVisits.objects.all()
    return render(request, "profiles/detail.html", context)