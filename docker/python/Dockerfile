FROM python:3.7
MAINTAINER Ryan Braving

COPY ./budgetproject /app

WORKDIR /app

RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#COPY ./docker/python/entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]

RUN adduser user
USER user
