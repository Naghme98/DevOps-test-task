# DevOps test task

### Application:
I wrote a simple Flask application that would show the Moscow time to us.
For the webserver part, I used gunicorn (the file wsgi.py is related to gunicorn)

### Docker file:
In this file first I create a new user to run the application (I didn't want to run it using root)
Then, using the requirements.txt, I would download the necessary packages.
At the end, I will run the command 

```
gunicorn --bind 0.0.0.0:8000 wsgi:app
```
using ENTRYPOINT and CMD

### Create Image and Container:

```
# make an image with tag "app:init"
docker build -t app:init .

#Create the container
docker run -p 8000:8000 app:init
```

![image](https://user-images.githubusercontent.com/45916098/211268263-1f04996f-1b8e-446c-af48-a909be00c215.png)
Figure1: Running Container

### Terraform:
I used terraform to deploy an Ubuntu 20.04 machine in AWS.
You can see the code and run, validate using the following commands:

```
#Start terraform:
terraform init

#Check:
terraform validate

#Apply the code:
terraform apply
```

![new ip-new vm](https://user-images.githubusercontent.com/45916098/211570945-24b76eab-c3b9-4d7d-849b-24d5bb9bca25.png)
Figure 2: Successful vm creation

![terraform vm created](https://user-images.githubusercontent.com/45916098/211572869-7754166a-9dad-4e99-bace-d5791e7fc767.png)
Figure 3: AWS dashbord, successful instance created

When we run the terraform, it will create a private key with name of "key.pem" in the terraform directory.
We use it to connect to the machine:

![new-success-cli-ubuntu](https://user-images.githubusercontent.com/45916098/211571253-8ff74a14-bdb9-4c53-9f63-45a4d28cb3c9.png)
Figure 4: Connecting to the created machine

### Ansible:
To configure the created machine and upload, build, run the container of our application, we will use Ansible.
Use can see each specific category tasks have their directory (app for deploying the application, docker for installing docker, configuration for changing the hostname, apt for installing packages.

You can see the ansible directory structure:

![image](https://user-images.githubusercontent.com/45916098/211571824-7b931d16-683b-4324-ba3e-819e17bd50cf.png)

Figure 5: Ansible directory structure

```
#check the syntax:
ansible-lint playbook.yml

#run ansible playbooks:
ansible-playbook -i ./inventory/ playbook.yml
```
Because I used inventory and inside it defined my hosts, I had to run the play the ansible-playbook like that.

![working](https://user-images.githubusercontent.com/45916098/211573067-d0f2f8a4-13d6-46ad-8025-8b817287ab99.png)

![mysite](https://user-images.githubusercontent.com/45916098/211573109-18cd8d65-a83b-4af2-8595-9293344eed01.png)

public IP of the machine if you need to try it: 18.159.3.248
