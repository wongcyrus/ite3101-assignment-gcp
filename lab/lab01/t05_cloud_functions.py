import os
import tempfile
import zipfile
from os import environ

from google.cloud import functions_v2
from google.cloud.functions_v2 import (BuildConfig, CreateFunctionRequest,
                                       Environment, Function, ServiceConfig,
                                       Source, StorageSource, GetFunctionRequest)

from lab.lab01.t01_bucket import upload_file_to_bucket

import json
import requests
import google.oauth2.id_token
import google.auth.transport.requests


def get_parent():
    project_id = environ.get("PROJECT_ID", "")
    locations = environ.get("LOCATIONS", "")
    parent = f"projects/{project_id}/locations/{locations}"
    return parent


def get_unique_function_name():
    project_id = environ.get("PROJECT_ID", "")
    locations = environ.get("LOCATIONS", "")
    parent = f"projects/{project_id}/locations/{locations}/functions/helloworld"
    return parent


# Reference
# https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient


def create_function(bucket_name: str):

    # https://gist.github.com/simonthompson99/362404d6142db3ed14908244f5750d08
    dirname = os.path.dirname(__file__)
    source = os.path.join(dirname, "hello_world.py")
    tmpdir = tempfile.mkdtemp()
    zip_fn = os.path.join(tmpdir, 'archive.zip')
    # TODO: Add file to zip

    upload_file_to_bucket(bucket_name, "hello_world.zip", zip_fn)
    description = "Hello World"

    storage_source = StorageSource()
    # TODO: set bucket name
    storage_source.object_ = "hello_world.zip"

    source = Source()
    source.storage_source = storage_source

    build_config = BuildConfig()
    # TODO: set runtime and entry point
    build_config.source = source

    service_config = ServiceConfig()
    service_config.available_memory = "256M"
    service_config.timeout_seconds = 60
    service_config.ingress_settings = ServiceConfig.IngressSettings.ALLOW_ALL

    fn = Function()
    fn.build_config = build_config
    fn.service_config = service_config
    fn.description = description
    fn.environment = Environment.GEN_2

    # set function_id to "translateToChineseTrandtional"
    # https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.CreateFunctionRequest

    create_function_request = CreateFunctionRequest()
    create_function_request.function = fn
    create_function_request.function_id = "helloworld"
    create_function_request.parent = get_parent()

    # TODO: Create a client
    
    # TODO: Make the request
    operation = None

    return operation


def check_cloud_function_state():
    get_function_request = GetFunctionRequest()
    get_function_request.name = get_unique_function_name()

    # TODO: Create a client
    client = functions_v2.FunctionServiceClient()
    # TODO: call the get_function request 
    fn = None
    return fn.state.name

# https://stackoverflow.com/questions/61573102/calling-a-google-cloud-function-from-within-python
def invoke_cloud_function_state(name):
    get_function_request = GetFunctionRequest()
    get_function_request.name = get_unique_function_name()
    client = functions_v2.FunctionServiceClient()
    fn = client.get_function(request=get_function_request)
    uri = fn.service_config.uri

    pass
