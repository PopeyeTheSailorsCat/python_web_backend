# python_web_backend gRPC part

gRPC server which can recommend to user Team based on user info

To compile protobuf files run


```commandline
python -m grpc_tools.protoc --proto_path 'app/proto=proto' --python_out=. proto/messages.proto \
  && python -m grpc_tools.protoc --proto_path 'app/proto=proto' --python_out=. proto/services.proto
```

grpc_tools module will be installed with development dependencies

Poetry initial setup
-------------------------------------------------------------------------------
- Configure Poetry **(should be done once globally)**:

.. code::

    poetry config virtualenvs.in-project false
    poetry config virtualenvs.path <conda-install-path>/envs

Packages installation
-------------------------------------------------------------------------------
- Create and activate *conda* virtual environment for development:

.. code::

    conda create -n BaseApp python=3.10
    conda activate BaseApp

- Install dependencies with Poetry:

.. code::

    poetry install

## Run server and cliend
To run server execute
```
PYTHONPATH=. python app/server.py.
```
To run client execute
```
PYTHONPATH=. python app/client.py.
```

## Tests
To run integration tests use:
```commandline
pytest
```
