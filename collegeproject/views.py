from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
# import openai, os
# from dotenv import load_dotenv
# load_dotenv()
# api_key = "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"
# openai.api_key = api_key

# # Create your views here.

# # def empty(request):
# #     return render( request, "searchpage.html")

# def empty(request):
#     print(api_key)
#     if api_key is not None and request.method == "POST":
#         userinput = request.POST.get('user_input')
#         print(userinput)
#         response = openai.Image.create(
#             prompt = userinput,
#             size = '256x256'
#         )
#         print(response)
#     return render( request, "searchpage.html")

import os
import openai
import time
import base64
import json
import requests
from PIL import Image
from io import BytesIO


def generate(request):
    if request.method == "POST":
        title = request.POST['user_input']
    print("generating the image")
    openai.api_key = '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'  # your api key
    openai.Model.list()
    response = openai.Image.create(
    prompt=title,
    n=1,
    size="1024x1024",
    # response_format="b64_json",
    response_format = "url"
            )
    # image_url = response['data'][0]['b64_json'][:50]
    # print(image_url)
    image_url = response['data'][0]["url"]
    print(image_url)
    # code for the downloading part
    # response_download = openai.Image.create(
    # prompt=title,
    # n=1,
    # size="1024x1024",
    # response_format="b64_json",
    # )
    
    # for i in range(0, len(response_download['data'])):
    #     b64 = response_download['data'][i]['b64_json']
    # # filename = f'image_{int(time.time())}_{i}.png'
    #     filename = 'image.png'
    #     print('Saving file ' + filename)
    #     with open(filename, 'wb') as f:
    #         f.write(base64.urlsafe_b64decode(b64))

    return render(request, "searchpage.html", {
        'image_data': image_url,
        "prompt" : title
    })




def empty(request):
    return render(request, "searchpage.html")


def content(request):
    if request.method == "POST":
        url = request.POST["url"]
        content = request.POST['text_input']
        prompt = request.POST["prompt"]
        print(prompt)
    openai.api_key = "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"
    n=0
    print(url)
    while n<1:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= content,
        temperature=0.7,
        max_tokens=2560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        n=n+1
    #with open('prompt.txt','w') as f:
     #   f.writelines(response['choices'][0]['text'])
    words = response['choices'][0]['text'].split()
    with open('prompt.txt', 'w') as f:
      for i in range(0, len(words), 10):
            f.write(" ".join(words[i:i+10]))
            f.write("\n")
            
    return render(request,"searchpage.html",{
        "caption" : ' '.join(words),
        "image_data": url,
        "prompt" : prompt
    })

   
    



    

# while len(image_url) % 4 != 0:
#         image_url += "="
#     image_data = base64.b64decode(image_url)
#     print("image data is",image_data)