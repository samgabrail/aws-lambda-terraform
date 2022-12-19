output "endpoint_url" {
  value = "${aws_api_gateway_stage.example.invoke_url}/${var.endpoint_path}?amount=100&fromCurrency=USD&toCurrency=CAD"
}