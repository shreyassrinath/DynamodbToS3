import json
import boto3
import time
import os
import sys

def main():
    client = boto3.client('dynamodb')
    paginator = client.get_paginator('scan') 
    lst = []
    pageNumber=0
    tblName= os.environ['tbl']
    bucketName = os.environ['bName']
    
    for page in paginator.paginate(TableName=tblName, PaginationConfig={
            'PageSize': 10
        }):       
        if 'LastEvaluatedKey' in page:
            pageNumber += 1
            print str(page['LastEvaluatedKey'])
            print "In page# ", pageNumber       
        for item in page['Items']:
            lst.append(dict(item))           
    
    fileName= "Backup_"+tblName+"_"+time.strftime("%c")
   
    f = open(fileName, 'w')
    f.write(json.dumps(lst))
    f.close()
    print "Uploading file: " + fileName
    s3Client = boto3.resource('s3')
    s3Client.meta.client.upload_file(fileName,bucketName,'DynamoDBbackups/'+tblName+'/'+ fileName)
    os.remove(fileName)

if __name__=="__main__":
    print __name__
    print os.environ['tbl']
    print os.environ['bName']     
    main()
    


