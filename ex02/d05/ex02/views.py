from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import InputForm
from django.conf import settings
import os

def index(request):
    history = []
    log_file = settings.LOG_FILE_PATH
    # read log file
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                history.append(line.strip())
    # handle POST request
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            timestamp = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp}: {text}"
            history.append(entry)
            # write to log file
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(entry + "\n")
            return redirect("ex02_index")
    else:
        # GET request
        # create a new form
        form = InputForm()
    # pass the form and history to the template as context
    context = {"form": form, "history": history}
    return render(request, "ex02/index.html", context)
