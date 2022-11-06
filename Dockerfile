FROM python:3.11.0
WORKDIR /app
RUN pip install asyncpg==0.27.0
RUN pip install SQLAlchemy==1.4.42
COPY . .
CMD python main.py