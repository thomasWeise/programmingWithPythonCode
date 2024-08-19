#!/bin/bash -

## mypy execution script
## $1 the folder to run it in
## $2 is the parameter to mypy

# strict error handling
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# First we check if mypy is installed.
mypyInfos="$(pip show mypy 2>/dev/null || true)"
if [ -z "$mypyInfos" ]; then
  # mypy is not installed, so we install it now.
  # We do this silently, without printing any information...
  pip install mypy 1>/dev/null 2>&1
  mypyInfos="$(pip show mypy 2>/dev/null)"
fi
# Now we can obtain the version of mypy.
mypyVer="$(grep Version: <<< "$mypyInfos")"
mypyVer="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$mypyVer")"

# We print the mypy version and show the command line which is executed.
echo "\$ mypy $2 --no-strict-optional --check-untyped-defs"

# Now we enter the folder.
cd "$1"

# Switch of "exit-on-error", run mypy, and afterwards switch it back on.
set +o errexit
mypy $2 --no-strict-optional --check-untyped-defs --no-color-output 2>&1
exitCode="$?"
set -o errexit

# Finally, print the exit code.
if (("$exitCode" != 0)) ; then
  exitCodeStr="failed"
else
  exitCodeStr="succeeded"
fi
echo "# mypy $mypyVer $exitCodeStr with exit code $exitCode."

