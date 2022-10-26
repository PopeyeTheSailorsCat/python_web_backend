import sys
import pytest
from hw5.rabbitmq import agency, user_premium
import threading
import time

def f(name):
    print("hello {}".format(name))


def test_f(capfd):
    f("Tom")

    out, err = capfd.readouterr()
    assert out == "hello Tom\n"


def test_premium_user(capfd):
    premium_ap = {
        "name": "Test Premium aparts",
        "client": "premium",
        "cost": 100500
    }
    agency.send_apartment_to_clients(premium_ap)
    # loop = threading.Thread(target=user_premium.app_process)
    # loop.start()

    user_premium.app_process(running_test=True)
    out, err = capfd.readouterr()
    print(err)
    print(out)
    assert out == "hello Tom\n"


