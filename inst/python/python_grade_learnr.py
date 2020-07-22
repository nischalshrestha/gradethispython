import random
import pandas as pd
import parser
from typing import Any, Callable, List, Tuple

def praise() -> str:
  """Returns a random praise message"""
  return random.choice([
      "Absolutely fabulous!",
      "Amazing!",
      "Awesome!",
      "Beautiful!",
      "Bravo!",
      "Cool job!",
      "Delightful!",
      "Excellent!",
      "Fantastic!",
      "Great work!",
      "I couldn't have done it better myself.",
      "Impressive work!",
      "Lovely job!",
      "Magnificent!",
      "Nice job!",
      "Out of this world!",
      "Resplendent!",
      "Smashing!",
      "Someone knows what they're doing :)",
      "Spectacular job!",
      "Splendid!",
      "Success!",
      "Super job!",
      "Superb work!",
      "Swell job!",
      "Terrific!",
      "That's a first-class answer!",
      "That's glorious!",
      "That's marvelous!",
      "Very good!",
      "Well done!",
      "What first-rate work!",
      "Wicked smaht!",
      "Wonderful!",
      "You aced it!",
      "You rock!",
      "You should be proud.",
      ":)"
    ]
  )

def encourage() -> str:
  """Returns a random encouragement message"""
  return random.choice([
      "Please try again.",
      "Give it another try.",
      "Let's try it again.",
      "Try it again; next time's the charm!",
      "Don't give up now, try it one more time.",
      "But no need to fret, try it again.",
      "Try it again. I have a good feeling about this.",
      "Try it again. You get better each time.",
      "Try it again. Perseverence is the key to success.",
      "That's okay: you learn more from mistakes than successes. Let's do it one more time."
    ]
  )

def python_condition(x: Any, message: str, correct: bool, type: str = "value") -> dict:
  """Return the proper structure for a particular type of condition."""
  # Note: we don't use the type field from `gradethis::condition` yet, so assumes value
  # TODO think about whether we allow passing of a function (lambda or regular)
  return dict(x = x, message = message, correct = correct, type = type)

def python_pass_if(x: Any, message = "") -> dict:
  """Return a pass condition."""
  return python_condition(x, message, correct = True)

def python_fail_if(x: Any, message = "") -> dict:
  """Return a fail condition."""
  return python_condition(x, message, correct = False)
  
def python_result(message: str, correct: bool, type: str, location: str) -> dict:
  return dict(message = message, correct = correct, type = type, location = location)

def python_grade_result(*args, **kwargs):
  """
  This function mirrors the `grade_result` function from {gradethis} package so that
  we can check Python exercises.
  
  For now, all it does is to get all of the python_pass_if/fail_if conditions and 
  returning it.
  """
  # TODO make sure args are actually python_pass_if/fail_if functions
  return args
  
def python_compare_output(user_output: Any, expected_output: Any) -> bool:
  """Return whether the user output and expected output match"""
  if type(user_output) != type(expected_output):
    return False
  elif isinstance(user_output, pd.DataFrame) and isinstance(expected_output, pd.DataFrame):
      return user_output.equals(expected_output)
  else:
    return user_output == expected_output
  
def python_grade_conditions(conditions: List[Any], user_code_result: Any) -> Tuple[bool, dict]:
  """
  Goes through all conditions (python_pass_if, python_fail_if) and
  returns the first condition that comes True.
  """
  result = False
  condition = None
  for cond in conditions:
    condition = cond
    result = python_compare_output(cond['x'], user_code_result)
    if result:
      return result, condition
  return False, condition

def python_grade_learnr(label: str = None,
                        solution_code: str = None, 
                        user_code: str = None, 
                        check_code: List[str] = None, 
                        envir_result: dict = None, 
                        evaluate_result: List[str] = None,
                        envir_prep: dict = None, 
                        last_value: Any = None, 
                        **kwargs) -> dict:
    """
    This function mirrors the `grade_learnr` function from {gradethis} package so that
    we can check Python exercises.
    """
    # check if there is user_code
    if user_code and "".join(user_code) == "":
      return python_result(
        message = "I didn't receive your code. Did you write any?",
        correct = False,
        type = "error",
        location = "append"
      )
    # if there is check code and solution code, check if there is a solution code
    if (check_code and solution_code) and "".join(solution_code) == "":
      return python_result(
        message = "No solution is provided for this exercise.",
        correct = True,
        type = "info",
        location = "append"
      )
    
    # evaluate exercise
    try:
      # TODO should be checking the user actually used pass if/fail functions
      # Note: because Python is eager evaluation, we already have introduced
      # the `r` object in the current scope when entering this function
      # evaluate check code so that expected output is ready
      check_code_conditions = eval("".join(check_code), {}, r)
      # evaluate user code so that we can compare to expected
      user_code_result = eval("".join(user_code), {}, r)
    except EOFError:
      return python_result(correct = False, message = "Error occured while checking the submission", type = "error", location = "append")

    # grade python_pass_if/fail_if conditions against user's code output
    # TODO fix the bug where you get encourage for incorrect for a single pass_if condition
    result, condition = python_grade_conditions(check_code_conditions, user_code_result)

    # return a list representing a graded condition for learnr to process for feedback
    if result:
      # TODO concatenate praise before custom message
      praising = f"{praise()} {condition['message']}" if condition['message'] != "" else praise()
      return python_result(message = praising, correct = condition['correct'], type = "success", location = "append")
    else:
      return python_result(message = f"{encourage()} {condition['message']}", correct = condition['correct'], type = "error", location = "append")

if __name__ == '__main__':
  # for now we don't have any additional setup
  pass
else:
  # this is so that when we use `reticulate::import_from_path` to selectively
  # expose functions, we make sure to also import `r` which normally doesn't get
  # imported since we do not use `reticulate::source`
  from __main__ import r
  

