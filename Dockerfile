FROM python:3

WORKDIR /src

ADD main.py data/db.json requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /src/Test
ADD Test/Test.py Test
RUN rm requirements.txt

CMD ["hug", "-p 8000", "-f", "main.py" ]
EXPOSE 8000
