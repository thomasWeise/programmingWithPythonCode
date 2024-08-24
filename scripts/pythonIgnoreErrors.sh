#!/bin/bash -

# This program executes python but ignores the errors.
# Argument $1: the directory in which the command should run
# Argument $2: the file to run

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

execStr="python3 $2"  # Compose the execution string.

cd "$1"  # Enter the folder inside of which we should run the program.

# Switch of "exit-on-error", run the program, then switch it back on.
set +o errexit  # Turn off exit-on-error.
$execStr 2>&1 # Run the program
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

if (("$exitCode" != 0)) ; then
  exitCodeStr="failed"  # the execution failed with a non-zero exit code.
else
  exitCodeStr="succeeded"  # the execution succeeded: the exit code is 0.
fi

# Finally, we print the result string.
echo "# '$execStr' $exitCodeStr with exit code $exitCode."
