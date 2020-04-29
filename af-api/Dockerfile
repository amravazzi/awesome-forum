FROM python:3.6

# Create app directory
WORKDIR /srv/app

# Copy Pipefiles
COPY Pipfile ./
COPY Pipfile.lock ./
COPY requirements.txt ./

# Install app dependencies
RUN pip install -r requirements.txt

RUN pipenv install --deploy --ignore-pipfile --system

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "run" ]