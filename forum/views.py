from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from forum.models import Topic
from forum.forms import CommentForm, TopicForm

import os

def index(request):
    topics = Topic.objects.all()[:10]
    context = {'topics': topics,
               'topic_add_url':'add_topic',
               'topic_sorted':'sorted',
               'name':os.getlogin()}
    return render(request, 'index.html', context)

def sorted(request):
    topics = Topic.objects.all().order_by('-views')[:10]
    context = {'topics': topics,
               'topic_add_url':'add_topic',
               'topic_sorted':'sorted',
               'name':os.getlogin()}
    return render(request, 'index.html', context)

class TopicView(DetailView):
    model = Topic
    template_name = 'topic.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if True:
                q1 = Topic.objects.get(pk=context['topic'].id)
                q1.views += 1
                q1.save()
        context['comment_add_url'] = "/topic/{}/add_comment".format(context['topic'].id)
        return context

class CommentAdd(CreateView):
    template_name = 'comment_add.html'
    form_class = CommentForm

    def get_initial(self):
        return {
            "topic": self.kwargs['topic_pk']
        }

    def get_success_url(self):
        return "/topic/{}".format(self.kwargs['topic_pk'])


class TopicAdd(CreateView):
    template_name = 'topic_add.html'
    form_class = TopicForm

##    def get_initial(self):
##        return {
##            "topic": self.kwargs['topic_pk']
##        }

    def get_success_url(self):
        return ""#.format(self.kwargs['topic_pk'])



