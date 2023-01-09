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

