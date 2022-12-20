# Overview
An example to use Terraform to create an AWS Lambda function with an API gateway.

## Instructions

1. Create a `requirements.txt` file from pipenv

```bash
pipenv requirements > requirements.txt
```

2. Install the requests library to a new package directory.

```bash
pip install --target ./infrastructure/package -r requirements.txt
```

3. Create a deployment package with the installed library at the root.

```bash
cd infrastructure/package
zip -r ../my-deployment-package.zip .
```

4. Add the `main.py` file to the root of the zip file.

```bash
cd ..
zip my-deployment-package.zip ../main.py
```

5. Export your AWS Environment variables.

```bash
export AWS_ACCESS_KEY_ID=put_your_key_here
export AWS_SECRET_ACCESS_KEY=put_your_secret_here
```

6. Initialize Terraform

Make sure you're inside the infrastructure folder.

```bash
terraform init
```

7. Populate the AccountId Variable

In the file `terraform.tfvars`, put in your account ID. You can find it by clicking in the top right corner of the AWS console.

8. Plan Terraform

```bash
terraform plan
```

9. Apply Terraform

```bash
terraform apply
```

10. Go to the URL output of Terraform

The default query has ?amount=100&fromCurrency=USD&toCurrency=CAD

Change the amount and from and to currency to see different conversions.

11. Clean up

```bash
terraform destroy
```