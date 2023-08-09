# API-Lambda-Calc

Welcome to the API-Lambda-Calc repository! This project demonstrates how to create a simple calculator web app using AWS Lambda, API Gateway, and HTML. With this setup, you can perform basic mathematical operations through a REST API and visualize the results using a user-friendly HTML interface.

## Prerequisites

Before you begin, make sure you have the following:

- An AWS account with IAM permissions to create Lambda functions and API Gateway.
- AWS CLI installed and configured with your credentials.
- Basic understanding of AWS Lambda, API Gateway, and HTML.

## Getting Started

Follow these steps to set up and use the API-Lambda-Calc:

1. **Lambda Function**: Create a Lambda Function that generates basic calculator computations. This function should accept an operation and operands, perform the calculation, and return the result.

2. **API Gateway**: Utilize API Gateway to create a REST API that integrates with the Lambda function. API Gateway enables communication with the calculator application in Lambda.

3. **Test the API**: Use a web browser to test the API by passing various values. This can help ensure that the API and Lambda function are functioning correctly.

4. **Build the HTML Calculator**: Construct an HTML page (`calculator.html`) using JavaScript to invoke the API URL dynamically. The HTML page should provide an input mechanism for numbers and operations and display the calculation results.

## Usage

Follow these steps to use the API-Lambda-Calc:

1. Open `calculator.html` in a web browser.
2. Input the numbers and select the desired operation.
3. Click the "Calculate" button to send a request to the AWS Lambda function via the API Gateway.
4. The calculation result will be displayed on the webpage.

## Contributing

Contributions are welcome! If you'd like to enhance this project or fix any issues, please submit a pull request.

## License

This project belongs to cloudtechtr.click
