import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonviewer",
    version="0.1.4",
    author="fangyh09",
    author_email="fangyh09@gmail.com",
    description="display json meta structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fangyh09/json-viewer",
    packages=setuptools.find_packages(),
)