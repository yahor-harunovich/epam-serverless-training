**The goal of this task is** to encrypt the contents of the S3 bucket utilizing an automatically created in your account KMS key and try to add a new object to the encrypted bucket.

In this task, you should work with the following resources:

- a `${iam_role}` role - the role has already full access to IAM and S3 services. You have to simulate all your actions using Policy Simulator under this role!
- `${s3_bucket_1}` and `${s3_bucket_2}` S3 buckets - the first one has one object inside, which in this task you have to copy to the second bucket
- a KMS key `${kms_key_arn}` - this key is created automatically in your account. It will be set to "Pending deletion" status when you will finish this task and it will be deleted from your account after MINIMUM deletion period - 7 days. Keep in mind that it is allowed to use only this key for encryption of objects in the second bucket, encryption of objects and the bucket itself with other keys is prohibited

In three moves, you must:

1. Grant all the necessary permissions for the `${iam_role}` role to work with the key. Do not grant full administrator access!

```bash
aws iam create-policy --policy-name ${kms_policy_name} --policy-document file://kms-policy.json --profile serverless-training
```


```bash
aws iam attach-role-policy --role-name ${iam_role} --policy-arn ${kms_policy_arn} --profile serverless-training
```

1. Enable for the `${s3_bucket_2}` bucket server-side encryption using the your AWS KMS key with the `${kms_key_arn}` ARN.

```bash
aws s3api put-bucket-encryption --bucket ${s3_bucket_2} --server-side-encryption-configuration file://encryption-config.json --profile serverless-training
```


1. Check whether you can put a new encrypted object to the encrypted bucket. To do this, you have to copy a *confidential_credentials.csv* file from `${s3_bucket_1}` bucket to `${s3_bucket_2}`. As a result, the copied file *confidential_credentials.csv* should be encrypted.

```bash
aws s3 cp s3://${s3_bucket_1}/confidential_credentials.csv s3://${s3_bucket_2}/ --profile serverless-training
```