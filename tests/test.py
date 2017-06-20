import api_client

client = api_client.ApiClient()

api = "market-data"
params = { 
    'securityId': 'NSE:7UP',
    'date': '20170320'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "market-data-eod"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "company-financials"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "company-returns"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "company-movaverage"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "company-technicals"
params = { 
    'securityId': 'NSE:NNFM',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "currency-rate"
params = { 
    'curr_code': 'TND',
    'base_curr': 'USD',
    'startDate': '2017-02-01',
    'endDate': '2017-03-20'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "currency"
params = { 
    'country_name': 'Tunisia'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()

api = "company"
params = { 
    'securityId': 'NSE:7UP'
}
api_key = 'CCSnPZGQES4RkFmZAV4ll3IYEvhscycG1tnBjvh9'
print api
print client.get(api_key, api, params).data_frame()