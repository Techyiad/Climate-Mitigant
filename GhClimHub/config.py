import ee

import os



credentials = ee.ServiceAccountCredentials(service_account, os.path.join(os.path.dirname(os.path.realpath(__file__)),'privatekey.json'))

