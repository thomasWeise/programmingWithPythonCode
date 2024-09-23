#!/bin/bash -

# This program executes python but ignores the errors.
# Argument $1: the directory in which the command should run
# Argument $2: the file to run

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# Find the Python interpreter. PYTHON_INTERPRETER maybe set by latexgit.
if [[ $(declare -p PYTHON_INTERPRETER 2>/dev/null) != declare\ ?x* ]]; then
  export PYTHON_INTERPRETER="$(which python3)"  # If not, then we set it.
fi

cd "$1"  # Enter the folder inside of which we should run the program.

# Switch of "exit-on-error", run the program, then switch it back on.
set +o errexit  # Turn off exit-on-error.
"$PYTHON_INTERPRETER" $2 2>&1 # Run the program
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

# Convert exit code to success or failure string.
[ "$exitCode" -eq 0 ] && exitCodeStr="succeeded" || exitCodeStr="failed"

# Finally, we print the result string.
echo "# 'python3 $2' $exitCodeStr with exit code $exitCode."
