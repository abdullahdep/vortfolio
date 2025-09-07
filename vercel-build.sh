#!/bin/bash

# Create necessary directories
mkdir -p /var/task/certs

# Copy SSL certificate
cp certs/isrgrootx1.pem /var/task/certs/

# Run migrations
python manage.py migrate

# Create initial page if it doesn't exist
python manage.py create_initial_pages
