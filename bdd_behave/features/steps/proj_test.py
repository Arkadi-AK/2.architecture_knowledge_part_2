from behave import *

import projects.amount as am
import projects.zeros as zer


@given("get a pair of numbers")
def step(context):
    context.container = (4, 2)


@when("get the sum of two numbers")
def step(context):
    context.net = am.amount(context.container)


@then('get count zeros')
def step(context):
    assert zer.zeros(6) == 1
