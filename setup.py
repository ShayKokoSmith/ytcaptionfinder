
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ytcaptionfinder',
    version='0.0.9',
    author='Shay Koko-Smith',
    author_email='shay.smith314@gmail.com',
    description='Finds string in youtube videos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ShayKokoSmith/ytcaptionfinder',
    packages=['.'],
    install_requires=['yt_dlp','tblib'],
)