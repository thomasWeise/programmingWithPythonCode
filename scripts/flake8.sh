#!/bin/bash -

# This is our internal flake8 execution script.
# It prints the flake8 command and the results of flake8.
# It always exits with an exit code 0, even if flake8 fails.
# Argument $1: the folder to run it in
# Argument $2: the file(s) to scan

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# Check if flake8 and all required plugins are installed.
versions=""  # This variable will receive all tool versions.
for flake in "flake8" "flake8-bugbear" "flake8-eradicate" "flake8-use-fstring" "flake8-pie" "dlint"; do
  infos="$(python3 -m pip show "$flake" 2>/dev/null || true)"
  if [ -z "$infos" ]; then
    # flake8 or the plugin is not installed, so we install it now.
    # We do this silently, without printing any information...
    python3 -m pip install "$flake" 1>/dev/null 2>&1
    infos="$(python3 -m pip show "$flake" 2>/dev/null)"
  fi

  # For each tool or plugin, we get the version separately.
  infos="$(grep Version: <<< "$infos")"
  infos="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$infos")"
  if [ -z "$versions" ]; then  # ... and we concatenate them
    versions="$flake $infos with plugins"
  elif [[ "$versions" == *plugins ]]; then
    versions="$versions $flake $infos"
  else
    versions="$versions, $flake $infos"
  fi
done

# Construct the flake8 command.
command="flake8 $2 --ignore=B008,B009,B010,DUO102,TRY003,TRY101,W503"

echo "\$ $command"  # We print the command line which will be executed.
cd "$1"  # We enter the folder inside of which we should execute flake8.

# Switch of "exit-on-error", run flake8, and afterwards switch it back on.
set +o errexit  # Turn off exit-on-error.
$command 2>&1
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

# Convert exit code to success or failure string.
[ "$exitCode" -eq 0 ] && exitCodeStr="succeeded" || exitCodeStr="failed"

# Finally, we print the result string.
echo "# $versions $exitCodeStr with exit code $exitCode."
