# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY requirements.txt /docker-test/requirements.txt

# switch working directory
WORKDIR /docker-test

# upgraded pip
RUN pip install --upgrade pip

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /docker-test

# expose the port
EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["run.py"]