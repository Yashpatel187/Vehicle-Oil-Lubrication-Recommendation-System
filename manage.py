# !/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# For run : Python (filename) runserver
        # python manage.py runserver

# TN 07 JK 7890
# KA 03 GH 3456
# DL 01 EF 9012
# MH 12 CD 5678
# GJ 01 AB 1234

# Test API key = rzp_test_Sq1G6FeQ1E3yzV
# Test key secret = ZlIudY4EFF8Y4st2yhQW09oM