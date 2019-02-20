import requests
import json

api_url="https://api.ssllabs.com/api/v3/info"

def getSSLLabsAPIStatus(apiUrl):
    api_response=requests.get(apiUrl)
    #print(type(api_response))
    apiResponse_json=api_response.json()
    #print(apiResponse_json['engineVersion'])
    if(apiResponse_json['engineVersion'])!='':
        #print('API Available!')
        return 'OK'
    else:
        #print('API Not Available !')
        return 'ERROR'

def getDomainAnalyzed(domainName):
    analyzeApiUrl="https://api.ssllabs.com/api/v3/analyze?host="+domainName
    print(analyzeApiUrl)
    apiStatus=getSSLLabsAPIStatus(api_url)
    if(apiStatus=='OK'):
        #print('OK')
        analyzeAPIRes=requests.get(analyzeApiUrl)
        analyzeAPIRes_json=analyzeAPIRes.json()
        grade=analyzeAPIRes_json['endpoints'][0]['grade']
        print(grade)


if __name__=='__main__':
    #getSSLLabsAPIStatus(api_url)
    #sample domains
    #jira.ce.wolterskluwer.io
    #www.ssllabs.com
    #bigrock.com
    #www.mediaccess.com.mx
    #nilogic.se
    getDomainAnalyzed('nilogic.se')