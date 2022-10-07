from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import random
import grpc
import config
import app.proto.services_pb2_grpc as services
import app.proto.messages_pb2 as messages
from app.servicers import Service


def execute_server_on_port(port: str):
    """
    Starts gRPC server on localhost: port
    :param port:
    :return:
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    services.add_TeamRecommenderServicer_to_server(
        Service(),
        server
    )

    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    execute_server_on_port(config.PORT)
