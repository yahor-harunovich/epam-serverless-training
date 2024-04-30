**The goal of this task is** to set up S3 bucket notifications to SQS queue when adding a file to certain (in our case input/) folder, which triggers Lambda function to handle that file and put the processed result into S3 output directory.

You have:

- S3 bucket `${bucket_name}` - this bucket contains /input folder to upload files into.
- SQS queue `${queue_name}` - the sqs queue which needs to be connected as notification destination for S3 and should be as eventsource for Lambda.
- Lambda Function `${lambda_function}` - Lambda function that will poll for messages as they arrive in the SQS queue after S3 uploads, transform files and store processed file to S3 /output directory.

All necessary permissions and policies were already set.

In three moves, you must:

1. In S3 create event notification with prefix /input for all object create events and `${queue_name}` SQS as destination to publish the events.

```bash
aws s3api put-bucket-notification-configuration \
    --bucket ${s3_bucket_name} \
    --notification-configuration file://notification-config.json \
    --profile serverless-training
```

2. In SQS configure Lambda function trigger to execute function each time messages arrive to queue. Wait for the trigger to be created.

```bash
aws lambda create-event-source-mapping \
    --function-name ${lambda_function_name} \
    --event-source-arn ${sqs_queue_arn} \
    --profile serverless-training
```

3. Upload any .txt file into the /input S3 bucket folder.

```bash
aws s3 cp ./test.txt s3://${s3_bucket_name}input/test.txt --profile serverless-training
```