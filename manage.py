#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherpy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # If the above import fails, we’ll be in trouble.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable?"
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
