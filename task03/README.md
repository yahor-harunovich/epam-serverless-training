- Grant full access to Amazon S3 service for the `${iam_role}` role. **Please use existing AWS policy and not create your own.**

```bash
aws iam attach-role-policy --role-name ${iam_role} --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --profile serverless-training
```

- Update the resource-based S3 bucket policy, which as a result should prohibit the deletion of any objects inside the `${s3_bucket} S3` bucket only for the `${iam_role}` role.

```bash
aws s3api put-bucket-policy --bucket ${s3_bucket} --policy file://bucket-policy.json --profile serverless-training
```