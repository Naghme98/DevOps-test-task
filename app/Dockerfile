From python:3.12-rc-slim

RUN groupadd --gid 1000 app && \
    useradd --create-home --gid 1000 --uid 1000 app

RUN mkdir -p /home/app/src

WORKDIR /home/app/src

#Copy project file
COPY ./ /home/app/src

RUN pip3 install -r requirements.txt

USER app

ENTRYPOINT ["gunicorn"]

EXPOSE 8000

CMD ["--bind", "0.0.0.0:8000", "wsgi:app"]
