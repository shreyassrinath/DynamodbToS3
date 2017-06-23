FROM python:2
ADD ./config/.aws/credentials /root/.aws/credentials
ADD . /exportDDB 
WORKDIR /exportDDB
RUN pip install -r requirements.txt
ARG ddbTable
ENV tbl $ddbTable
ARG s3Bucket
ENV bName $s3Bucket 
ENTRYPOINT ["python", "src/exportDynamoDbData.py"]
