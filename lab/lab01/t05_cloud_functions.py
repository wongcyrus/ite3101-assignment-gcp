import os
import tempfile
import zipfile

from google.cloud import functions_v2
from google.cloud.functions_v2 import (BuildConfig,
                                       Environment, Function, ServiceConfig,
                                       Source, StorageSource, GetFunctionRequest)

from lab.lab01.t01_bucket import upload_file_to_bucket

from google.oauth2 import service_account

dirname = os.path.dirname(__file__)
key_file_path = os.path.abspath(os.path.join(
    dirname, '..', '..', 'service_account_key.json'))
credentials = service_account.Credentials.from_service_account_file(
    key_file_path, scopes=['https://www.googleapis.com/auth/cloud-platform'])


def get_parent() ->str:
    project_id = credentials.project_id
    locations = os.environ.get("LOCATIONS", "")
    parent = os.path.join("projects", project_id, "locations", locations)
    return parent


def get_function_name(function_id: str) ->str:
    project_id = credentials.project_id
    locations = os.environ.get("LOCATIONS", "")
    parent = os.path.join("projects", project_id, "locations",
                          locations, "functions", function_id)
    return parent


# Reference
# https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.services.function_service.FunctionServiceClient


def create_function(bucket_name: str, function_id: str):

    # https://gist.github.com/simonthompson99/362404d6142db3ed14908244f5750d08
    source = os.path.abspath(os.path.join(dirname, "hello_world.py"))
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_fn = os.path.join(tmpdir, 'archive.zip')
        # TODO: Add "hello_world.py" file to zip but file name is "main.py"

        upload_file_to_bucket(bucket_name, "hello_world.zip", zip_fn)
    

    upload_file_to_bucket(bucket_name, "hello_world.zip", zip_fn)
    description = "Hello World"

    storage_source = StorageSource()
    # TODO: set bucket name
    storage_source.object_ = "hello_world.zip"

    source = Source()
    source.storage_source = storage_source

    build_config = BuildConfig()
    # TODO: set runtime to python312 and entry point
    build_config.source = source

    service_config = ServiceConfig()
    service_config.available_memory = "256M"
    service_config.timeout_seconds = 60
    service_config.ingress_settings = ServiceConfig.IngressSettings.ALLOW_ALL

    function = Function()
    function.name = get_parent() + "/functions/"+function_id
    function.build_config = build_config
    function.service_config = service_config
    function.description = description
    function.environment = Environment.GEN_2

    # Tips
    # https://cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.CreateFunctionRequest

    # TODO: Create a client
    
    # TODO: Make the request
    operation = None

    return operation


def check_cloud_function_state(function_id: str)->str:
    get_function_request = GetFunctionRequest()
    get_function_request.name = get_function_name(function_id)

    # TODO: Create a client
    client = functions_v2.FunctionServiceClient()
    # TODO: call the get_function request 
    fn = None
    return fn.state.name

