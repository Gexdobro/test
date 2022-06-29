# install package as lib + dependecies 
pip install -e .[dev]

# build python wheel
python setup.py sdist bdist_wheel