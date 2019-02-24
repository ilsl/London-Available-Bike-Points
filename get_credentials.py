import os
from google.cloud import storage

# Get the default bucket for my Google python project # tfl_bike
def get(self):
  bucket_name = os.environ.get('tfl_bike', app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')

def read_file(filename):

    client = storage.Client.from_service_account_json("isobel-service-account-key.json")
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket('tfl_bike')
    # Then do other things...
    blob = bucket.get_blob(filename)
    return blob.download_as_string()  # read content from bucket and print to stdout
