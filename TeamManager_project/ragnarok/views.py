from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from ragnarok.models import Category, Page
from ragnarok.forms import CategoryForm, PageForm


def encode_url(string):
    return string.replace(' ','_')

def decode_url(string):
    return string.replace('_',' ')

def get_category_list():
    cat_list = []
    cat_list = Category.objects.all()
    for cat in  cat_list:
        cat.url = encode_url(cat.name)

    return cat_list


def index(request):

    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # page top 5
    page_hitlist = Page.objects.order_by("-views")[:5]
    context_dict['pages'] = page_hitlist

    for category in category_list:
        # category.url = category.name.replace(' ', '_')
        category.url = encode_url(category.name)

    return render_to_response('ragnarok/index.html', context_dict, context)


def category(request, category_name_url):
    context = RequestContext(request)
    category_name = decode_url(category_name_url)
    context_dict = {'category_name': category_name, 'category_name_url': category_name_url}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('ragnarok/category.html', context_dict, context)


def about(request):
    return HttpResponse("This is about Ragnarok...")

def members(request):
    return HttpResponse("Members of Ragnarok...")

def add_category(request):
    context = RequestContext(request)
    context_dict = {}


    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print form.errors
    else:
        form = CategoryForm
    context_dict['form'] = form
    return render_to_response('ragnarok/add_category.html', context_dict, context)

def add_page(request, category_name_url):
    context = RequestContext(request)
    context_dict = {}
    category_name = decode_url(category_name_url)
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)

            try:
                cat = Category.objects.get(name = category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response('ragnarok/add_category.html',
                                          context_dict,
                                          context)

            page.views = 0

            page.save()

            return category(request, category_name_url)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['category_name_url'] = category_name_url
    context_dict['category_name'] = category_name
    context_dict['form'] = form
    return render_to_response('ragnarok/add_page.html',
                              context_dict,
                              context)


#def index(request):
#    # Request the context of the request.
#    # The context contains information such as the client's machine details, for example.
#    context = RequestContext(request)
#
#    # Construct a dictionary to pass to the template engine as its context.
#    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
#    context_dict = {'boldmessage': "I am bold font from the context"}
#
#    # Return a rendered response to send to the client.
#    # We make use of the shortcut function to make our lives easier.
#    # Note that the first parameter is the template we wish to use.
#    return render_to_response('ragnarok/index.html', context_dict, context)