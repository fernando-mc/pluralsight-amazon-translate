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
