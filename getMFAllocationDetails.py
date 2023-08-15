import requests
import pandas as pd
import time

headers = {
    'Accept': 'application/json, text/plain, */*',
    'accept-version': '7.0.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
}
 
my_mutual_funds_code={'M_QUNB','M_CANY','M_MIAL','M_MISM','M_AXFO','M_AXLO','M_SBTY','M_NIMS','M_AXMC','M_ICCSF','M_SBFQ','M_ICIDX','M_MOI2','M_FREK','M_HDCGO','M_HDFSU','M_KOSM','M_HDCBA'}
test_list={'M_QUNB','M_MISM', 'M_MIAL'}
#Method to get current allocation details of a mutual fund.Input - Mutual Fund code which is Tickertape specific, expample Quant Absolute Fund - M_QUNB
#print(response_json['data']['currentAllocation'][0]['title'])

def getAllCurrentAllocations(mfcode):

    try:
        #API url example - 'https://api.tickertape.in/mutualfunds/M_QUNB/holdings'
        api_url='https://api.tickertape.in/mutualfunds/{}/holdings'.format(mfcode)
        print(api_url)
        response = requests.get(api_url, headers=headers)
        
        if response.status_code==200:
            response_json=response.json()
        else:
            print('Tickertape API did not responded with 200 !')    
    except Exception as e:
        print(e)

    allocations=response_json['data']['currentAllocation']
    #print(allocations)
    allocations=response_json['data']['currentAllocation']
    master_list=[]

    for item in allocations:

        itemdetails={}
        itemdetails['type']=item['type']
        itemdetails['title']=item['title']
        itemdetails['allocation']=item['latest']
        master_list.append(itemdetails)

    data=pd.DataFrame(master_list)
    #print(data)
    return(data)

   
if __name__=='__main__':
    #getAllCurrentAllocations('M_CANY')
    for mf in my_mutual_funds_code:
        mfdata=getAllCurrentAllocations(mf)
        #with pd.ExcelWriter('MFHoldingInfo.xlsx') as writer:
        with pd.ExcelWriter('MFHoldings/'+mf+'_holdings.xlsx') as writer:
            mfdata.to_excel(writer,sheet_name=mf,engine='openpyxl',index=False)
            #writer.close()
        time.sleep(2)





