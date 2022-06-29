import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup( 
    name="my_utils",
    version="0.0.3",
    author="Krzysztof Dobrowolski",
    author_email="k.dobrowolski1990@gmail.com",
    description="Package to create supporting functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where='src', exclude=('*test*', )),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires = ['pandas', 'requests'],
    extras_require = {
        'dev': [
            'unitest'
        ],
    }
)