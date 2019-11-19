import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerline_dice",
    version="1.0.0",
    license="GPLv3+",
    author="Miguel de Dios Matias",
    author_email="tres.14159@gmail.com",
    description="A toy Powerline segment. This segment shows a result of dice combination.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdtrooper/powerline_dice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Games/Entertainment"
    ],
    python_requires='>=3.7',
    install_requires=[
        'dice>=2.4.2'
    ],
    platforms=['any']
)