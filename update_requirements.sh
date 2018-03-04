#!/bin/bash

# Requires that you are in the root directory
# Requires that you have a virtual env at project_dir/venv

. venv/bin/activate
pip freeze > requirements.txt
