From python:3.12-rc-slim

RUN groupadd --gid 1000 app && \
    useradd --create-home --gid 1000 --uid 1000 app

RUN mkdir -p /home/app/src

WORKDIR /home/app/src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#Copy project file
COPY ./ /home/app/src

USER app

ENTRYPOINT ["gunicorn"]
EXPOSE 5000
CMD ["--bind 0.0.0.0", "wsgi:app"]
