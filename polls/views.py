from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "result": list(polls.values("question","created_by__username","pub_date"))
    }
    return JsonResponse(data)


def polls_detail(request, pk):
    polls = get_object_or_404(Poll, pk=pk)
    data = dict(results={'question': polls.question, 'created_by': polls.created_by, 'pub_date': polls.pub_date})
    return JsonResponse(data)
