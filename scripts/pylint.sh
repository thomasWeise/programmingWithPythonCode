#!/bin/bash -

# This is our internal pylint execution script.
# It prints the pylint command and the results of pylint.
# It always exits with an exit code 0, even if pylint fails.
# Argument $1: the folder to run it in
# Argument $2: the file(s) to scan

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# First we check if pylint is installed and if so, get its version.
pylintInfos="$(pip show pylint 2>/dev/null || true)"
if [ -z "$pylintInfos" ]; then
  # pylint is not installed, so we install it now.
  # We do this silently, without printing any information...
  pip install pylint 1>/dev/null 2>&1
  pylintInfos="$(pip show pylint 2>/dev/null)"  # Now contains pylint version.
fi
# We now extract the version of pylint from the information string.
pylintVer="$(grep Version: <<< "$pylintInfos")"
pylintVer="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$pylintVer")"

# Construct the pylint command.
pylintCmd="pylint $2 --disable=C0103,C0302,C0325,R0801,R0901,R0902,R0903,R0911,R0912,R0913,R0914,R0915,R1702,R1728,W0212,W0238,W0703"

echo "\$ $pylintCmd"  # We print the command line which will be executed.
cd "$1"  # We enter the folder inside of which we should execute pylint.

# Switch of "exit-on-error", run pylint, and afterwards switch it back on.
set +o errexit  # Turn off exit-on-error.
$pylintCmd 2>&1  # Run pylint.
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

if (("$exitCode" != 0)) ; then
  exitCodeStr="failed"  # pylint failed with a non-zero exit code.
else
  exitCodeStr="succeeded"  # pylint succeeded: the exit code is 0.
fi

# Finally, we print the result string.
echo "# pylint $pylintVer $exitCodeStr with exit code $exitCode."
