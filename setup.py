import setuptools

setuptools.setup(
    name="linechart_animator",
    version="0.0.0",
    author="Péntek Zsolt",
    description="Animate linecharts easily",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/amazon_scraper",
    packages=setuptools.find_packages(),
    install_requires=["matplotlib", "beautifulsoup4"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)