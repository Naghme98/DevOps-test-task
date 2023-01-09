From python:3.12.0a3-slim

RUN groupadd --gid 1000 && \
    useradd --create-home --gid 1000 --uid 1000 app

RUN mkdir -p /home/app/src

WORKDIR /home/app/src

COPY ./ requirements.txt
RUN pip3 install -r requirements.txt

USER app

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]
