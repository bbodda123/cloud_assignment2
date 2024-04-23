# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install NLTK
RUN pip install nltk
# Download NLTK data
RUN python -m nltk.downloader stopwords webtext punkt
RUN pip install --no-cache-dir nltk


# Run script.py when the container launches
CMD ["python", "cloud.py"]
