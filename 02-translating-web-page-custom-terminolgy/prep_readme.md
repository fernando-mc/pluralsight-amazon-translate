## Steps to prepare your Python environment

- [Install Python3](https://www.python.org/downloads/)
- [Install Boto3](https://pypi.org/project/boto3/)
- [Install BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

Then you can run a few commands in the same directory as this code. The directory is `02-translating-web-page-custom-terminolgy` 

### For Linux/Mac

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install beautifulsoup4 boto3
```

### For Windows cmd.exe (Not powershell)

```
python3 -m venv venv
venv\Scripts\activate.bat
pip install beautifulsoup4 boto3 
```

### Installing the AWS CLI

```bash 
pip install awscli
```

### Adding the custom terminology with Python and Boto3

```python
import boto3

translate = boto3.client('translate')

with open('./customterminology.csv', 'rb') as ct_file:
    translate.import_terminology(
        Name='NewCloudFree',
        MergeStrategy='OVERWRITE',
        Description='Terminology for CloudFree custom plans',
        TerminologyData={
            'File': ct_file.read(),
            'Format': 'CSV'
        }
    )

```
