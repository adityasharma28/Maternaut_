import requests
from bs4 import BeautifulSoup
import json

def get_babysitters(city): 
    # if(city=="null"):

    url='https://www.justdial.com/' + city + '/search?q=Baby-Sitters'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    name1=[]
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    name = soup.findAll("span",{'class':'lng_cont_name'})
    n1=[]
    for i in range(len(name)):
        n={}
        n['lng_cont_name']=name[i].text
        name1.append(n)

    babysitters = []
    sp=soup.findAll(attrs={"class" : "cntanr"})

    for i in range(len(name1)):
        babysitter = {}
        n1=name1[i]
        op=sp[i]["data-href"]
        babysitter['name'] = n1
        babysitter['link'] = op
        babysitters.append(babysitter) 

    babysitters = json.dumps(babysitters)    

    return babysitters

