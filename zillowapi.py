# import sys
# print '\n'.join(sys.path)

# import pyzillow

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
address = '61 Riverside Ave APT 1B'
zipcode = '06905'

zillow_data = ZillowWrapper('X1-ZWz19of44d37d7_3xvfc')
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)
print result.zillow_id 