#!/bin/bash -

# This is our internal mypy execution script.
# It prints the mypy command and the results of mypy.
# It always exits with an exit code 0, even if mypy fails.
# Argument $1: the folder to run it in
# Argument $2: the file(s) to scan

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# First we check if mypy is installed and if so, get its version.
mypyInfos="$(pip show mypy 2>/dev/null || true)"
if [ -z "$mypyInfos" ]; then
  # mypy is not installed, so we install it now.
  # We do this silently, without printing any information...
  pip install mypy 1>/dev/null 2>&1
  mypyInfos="$(pip show mypy 2>/dev/null)"  # Now contains mypy version.
fi
# We now extract the version of mypy from the information string.
mypyVer="$(grep Version: <<< "$mypyInfos")"
mypyVer="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$mypyVer")"

# We print the command line which will be executed.
echo "\$ mypy $2 --no-strict-optional --check-untyped-defs"

cd "$1"  # We enter the folder inside of which we should execute mypy.

# Switch of "exit-on-error", run mypy, and afterwards switch it back on.
set +o errexit  # Turn off exit-on-error.
mypy $2 --no-strict-optional --check-untyped-defs --no-color-output 2>&1
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

if (("$exitCode" != 0)) ; then
  exitCodeStr="failed"  # mypy failed with a non-zero exit code.
else
  exitCodeStr="succeeded"  # mypy succeeded: the exit code is 0.
fi

# Finally, we print the result string.
echo "# mypy $mypyVer $exitCodeStr with exit code $exitCode."
