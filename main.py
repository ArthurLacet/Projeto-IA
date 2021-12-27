from mlimages import classifyImage
from imagedata import getDataFromUrl
from mlmodel import checkModel
import os
import subprocess
from urllib.request import urlretrieve

while True:
  imageurl=input("Digite o endereço da imagem desejada: ")

  def downloadMS(link):
    ms=len([iq for iq in os.scandir("MEMBROS_SUPERIORES")])
    urlretrieve(f"{link}",f"MEMBROS_SUPERIORES/RAIO X {ms}.jpg")
  def downloadMI(link):
    mi=len([iq for iq in os.scandir("MEMBROS_INFERIORES")])
    urlretrieve(f"{link}",f"MEMBROS_INFERIORES/RAIO X {mi}.jpg")
  def downloadT(link):
    t=len([iq for iq in os.scandir("TRONCO")])
    urlretrieve(f"{link}",f"TRONCO/RAIO X {t}.jpg")
  def downloadC(link):
    c=len([iq for iq in os.scandir("CABECA")])
    urlretrieve(f"{link}",f"CABECA/RAIO X {c}.jpg")
  API_KEY="9e53b8f0-2368-11eb-afad-7733c7a0ca677d5a9730-6301-4a37-a08a-1a363fcee18c"


  # -------------------------------------------------------
  # CHECK IF THE MACHINE LEARNING MODEL IS READY TO USE
  # -------------------------------------------------------

  # you can use this to check if your machine learning model
  # has finished training 

  status = checkModel(API_KEY)
  print (status)




  # -------------------------------------------------------
  # USE YOUR MACHINE LEARNING MODEL TO RECOGNIZE IMAGES 
  # -------------------------------------------------------

  # CHANGE THIS to an image that you want your 
  # machine learning model to classify

  test_data = getDataFromUrl(imageurl)
  demo = classifyImage(API_KEY, test_data)

  label = demo["class_name"]
  confidence = demo["confidence"]

  if confidence >= 80:
    print("resultado: '%s' com %d%% de confiança" % (label, confidence))
    if label=="CABECA":
      try:
        os.mkdir("CABECA")
        downloadC(imageurl)
      except:
        downloadC(imageurl)

    elif label=="TRONCO":
      try:
        os.mkdir("TRONCO")
        downloadT(imageurl)

      except:
          downloadT(imageurl)

    elif label=="MEMBROS_SUPERIORES":
      try:
        os.mkdir("MEMBROS_SUPERIORES")
        downloadMS(imageurl)
      except:
        downloadMS(imageurl)
    elif label=="MEMBROS_INFERIORES":
      try:
        os.mkdir("MEMBROS_INFERIORES")
        downloadMI(imageurl)
      except:
        downloadMI(imageurl)
    continuacao = input('QUER CONTINUAR? [S/N]').strip().upper()
    if continuacao[0]=='N':
      print("OBRIGADO! VOLTE SEMPRE!")
      break
  elif confidence < 80:
    print("Desculpe, não foi possível classificar a imagem solicitada. Por favor, tente novamente!")
    continuacao = input('QUER CONTINUAR? [S/N]').strip().upper()
    if continuacao[0]=='N':
      print("OBRIGADO! VOLTE SEMPRE!")
      break