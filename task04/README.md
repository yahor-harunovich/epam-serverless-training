- Create and attach an identity-based policy to the `${iam_role}` role that should allow to list all buckets.
```bash
aws iam create-policy --policy-name ${policy_name} --policy-document file://iam-policy.json --profile serverless-training
```

```bash
aws iam attach-role-policy --role-name ${iam_role} --policy-arn ${policy_arn} --profile serverless-training
```

- Create a resource-based S3 bucket policy that should allow to *get* and *put* an object and also list objects of the `${s3_bucket}` bucket. The `${iam_role}` role must be allowed to perform all of these actions and only for the `${s3_bucket}` bucket, do not allow access to all principals.

```bash
aws s3api put-bucket-policy --bucket ${s3_bucket} --policy file://bucket-policy.json --profile serverless-training
```