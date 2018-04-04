import ee

import os

service_account = 'ghclimhub@appspot.gserviceaccount.com'

credentials = ee.ServiceAccountCredentials(service_account, os.path.join(os.path.dirname(os.path.realpath(__file__)),'privatekey.json'))

