# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import io
import logging
import json
import docx
from SiteCredabilty import Infer
from wordAPI import get_urls
# from fdk import response
# creating a Flask app
app = Flask(__name__)

@app.route("/test", methods = ['GET'])
def test():
    return "hello world!"

@app.route("/putFile", methods = ['PUT'])
def putFile():
    print("dsfsf")
    # logging.basicConfig(filename="/home/odedharshe/rest-server/rest-server-func/neweile.log",format='%(asctime)s %(message)s',filemode='w')

    # # Creating an object
    # logger = logging.getLogger()

    # # Setting the threshold of logger to DEBUG
    # logger.setLevel(logging.DEBUG)
    # Getting the docx from the HTTP request
    try:
        docx_file = io.BytesIO(request.data)
        doc = docx.Document(docx_file)
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing byteArry payload: ' + str(ex))
    url_list = get_urls(doc)
    
    # Getting the score for each URL
    output = []
    #url_list = ["https://www.msn.com/he-il/entertainment/other/%D7%9B%D7%95%D7%9B%D7%91%D7%AA-%D7%97%D7%AA%D7%95%D7%A0%D7%9E%D7%99-%D7%A2%D7%95%D7%96%D7%91%D7%AA-%D7%96%D7%94-%D7%94%D7%96%D7%9E%D7%9F-%D7%9C%D7%A7%D7%95%D7%9D-%D7%95%D7%9C%D7%9C%D7%9B%D7%AA/ar-AA1fEig0?ocid=msedgntp&cvid=38ad764eab264f989d19cc78785f81e6&ei=9", "https://he.wikipedia.org/wiki/%D7%A1%D7%99%D7%99%D7%91%D7%A8"]
    # logger.debug("before")

    for url in url_list:
        try:
            score = Infer(url)
            print(url)
            print(score)
            output.append({"link": url, "score": str(score)})
        except (Exception, ValueError) as ex:
            output.append({"link": url, "score": "75.0"})
        # logger.debug(url)
    print("done")
    # logger.debug("after")

    return json.dumps(output)


@app.route("/putUrl", methods = ['PUT'])
def putUrl():
    output = ""
    url = str(request.data)
    try:
        score = Infer(url)
        print(url)
        print(score)
        output = str(score) 
    except (Exception, ValueError) as ex:
        output = "75.0"
    return output

# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug = True)

