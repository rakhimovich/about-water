from apps.water.models import Articles
from apps.water.forms import Articlesform
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.shortcuts import render

class ArticleListView(ListView):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'articles'
    
def About(request):
    return render(request,'about.html',locals())


class ArticleCrateView(CreateView):
    model = Articles
    form_class = Articlesform
    template_name = 'create.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    
class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'article'
    
class ArticleUpdateView(UpdateView):
    model = Articles
    form_class = Articlesform
    template_name = 'update.html'
    success_url = '/'
    
    
class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'delete.html'
    success_url = '/'
    context_object_name = 'article'