#!/bin/bash
gunicorn --max-requests 200 -w 4 --bind 0.0.0.0:4000 app:app