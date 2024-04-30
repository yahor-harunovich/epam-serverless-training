**The goal of this task is** to integrate API Gateway with a Lambda function.

At the beginning of this task, the following infrastructure is prepared for you, which includes:

- API Gateway *`${api_gateway}`*
- Route ID *`${route_id}`*
- Lambda function *`${lambda_function_name}`*

In this task, you should:

- Integrate API Gateway with a lambda function *`${lambda_function_name}`* using existing route
    
    ```bash
    aws apigatewayv2 update-route \
     --api-id ${api_gateway_id} \
     --route-id ${route_id} \
     --route-key "GET /contacts" \
     --profile serverless-training
    ```
    
    ```bash
    aws lambda add-permission \
     --statement-id 236c85f1-67e3-5e3d-b36e-aa2f3ea39165 \
     --action lambda:InvokeFunction \
     --function-name "${function_name}" \
     --principal apigateway.amazonaws.com \
     --source-arn "${route_arn}" \
     --profile serverless-training
    ```
    
- Configure *`${lambda_function_name}`* to return via *`GET /contacts`* a list of contacts:
    
    ```bash
    zip function.zip handler.py
    ```
    
    ```bash
    aws lambda update-function-code \
     --function-name ${function_name} \
     --zip-file fileb://function.zip \
     --profile serverless-training
    ```