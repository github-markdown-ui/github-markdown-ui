import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='github-markdown-ui',
    version='0.0.1',
    packages=setuptools.find_packages(exclude=['test']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/github-markdown-ui/github-markdown-ui'
)
