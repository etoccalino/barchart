from setuptools import setup, find_packages
setup(
    name = "barchart",
    version = "0.6",
    py_modules = ['barchar'],
    scripts = ["bin/barchart", "bin/dub"],

    package_data = {
        '': ['*.rst', '*.rst'],
        },

    author = "Elvio Toccalino",
    author_email = "elviotoccalino@gmail.com",
    license = "GPLv3",
    keywords = "console terminal du barchart",
    url = "http://github.com/etoccalino/barchart/",
    description = "Produce a bar chart of file/directory sizes.",
    long_description = open('README.rst').read(),
)
