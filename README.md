# SNDBOX-LIGHT-API
A Light wrapper for the SNDBOX Rest API written in Python3.
This wrapper can be used to communicate to the SNDBOX exposed Rest API to all for the submissions of samples to the platform.
As per the documentation found at: https://app.sndbox.com/docs/api The wrapper allows for the three functions:

    Search - Search the database for a md5hash.
    Submit - Submit a sample to the platform.
    Metadata - Gather information about a uploaded file.

In order to use the API you must first obtain a API Key, This is found by registering a account with SNDBOX(https://app.sndbox.com/register)
Then navigating to the profile section.

Below are the requirements for each function:

    search(apikey='123',md5hash='1bed6d8bdf2c1b7fd5e6badc08e7634a')
    submit(apikey='123',file='testsample.docx',email=False)    
    metadata(apikey='123',id='12345-33422-23134-122')

Providing all input is correct each function returns the full raw response from the SNDBOX Rest API.
    
this package relies on requests to make its calls, Please install requests with: 
    
    pip install requests

You can also install this package via pip with: 

    pip install sndboxapi

import the package into your code with:
    
    from sndbox import sndboxapi
