from django.shortcuts import render

def django_page(request):
    context = {
        "page_title": "Ex01: Django, framework web.",
        "description": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It was originally developed in 2003 and released publicly in 2005.",
        "css_file": "style1.css"
    }
    return render(request, "ex01/django.html", context)

def display_page(request):
    context = {
        "page_title": "Ex01: Display process of a static page.",
        "description": "A static page is displayed by processing a template through a view. The view retrieves the template, passes context variables, and returns an HttpResponse with the rendered HTML.",
        "css_file": "style1.css"
    }
    return render(request, "ex01/display.html", context)

def template_page(request):
    context = {
        "page_title": "Ex01: Template engine.",
        "description": (
            "Django's template engine supports blocks, for-loops, if control structures, "
            "and context variable rendering. It allows you to create reusable templates. "
            "Blocks define sections that child templates can override; for-loops iterate over data; "
            "and if conditions allow conditional rendering."
        ),
        "css_file": "style2.css"
    }
    return render(request, "ex01/templates.html", context)
