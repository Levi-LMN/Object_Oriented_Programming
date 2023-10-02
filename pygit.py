#!/usr/bin/env python3

import sys
import subprocess

# Get the commit message from the command line argument
commit_message = " ".join(sys.argv[1:])

# Check if a commit message is provided
if not commit_message:
    print("Please provide a commit message.")
    sys.exit(1)

try:
    # Run git add, commit, and push commands
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Changes successfully committed and pushed to remote repository.")
except subprocess.CalledProcessError as e:
    print("An error occurred:", e)
    sys.exit(1)
