#!/usr/bin/env python
"""Handles Earth Engine service account configuration."""
import ee


# The service account email address authorized by your Google contact.
# Set up a service account as described in the README.


service_account = 'drought@droughtmonitor-169009.iam.gserviceaccount.com'

private_key='C:\\Users\IAN CECIL AKOTO\source\repos\gheco-eng\GhClimHub\privatekey.json'



credentials = ee.ServiceAccountCredentials(service_account, private_key)
