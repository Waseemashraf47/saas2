from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir =  pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    # print(this_dir)
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Title Page"
    my_context = {
        "page_title": my_title,
        # "queryset" : queryset,
        "page_visit_count" : page_qs.count(),
        "percent" : (page_qs.count()*100) / qs.count(),
        "total_visits_count" : qs.count(),
    }
    
    path = request.path
    print("path", path)
    html_template ="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    print(this_dir)
    my_title = "My Page 1"
    my_context = {
        "page_title": my_title
    }
    html_ ="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Inline This is {page_title}?</h1>
</body>
</html>
    """.format(**my_context)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    # return HttpResponse("<h1>Hello World</h1>")
    return HttpResponse(html_)