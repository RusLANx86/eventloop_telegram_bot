FROM python:3.7.3-stretch
WORKDIR /app
RUN pip install aiogram
RUN pip install pyrogram
COPY src/ /app
RUN ls /app
EXPOSE 5000
CMD [ "python", "/app/run_aiogram.py" ]

