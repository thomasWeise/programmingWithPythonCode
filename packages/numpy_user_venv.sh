echo "# We create the directory '.venv' for the virtual environment."
mkdir -p .venv

echo "# We create the (empty) virtual environment inside the directory."
python3 -m venv .venv

echo "# After creating the virtual environment, we activate it."
echo "# Any Python program now uses the activated virtual environment."
source .venv/bin/activate

echo "# We install the package 'numpy' into the virtual environment."
pip install --require-virtualenv --progress-bar off numpy

echo "# 'numpy' is now available for Python programs."
echo "$ python3 numpy_user.py"
python3 numpy_user.py 2>&1

echo "# We deactivate the virtual environment."
echo "# This means that programs now use the system environment only."
deactivate

echo "# 'numpy' is no longer available (unless installed system-wide)."
echo "$ python3 numpy_user.py"
python3 numpy_user.py 2>&1 || true

echo "# We could re-use the virtual environment by activating it again."
echo "# However, we delete the directory to clean up after the example."
rm -rf .venv
