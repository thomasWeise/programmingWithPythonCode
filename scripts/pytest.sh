#!/bin/bash -

# This is our internal pytest execution script.
# It prints the pytest command and the results of pytest.
# It always exits with an exit code 0, even if pytest fails.
# Argument $1: the folder to run it in
# Argument $2: the file(s) to scan

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# Is pytest is installed? If yes, get its version. If no, install it.
infos="$(python3 -m pip show pytest 2>/dev/null || true)"
if [ -z "$infos" ]; then
  # pytest is not installed, so we install it now.
  # We do this silently, without printing any information...
  python3 -m pip install pytest 1>/dev/null 2>&1
  infos="$(python3 -m pip show pytest 2>/dev/null)"
fi
# We now extract the version of pytest from the information string.
version="$(grep Version: <<< "$infos")"
version="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$version")"

# Construct the pytest command.
command="timeout 10s pytest --strict-config $2"

echo "\$ $command"  # We print the command line which will be executed.
cd "$1"  # We enter the folder inside of which we should execute pytest.

# Switch of "exit-on-error", run pytest, and afterwards switch it back on.
set +o errexit  # Turn off exit-on-error.
$command 2>&1  # Run pytest.
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

# Convert exit code to success or failure string.
[ "$exitCode" -eq 0 ] && exitCodeStr="succeeded" || exitCodeStr="failed"

# Finally, we print the result string.
echo "# pytest $version $exitCodeStr with exit code $exitCode."
