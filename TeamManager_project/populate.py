import os

def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=10,
        likes=10)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=10,
        likes=10)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=10,
        likes=10)

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=10,
        likes=10)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=10,
        likes=10)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=10,
        likes=10)

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=10,
        likes=10)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=10,
        likes=10)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views, likes=likes)[0]
    return p

def add_cat(name, likes=0):
    c = Category.objects.get_or_create(name=name, likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Ragnarok population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamManager_project.settings')
    from ragnarok.models import Category, Page
    populate()