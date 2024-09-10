FROM public.ecr.aws/lambda/python:3.12
COPY requirements.txt .
COPY serve.py .
RUN dnf -y install git && dnf update git -y && dnf upgrade git -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD ["serve.handler"]