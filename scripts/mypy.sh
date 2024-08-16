#!/bin/bash -

## mypy execution script
## $1 the folder to run it in
## $2 is the parameter to mypy

# strict error handling
set -o pipefail  # trace ERR through pipes
set -o errtrace  # trace ERR through 'time command' and other functions
set -o nounset   # set -u : exit the script if you try to use an uninitialized variable
set -o errexit   # set -e : exit the script if any statement returns a non-true return value

# First we check if mypy is installed.
mypyInfos="$(pip show mypy 2>/dev/null || true)"
if [ -z "$mypyInfos" ]; then
  # mypy is not installed, so we install it now.
  # We do this silently, without printing any information to standard out or error...
  pip install mypy 1>/dev/null 2>&1
  mypyInfos="$(pip show mypy 2>/dev/null)"
fi
# Now we can obtain the version of mypy.
mypyVersion="$(grep Version: <<< "$mypyInfos")"
mypyVersion="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$mypyVersion")"

# We print the mypy version and we will show the command line which is executed.
echo "\$ mypy $2 --no-strict-optional --check-untyped-defs 2>&1"

# Now we enter the folder.
cd "$1"

# Actually execute mypy.
# Before executing it, we switch of "exit-on-error" and later switch it back on.
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
echo "# mypy $mypyVersion $exitCodeStr with exit code $exitCode."
