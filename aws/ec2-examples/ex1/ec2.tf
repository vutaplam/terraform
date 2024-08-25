resource "aws_instance" "web-server1" {
ami = "ami-0ae8f15ae66fe8cda"
instance_type = "t2.micro"
}

provider "aws" {
region = "us-east-1"
}
