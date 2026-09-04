"""Git branch operations."""
from gitassist.cli import output
from gitassist.git import branches as branch_ops
from gitassist.git.executor import run_git_command


def list_branches(show_all=False):
    """List local (or all) branches."""
    cmd = ["git", "branch", "-a"] if show_all else ["git", "branch"]
    return run_git_command(cmd, "Listing branches...")


def create_branch(name):
    """Create a new branch from current HEAD."""
    cmd = ["git", "branch", name]
    return run_git_command(cmd, f"Creating branch '{name}'")


def switch_branch(name):
    """Switch to an existing branch."""
    cmd = ["git", "switch", name]
    return run_git_command(cmd, f"Switching to branch '{name}'")


def delete_branch(name, force=False):
    """
    Delete a branch.
    force=True uses -D, otherwise -d (safe delete).
    """
    flag = "-D" if force else "-d"
    cmd = ["git", "branch", flag, name]
    return run_git_command(cmd, f"Deleting branch '{name}'")


def merge_branch(name):
    """Merge a branch into current branch."""
    cmd = ["git", "merge", name]
    return run_git_command(cmd, f"Merging branch '{name}' into current branch")
def manage_branches():
    """Branch management submenu."""
    while True:
        output.print_title("Branch Management")
        print("1. List branches")
        print("2. Create branch")
        print("3. Switch branch")
        print("4. Delete branch")
        print("5. Merge branch")
        print("0. Back to main menu")

        choice = ask_input("Enter choice:", allow_empty=False)

        if choice == "1":
            branch_ops.list_branches()
        elif choice == "2":
            name = ask_input("New branch name:")
            if name:
                if branch_ops.create_branch(name):
                    output.print_success(f"Branch '{name}' created.")
        elif choice == "3":
            name = ask_input("Branch name to switch to:")
            if name:
                if branch_ops.switch_branch(name):
                    output.print_success(f"Switched to '{name}'.")
        elif choice == "4":
            name = ask_input("Branch name to delete:")
            if name:
                force = ask_yes_no("Force delete (unmerged branches)?", default=False)
                if branch_ops.delete_branch(name, force):
                    output.print_success(f"Branch '{name}' deleted.")
        elif choice == "5":
            name = ask_input("Branch name to merge into current:")
            if name:
                if ask_yes_no(f"Merge '{name}' into current branch? This may cause conflicts."):
                    if branch_ops.merge_branch(name):
                        output.print_success(f"Merged '{name}'.")
        elif choice == "0":
            break
        else:
            output.print_error("Invalid choice.")

        output.print_line()