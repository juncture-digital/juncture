FROM public.ecr.aws/lambda/python:3.12
COPY requirements.txt .
COPY serve.py .
RUN dnf -y install git
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD ["serve.handler"]