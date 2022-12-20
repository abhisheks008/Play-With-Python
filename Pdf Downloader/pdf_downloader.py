# python program to download pdf from url

import requests

# enter the url containing the .pdf extension
url='https://www.thh.nhs.uk/documents/_Departments/Research/InfoSheets/16_sampling_research.pdf'
r = requests.get(url, stream=True)

# paste the path where you want your file to be downloaded (eg:C/download/myfile.pdf)
# "<filename>.pdf" must be included in the path for creating and saving the file.
with open('<pathname>/myfile.pdf', 'wb') as f:
    f.write(r.content)
