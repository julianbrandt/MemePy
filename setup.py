import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="MemePy",
    version="1.2.1",
    description="Meme Generator for python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Julian Brandt",
    author_email='julian@julianbrandt.dk',
    url="https://github.com/julianbrandt/MemePy",
    packages=["MemePy"],
    package_data={"MemePy": ["Resources/*/*"]},
    license="MIT",
    install_requires=[
        "pillow",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)