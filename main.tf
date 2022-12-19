terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.47.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda"
  runtime = "python3.8"
  role = "${aws_iam_role.lambda_role.arn}"
  handler = "handler.lambda_handler"
  source_code_hash = "${base64sha256(file("lambda_function.zip"))}"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_api_gateway_rest_api" "example_api" {
  name = "example_api"
}

resource "aws_api_gateway_resource" "example_resource" {
  rest_api_id = "${aws_api_gateway_rest_api.example_api.id}"
  parent_id = "${aws_api_gateway_rest_api.example_api.root_resource_id}"
  path_part = "example"
}

resource "aws_api_gateway_method" "example_method" {
  rest_api_id = "${aws_api_gateway_rest_api.example_api.id}"
  resource_id = "${aws_api_gateway_resource.example_resource.id}"
  http_method = "GET"
  authorization = "NONE"

  request_parameters = {
    "method.request.header.Content-Type" = true
  }

  integration {
    type = "AWS_PROXY"
    uri = "${aws_lambda_function.example_lambda.invoke_arn}"
    integration_http_method = "POST"
  }
}
