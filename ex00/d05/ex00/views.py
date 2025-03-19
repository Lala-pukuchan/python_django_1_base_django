from django.shortcuts import render


def index(request):
    context = {
        "markdown_info": [
            "Headers: # H1, ## H2, ### H3, ...",
            "Bold: **bold text**",
            "Italic: *italic text*",
            "Lists: - item1, - item2, ...",
            "Links: [text](url)",
            "Images: ![alt](url)",
        ]
    }
    return render(request, "ex00/index.html", context)
