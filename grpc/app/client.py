import app.proto.messages_pb2 as messages
import app.proto.services_pb2_grpc as services
import grpc
import config


def run_client_on_port(port: str):
    """
     Starts client send and receive data on localhost:port via gRPC
    :param port: name of port on user host
    :return:
    """
    with grpc.insecure_channel(f'localhost:{port}') as channel:
        client = services.TeamRecommenderStub(channel)

        response: messages.TeamRecommendation = client.AskForTeam(
            messages.User(name="John Smith", description="nice man", skill_level=12)
        )
    print("Assets client received: " + str(response))


if __name__ == '__main__':
    run_client_on_port(config.PORT)
