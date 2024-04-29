**The goal of this task is** to configure role chaining using two roles so that one dedicated role for role assuming could assume another role that has read-only access.

In this task, you have two roles:

- *`${assume_role}`* role - should be assumed by any user in your AWS account
- *`${readonly_role}`* role - should be assumed only by the *`${assume_role}`* role

- Configure proper permissions for the *`${assume_role}`* role, in order to assume the *`${readonly_role}`* role. Do not grant full administrator access!

```bash
aws iam update-assume-role-policy --role-name ${assume_role} --policy-document file://trust-policy-assume-role.json --profile serverless-training
```

- Grant full read-only access for the *`${readonly_role}`* role. **Please use existing AWS policy and not create your own.**

```bash
aws iam attach-role-policy --role-name ${readonly_role} --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --profile serverless-training
```

- Configure correct trust policy for the *`${readonly_role}`* role.

```bash
aws iam update-assume-role-policy --role-name ${readonly_role} --policy-document file://trust-policy-readonly-role.json --profile serverless-training
```
