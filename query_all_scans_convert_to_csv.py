# Documentation: 
# https://docs.nowsecure.com/api/auto/graphql/
# https://lab-api.nowsecure.com/graphql (click on Schema on the right and search for all available details that can be retrieved via GraphQL )

import requests
import json 
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://api.nowsecure.com/graphql'

query = """
{
  auto{
    applications{
      ref # -> same as id
      packageKey # -> same as package
      platform
      analysisConfigLevel
      # group {
      #   ref
      #   name
      # }
      assessments {
        ref
        # taskId
        createdAt
        build {
          digest
          version
          # uploadedAt
        }
        # report {
        #   score
        #   findings {
        #     impactType
        #     check {
        #       issue { 
        #         title
        #         description
        #         cvss
        #         cvssVector
        #       } 
        #     }
        #   } 
        # }
      }
      
      createdAt
    }
  }
}
"""

f=open('.apikey','r')
apikey=f.read()
f.close

headers = { 
  "Host": "api.nowsecure.com",
  "Origin": "https://api.nowsecure.com",
  "Connection": "keep-alive",
  "Accept-Encoding": "gzip, deflate, br",
  "Content-Type": "application/json",
  "Accept": "application/json",
  "DNT": "1",
  "Authorization": "Bearer "+str(apikey)
}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(url, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


result = run_query(query) # Execute the query

f=open('result.json','w') # Write JSON into result.json
f.write(json.dumps(result))
f.close()

# print(json.dumps(result)) # print to the console 


# convert into csv
openfile=open('result.json')  
jsondata=json.load(openfile)
df = pd.json_normalize(   jsondata['data']['auto']['applications'], 
                            # 'applications',
                            'assessments',
                            ['createdAt', 'ref', 'packageKey', 'platform', 'analysisConfigLevel'], 
                            errors='ignore',
                            record_prefix="_"
                        )
                        
df.columns = [  'Assessment_reference', 
                'Assessment_createdAt', 
                'App_build_digest',
                'App_build_version',
                'build',
                'Application_createdAt',
                'Application_reference',
                'package_key',
                'Platform',
                'AnalysisConfigLevel']

df.to_csv (r'result.csv', index = None)

openfile.close()
print(df)
