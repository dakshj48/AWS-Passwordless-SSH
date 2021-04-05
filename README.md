# AWS-Passwordless-SSH
Script to enable passwordless SSH on AWS EC2 servers

### Requirements:
- Python 3
- IPs of the AWS instances.
- AWS key pair used to start the AWS instances needed in the root directory of the script.
- Configure the source and destination values in inbound and outbound rules of the security group of the instances to `Anywhere`.

### Instructions:
Please use the command `bash run.sh` to start the setup process.

`run.sh` will use the python script `setup.py` to take user inputs and then configure and create a `deploy.sh` script which will then be used to enable passworless SSH on the given AWS instances.
