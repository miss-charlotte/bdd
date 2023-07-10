from behave import given, when, then

@given('I have entered {number:d} into the calculator')
def step_given(context, number):
    if not hasattr(context, 'numbers'):
        context.numbers = []
    context.numbers.append(number)

@when('I press add')
def step_when(context):
    context.result = sum(context.numbers)

@then('the result should be {expected_result:d} on the screen')
def step_then(context, expected_result):
    assert context.result == expected_result

