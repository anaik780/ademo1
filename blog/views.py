from django.shortcuts import render
from .models import Post, Club, Detail, Status
from django.views.generic import TemplateView
from django.contrib.auth.models import User


# posts = [
#     {
#         'author': 'AbhiKN',
#         'title': 'Saiyajin',
#         'content': 'Level 1',
#         'date_posted': 'June 11, 2020'
#     },
#     {
#         'author': 'PratyushaP',
#         'title': 'Human',
#         'content': 'Level 1',
#         'date_posted': 'Nov 18, 2020'
#     }
# ]

# Create your views here.
def home(request) :
    group_list = []
    for g in request.user.groups.all():
        group_list.append(g.name)
    context = {
        'posts': Post.objects.all(),
        'groups': group_list,
        'group_exist': request.user.groups.exists()
    }
    return render(request,'blog/home.html', context)

def about(request) :
    return render(request,'blog/about.html')

class ClubChartView(TemplateView):
    template_name = 'blog/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Club.objects.all()
        return context

def add_detail(request):
    status = Status.objects.values()
    users_dict = User.objects.values()
    users = []
    for i in range(len(User.objects.all())):
        users.append(users_dict[i]['username'])
    context = {
        'status': status,
        'users': users,
    }
    return render(request, 'blog/add_detail.html', context)