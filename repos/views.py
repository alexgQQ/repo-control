from django.views.generic import ListView
from .models import GitRepo
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class HomePageView(ListView):
    model = GitRepo
    template_name = 'home.html'
    context_object_name = 'repos_list'
    allowed_methods = ['GET', 'POST']

    def post(self, request):
        for repo in GitRepo.objects.all():
            repo.pull()
        return HttpResponse('Success!')