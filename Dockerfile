# Get ticket number and color series for dthe winners of powerball
FROM python:2.7-slim
MAINTAINER lars.radoor.hansen@gmail.com

COPY powerball.py powerball.py
CMD ["python", "powerball.py"]