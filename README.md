# Government Demand Management Form

This project involves a web form developed with Flask that allows government users to register demands against individuals, including details such as the reason for the demand, name, ID number, year of birth, and file number. The data entered into the form is stored in an AWS DynamoDB database.

A data pipeline is implemented using AWS services. A DynamoDB stream feeds data into an SQS queue. From there, a Lambda function is triggered to transform the data and then store it in an Amazon S3 bucket.

Finally, the data stored in S3 can be queried using Amazon Athena for analysis and report generation.

The entire system is deployed and running on an AWS EC2 instance, providing a robust and scalable platform for efficient demand management and data analysis.

## AWS Architecture
![Pipeline](https://drive.google.com/file/d/1hNWFNH2omQjXzoE02unu2_EuqSF3DZQb/view?usp=sharing)


## End
You can find me on [LinkedIn](https://www.linkedin.com/in/t4y-del/).
