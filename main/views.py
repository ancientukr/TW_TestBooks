from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.views import View
from .models import Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy


class BookDetailView(DetailView):
    """Class inherits DetailView. Model Book"""
    model = Book


class BookList(ListView):
    """Class inherits ListView. Model Book"""
    model = Book


class BookCreate(CreateView):
    """Class inherits ListView. Model Book

    Fields for form:
      ['name','description','author','year','pages','rating']
    """

    model = Book
    success_url = reverse_lazy('book_list')
    fields = ['name',
              'description',
              'author',
              'year',
              'pages',
              'rating']


class BookUpdate(UpdateView):
    """Class inherits UpdateView. Model Book

    Fields for form:
      ['name','description','author','year','pages','rating']
    """
    model = Book
    success_url = reverse_lazy('book_list')
    fields = ['name',
              'description',
              'author',
              'year',
              'pages',
              'rating']


class BookDelete(DeleteView):
    """Class inherits DeleteView. Model Book"""
    model = Book
    success_url = reverse_lazy('book_list')


class ESearchView(View):
    """Class for implementing a search in the database by the name of the book.

    Paginator size: 5
    """

    template_name = 'main/search.html'

    def get(self, request, *args, **kwargs):
        """Search object in data base and save result in context['book_lists']

        Paginator size: 5
        """
        context = {}
        question = request.GET.get('q')

        if question is not None:
            search_book = Book.objects.filter(name=question)
            context['last_question'] = '?q=%s' % question
            current_page = Paginator(search_book, 5)
            page = request.GET.get('page')
            try:
                context['book_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['book_lists'] = current_page.page(1)
            except EmptyPage:
                context['book_lists'] = current_page.page(current_page.num_pages)

        return render_to_response(template_name=self.template_name, context=context)
