FROM python:3.7

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD python ./script.py

#CMD python ./Execute_AllCombinations.py
#CMD python ./Execute_Random.py
