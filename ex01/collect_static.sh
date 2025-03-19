#!/bin/bash

cd d05
python manage.py collectstatic

# https://stackoverflow.com/questions/34586114/whats-the-point-of-djangos-collectstatic
# Collect static files from multiple apps into a single path
# Well, a single Django project may use several apps, so while there you only have one myapp, it may actually be myapp1, myapp2, etc
# By copying them from inside the individual apps into a single folder, you can point your frontend web server (e.g. nginx) to that single folder STATIC_ROOT and serve static files from a single location, rather than configure your web server to serve static files from multiple paths.
