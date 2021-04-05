input("Please copy your AWS key pair file to the directory this script is in before proceeding further. \nPress enter to continue")

kp_name = input("Please enter the name of AWS key pair file: ")
num_ip = int(input("Number of Instances for which to enable passwordless ssh: "))

ips = []

for i in range(num_ip):
    ip = input("Please enter IP #%s: " % (str(i+1)))
    ips.append(ip)

pub = input("Please enter the contents of your authentication public key (in ~/.ssh/): ")

to_write = []
to_write.append('#!/bin/bash\n\n')

for i in range(num_ip):
    ip = ips[i]
    to_write.append("ssh -i %s ec2-user@%s 'echo \"%s\" >> ~/.ssh/authorized_keys'\n" % (kp_name, ip, pub))
    to_write.append("ssh -i %s ec2-user@%s 'sudo chmod -R 700 ~/.ssh'\n" % (kp_name, ip))
    to_write.append("ssh -i %s ec2-user@%s 'sudo chmod 600 ~/.ssh/*'\n\n" % (kp_name, ip))

with open("deploy.sh", "w") as f:
    f.writelines(to_write)
