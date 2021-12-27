import requests
from mlmodel import checkApiKey



#
# This function will pass your image to the machine learning model
# and return the top result with the highest confidence
#
#  key - API key - the secret code for your ML project 
#  imagedata - base64-encoded data for image you want to classify
#
def classifyImage(key, imagedata):
  checkApiKey(key)

  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/classify")

  response = requests.post(url, json={ "data" : imagedata })

  if response.ok:
    responseData = response.json()
    topMatch = responseData[0]
    return topMatch
  else:
    errorData = response.json()
    print (errorData)
    response.raise_for_status()


#
# This function will store your image in one of the training
# buckets in your machine learning project
#
#  key - API key - the secret code for your ML project 
#  imagedata - base64-encoded data to store as a training example
#  label - the training bucket to put the image into
#
def storeImage(key, imagedata, label):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/train")

  response = requests.post(url, 
                           json={ 
                             "data" : imagedata, 
                             "label" : label 
                           })

  if response.ok == False:
    # if something went wrong, display the error
    print (response.json())
