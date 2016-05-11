from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Question, Choice


# Create your views here.

def index(request):
    top_5_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        'top_5_questions': top_5_questions,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select choice",
        })

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse(
        'polls:results', args=[question.id]
    ))
