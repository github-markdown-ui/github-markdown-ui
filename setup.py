import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="github-markdown-ui",
    packages=setuptools.find_packages(),
)
