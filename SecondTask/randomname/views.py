import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Member


def index(request):
    return render(request, 'randomname/members.html')


class MembersView(View):
    """Simple API class for model Members
    
    """
    queryset = Member.objects.all()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MembersView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Performs GET request processing for Member model.
        Args:
            request: Django request object
            *args: list positional arguments
            **kwargs: dictionary keyword arguments

        Returns:
            Http response object
        """
        winners = [member.name for member in self.queryset.order_by('?')[:3]]
        return JsonResponse({'winners': winners}, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        name = data['name']
        try:
            Member.objects.get(name=name)
            message = "Member is exists"
        except:
            Member.objects.create(name=name)
            message = "Member was created"

        return JsonResponse({'message': message}, safe=False)

    def delete(self , request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        name = body['name']
        try:
            Member.objects.get(name=name).delete()
            message = "Member was deleted"
        except:
            message = "Member was not deleted"
        return JsonResponse({'message': message}, safe=False)


members = MembersView.as_view()
