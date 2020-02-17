from selenium import webdriver
import time
import requests
import json


mfApiUrl='https://www.mfapi.in/'

# this function would get the API end point URL after getting the fund name as user input
def gfetmfApiEndPoint(fundname):
    print('Fund Name {0} - '.format(fundname))
    chrome_driver=webdriver.Chrome()
    chrome_driver.get(mfApiUrl)
    searchBox=chrome_driver.find_element_by_xpath('//*[@id="mfsearch"]').send_keys(fundname)
 
    time.sleep(2)
    fundNames=chrome_driver.find_elements_by_xpath('//*[@id="ui-id-1"]/li')
    for name in fundNames:
        if name.text==fundname:
            name.click()
    
    time.sleep(2)
    endPointUrl=chrome_driver.find_element_by_xpath('//*[@id="intro"]/ul/li/a')
    apiurl=endPointUrl.text
    #print(apiurl)
    chrome_driver.close()
    if len(apiurl)>0:
        return(apiurl)
    else:
        print('No valid fund found !')
#function to invoke the MF API end point to get the data about how fund has been performing
def getFundPerfData(api_url,numdays):
    api_response=requests.get(api_url)
    #print(api_response)
    if api_response.status_code==200:
        api_res_json=api_response.json()
        #print(api_res_json)
        #i=1
        #while i<180:
            #print(api_res_json['data'][i])
        #    i=i+1

        start_date_value=api_res_json['data'][numdays]['nav']    
        end_date_vaklue=api_res_json['data'][1]['nav']
        diff=float(end_date_vaklue)-float(start_date_value)
        perc_diff=diff / float(start_date_value) * 100.0
        print('Last {0} days performance data - '.format(numdays))
        print('Growth in value -{0} - '.format(diff))
        print('Growth in percentage -{0} - '.format(perc_diff))
  
if __name__=='__main__':
    search_text=input('Which Mutual fund you are looking for? : ')
    numdays=int(input('Last how many days you want to see data for?: '))
    #finalUrl=gfetmfApiEndPoint('HDFC Top 100 Fund - Growth Option')
    #Axis Focused 25 Fund - Growth Option
    #Mirae Asset Emerging Bluechip Fund - Direct Plan - Growth
    #Mirae Asset Emerging Bluechip Fund - Regular Plan - Growth Option
    if len(search_text)>0:
        finalAPIUrl=gfetmfApiEndPoint(search_text)
        
        #invoke the API end point
        getFundPerfData(finalAPIUrl,numdays)
    else:
        print('Please enter a valid mutual fund name.')    
    
