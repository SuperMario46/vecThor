import setuptools

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vextors-SuperMario64",  
    version="0.0.1",
    author="Simone Spedicato",
    author_email="simonespedicatospf@gmail.com",
    description="A small package to deal with vectors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SuperMario46/vextors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
