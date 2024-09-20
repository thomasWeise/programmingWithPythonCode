#!/bin/bash -

# This is our internal ruff execution script.
# It prints the ruff command and the results of ruff.
# It always exits with an exit code 0, even if ruff fails.
# Argument $1: the folder to run it in
# Argument $2: the file(s) to scan

# We enforce strict error handling, i.e., fail on any unexpected error.
set -o pipefail  # trace errors through pipes
set -o errtrace  # trace errors through commands and functions
set -o nounset   # exit if encountering an uninitialized variable
set -o errexit   # exit if any statement returns a non-0 return value

# First we check if ruff is installed and if so, get its version.
ruffInfos="$(pip show ruff 2>/dev/null || true)"
if [ -z "$ruffInfos" ]; then
  # ruff is not installed, so we install it now.
  # We do this silently, without printing any information...
  pip install ruff 1>/dev/null 2>&1
  ruffInfos="$(pip show ruff 2>/dev/null)"  # Now contains ruff version.
fi
# We now extract the version of ruff from the information string.
ruffVer="$(grep Version: <<< "$ruffInfos")"
ruffVer="$(sed -n 's/.*Version:\s*\([.0-9]*\)/\1/p' <<< "$ruffVer")"

# Construct the ruff command.
ruffCmd="ruff check --target-version py312 --select=A,AIR,ANN,ASYNC,B,BLE,C,C4,COM,D,DJ,DTZ,E,ERA,EXE,F,FA,FIX,FLY,FURB,G,I,ICN,INP,ISC,INT,LOG,N,NPY,PERF,PIE,PLC,PLE,PLR,PLW,PT,PYI,Q,RET,RSE,RUF,S,SIM,T,T10,TD,TID,TRY,UP,W,YTT --ignore=A005,ANN001,ANN002,ANN003,ANN101,ANN204,ANN401,B008,B009,B010,C901,D203,D208,D212,D401,D407,D413,INP001,N801,PLC2801,PLR0904,PLR0911,PLR0912,PLR0913,PLR0914,PLR0915,PLR0916,PLR0917,PLR1702,PLR2004,PLR6301,PT011,PT012,PT013,PYI041,RUF100,S,T201,TRY003,UP035,W --line-length 79 $2"

echo "\$ $ruffCmd"  # We print the command line which will be executed.
cd "$1"  # We enter the folder inside of which we should execute ruff.

# Switch of "exit-on-error", run ruff, and afterwards switch it back on.
set +o errexit  # Turn off exit-on-error.
$ruffCmd 2>&1  # Run ruff.
exitCode="$?"  # Store exit code of program in variable exitCode.
set -o errexit  # Turn exit-on-error back on.

if (("$exitCode" != 0)) ; then
  exitCodeStr="failed"  # ruff failed with a non-zero exit code.
else
  exitCodeStr="succeeded"  # ruff succeeded: the exit code is 0.
fi

# Finally, we print the result string.
echo "# ruff $ruffVer $exitCodeStr with exit code $exitCode."
