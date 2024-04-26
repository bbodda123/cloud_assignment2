FROM python:3.9

WORKDIR /app


COPY . /app


RUN pip install nltk

RUN python -m nltk.downloader stopwords webtext punkt

RUN pip install --no-cache-dir nltk

CMD ["python", "cloud.py"]
