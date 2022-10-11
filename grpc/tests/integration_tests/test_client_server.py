import pytest
from grpc import StatusCode
from grpc_testing import server_from_dictionary, strict_real_time
import app.proto.services_pb2 as services
import app.proto.messages_pb2 as messages
from app.servicers import Service


def test_recommend_team():
    """
    Test for bacis gRPC client-server
    :return:
    """

    this_Servicer = Service()
    dict_services = {
        services.DESCRIPTOR.services_by_name['TeamRecommender']: this_Servicer
    }
    test_server = server_from_dictionary(
        dict_services, strict_real_time())

    request = messages.User(name="John Smith", description="nice man", skill_level=2)
    method = test_server.invoke_unary_unary(
        method_descriptor=(services.DESCRIPTOR
            .services_by_name['TeamRecommender']
            .methods_by_name['AskForTeam']),
        invocation_metadata={},
        request=request, timeout=1)

    response, metadata, code, details = method.termination()
    assert code, StatusCode.OK
    assert response.recommended_team == "John Smith"*2
