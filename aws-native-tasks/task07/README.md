In this task, you should work with the following resources:

- a Lambda function `${lambda_function}` - this function returns a list of Lambda functions in AWS account. Function has an execution role `${iam_role}` and a resource-based policy. This function is used for the backend of HTTP API.
- a Lambda function's execution role `${iam_role}`
- API Gateway `${apigatewayv2_api}` - an HTTP API that integrated with the `${lambda_function}` function

In two moves, you must:

1. Grant the correct permissions to the Lambda function so that it can access the resources it needs based on the function code. Use AWS managed policy that grants access to Lambda API actions and follow the principle of least privilege. **Please use existing AWS policy and not create your own.**

```bash
aws iam attach-role-policy \
 --role-name ${iam_role} \
 --policy-arn arn:aws:iam::aws:policy/AWSLambda_ReadOnlyAccess \
 --profile serverless-training
```

2. Grant the correct permissions to the Lambda function so that HTTP API could invoke it.

```bash
aws lambda add-permission \
 --statement-id 505a5da3-178f-516b-85d4-b44afe837166 \
 --action lambda:InvokeFunction \
 --function-name ${lambda_function_arn} \
 --principal apigateway.amazonaws.com \
 --source-arn "arn:aws:execute-api:eu-central-1:905418349556:f90pz4acdf/*/*/get_list" \
 --profile serverless-training
```