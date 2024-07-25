resource "aws_instance" "my_ec2_instance" {
  ami           = "ami-04a81a99f5ec58529"
  instance_type = "t2.micro"
}
