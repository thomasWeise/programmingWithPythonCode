echo # We create the directory '.venv' for the virtual environment.
md .venv

echo # We create the (empty) virtual environment inside the directory.
python -m venv .venv

echo # After creating the virtual environment, we activate it.
echo # Any Python program now uses the activated virtual environment.
call .venv\Scripts\activate.bat

echo # We install the package 'numpy' into the virtual environment.
pip install --require-virtualenv --progress-bar off numpy

echo # 'numpy' is now available for Python programs.
echo $ python numpy_user.py
python numpy_user.py 2>&1

echo # We deactivate the virtual environment.
echo # This means that programs now use the system environment only.
call deactivate

echo # 'numpy' is no longer available (unless installed system-wide).
echo python numpy_user.py
python numpy_user.py 2>&1

echo # We could re-use the virtual environment by activating it again.
echo # However, we delete the directory to clean up after the example.
rd /S /Q .venv
