from setuptools import setup, find_packages

'''
Run the following code in your conda environment to make the package available
$ python setup.py develop
'''


with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = ['numpy >= 1.19.2',
                'xarray >= 0.16.2',
                'matplotlib >= 3.3.2',
                'statsmodels >= 0.12.2',
                'tqdm',
                'cartopy >= 0.18.0']


setup(
    name = "xmca",
    include_package_data = True,
    keywords = 'mca',
    author = "Niclas Rieger",
    author_email = "niclasrieger@gmail.com",
    description = "Maximum Covariance Analysis in Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/nicrie/xmca",
    packages = find_packages(),
    license = "GPL-3.0",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    version_config={
        "dev_template": "{tag}.post{ccount}",
        "dirty_template": "{tag}.post{ccount}"
    },
    setup_requires=['setuptools-git-versioning','numpy'],
    install_requires = requirements,
)
