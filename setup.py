import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='sndboxapi',

     version='2.1',

     author="PR3R00T",

     author_email="PR3R00T@protonmail.com",

     description="A Python Wrapper for the SNDBOX Rest API",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/PR3R00T/SNDBOX-LIGHT-API",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
