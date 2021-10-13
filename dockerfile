FROM public.ecr.aws/lambda/python:latest
# Copy function code
COPY slackclient.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "slackclient.slack_logger" ]