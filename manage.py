import os
import sys

from django.core import management


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sugar.settings")
    management.execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
