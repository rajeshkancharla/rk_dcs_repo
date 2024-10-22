FROM python:3.9

WORKDIR /rk_dcs_repo

COPY . /rk_dcs_repo

RUN pip install -r requirements.txt

CMD [ "python", "./run_etl.py" ]