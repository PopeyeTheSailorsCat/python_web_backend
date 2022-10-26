from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import random
import grpc

import app.proto.services_pb2_grpc as services
import app.proto.messages_pb2 as messages


class Service(services.TeamRecommenderServicer):

    def AskForTeam(self, request: messages.User, context) -> messages.TeamRecommendation:
        """Return name of recommended team for this user.
        :param request: app.proto.messages_pb2.User: User requesting team recommendation
        :param context: not used
        :return: messages.TeamRecommendation: name of recommended team
        """
        return messages.TeamRecommendation(recommended_team=str(request.name * request.skill_level))
