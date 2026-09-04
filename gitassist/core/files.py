"""File management operations for GitAssist."""

import os
from gitassist.cli.output import print_error, print_success
from gitassist.cli.input_handler import ask_input, ask_yes_no
from gitassist.localization.texts import get_text


def create_file():
    filename = ask_input(get_text("filename_prompt"), allow_empty=False)
    if os.path.exists(filename):
        print_error(get_text("file_exists_error", name=filename))
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("")
        print_success(get_text("file_created", name=filename))
    except Exception as e:
        print_error(f"Failed to create file: {e}")


def edit_file():
    filename = ask_input(get_text("file_to_edit"), allow_empty=False)
    if not os.path.isfile(filename):
        print_error(get_text("file_not_found", name=filename))
        return
    line = ask_input(get_text("line_to_append"), allow_empty=False)
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line + "\n")
        print_success(get_text("line_appended", name=filename))
    except Exception as e:
        print_error(f"Failed to edit file: {e}")


def delete_file():
    filename = ask_input(get_text("file_to_delete"), allow_empty=False)
    if not os.path.isfile(filename):
        print_error(get_text("file_not_found", name=filename))
        return
    if ask_yes_no(get_text("delete_confirm", name=filename)):
        try:
            os.remove(filename)
            print_success(get_text("file_deleted", name=filename))
        except Exception as e:
            print_error(f"Failed to delete file: {e}")


def create_directory():
    dirname = ask_input(get_text("dirname_prompt"), allow_empty=False)
    if os.path.exists(dirname):
        print_error(get_text("file_exists_error", name=dirname))
        return
    try:
        os.makedirs(dirname)
        print_success(get_text("file_created", name=dirname))
    except Exception as e:
        print_error(f"Failed to create directory: {e}")