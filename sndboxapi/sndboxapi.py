#!/usr/bin/python3

import requests
import sys

def search(apikey,md5hash):
    '''
    Search the SNDBOX Database for Hash of Sample.
    Input:
    API Key - For authenication
    md5hash - For sample check
    Output:
    Response from check in json format if parameters are vaild.
    '''
    #Prep Call
    try:
        response = requests.get("https://api.sndbox.com/developers/files/verdict?apikey="+apikey+"&hash="+md5hash)
    except Exception as e:
        sys.exit("Error Occurred connecting to the SNDBOX API - " + str(e))
    #Check Response
    if response.status_code == 200 or response.status_code == 404:
        return response
    elif response.status_code == 400:
        sys.exit("Bad Parameter, Error with MD5 Hash Format")
    elif response.status_code == 401:
        sys.exit("API Key incorrect")


def file_check(file):
    '''
    Check a sample if it is supported on the SNDBOX enviroment
    Input:
    File - string name of File
    output:
    Boolen - True/False
    '''
    #File Extension Check
    supported_files=[".raw",".doc",".dot",".xls",".csv",".xlt",".xlm",".ppt",".pot",".pps",".docx",".docm",".dotx",".dotm",".dotm",".xlsx",".xlsm",".xltx",".xltm",".xlsb",".xla",".xlam",".iqy",".pptx",".pptm",".potx",".ppsx",".xml",".pe32",".rtf",".pdf",".vbs",".vbe",".ps1",".js",".lnk",".html",".bat",".zip"]
    supported_sample = False
    while supported_sample == False:
        if "." not in file:
            supported_sample = True
            return True
        else:
            for file_ext in supported_files:
                if file_ext in file:
                    supported_sample = True
                    return True
                else:
                    return False



def submit(apikey,file,email):
    '''
    submit a File to the SNDBOX Database.
    input:
    API Key - authentication
    File - Sample to test
    email - Optional - email to send alert to after processed Sample True/False
    output:
    response - JSON format of uploaded file
    '''
    #Check File is supported
    file_supported = file_check(file)
    if file_supported == False:
        print("File is not supported, Please check Documentation at: https://app.sndbox.com/docs/files")
        return False
    else:
    #Supported File must be true, Continue with the upload
        sndbox_api_url ='https://api.sndbox.com/developers/files?apikey=' + apikey
        files =  {'file':open(file,'rb')}
        email_flag = {'emailnotification':email}
        try:
            response = requests.post(url=sndbox_api_url, files=files,data=email_flag)
        except Exception as e:
            sys.exit("Error Occurred connected to the SNDBOX API - " + str(e))
        return response



def metadata(apikey,id):
    '''
    Get metadata of a submitted file from SNDBOX Database.
    input:
    apikey - authentication
    id - unique ID of the sample, found in response of submitting a sample.
    output:
    response - Metadata as JSON
    '''
    url = 'https://api.sndbox.com/developers/files/'+ id + '?apikey=' + apikey
    try:
        response = requests.get(url)
    except Exception as e:
        sys.exit("Error Occurred connecting to SNDBOX API - " + str(e))
    return response 


