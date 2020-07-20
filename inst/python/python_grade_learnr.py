import random
import pandas as pd
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

def python_condition(x: Any, message: str, correct: bool) -> dict:
  """Return the proper structure for a particular type of condition."""
  return dict(x = x, message = message, correct = correct, type = "append")

def python_pass_if(x: Any, message = "") -> dict:
  """Return a pass condition."""
  return python_condition(x, message, correct = True)

def python_fail_if(x: Any, message = "") -> dict:
  """Return a fail condition."""
  return python_condition(x, message, correct = False)

# TODO make sure args are actually python_pass_if/fail_if functions
def python_grade_result(*args, **kwargs):
  """
  This function mirrors the `grade_result` function from {gradethis} package so that
  we can check Python exercises.
  
  For now, all it does is to get all of the python_pass_if/fail_if conditions and 
  returning it.
  """
  return args
  
def compare_output(user_output: Any, expected_output: Any) -> bool:
  if type(user_output) != type(expected_output):
    return False
  elif isinstance(user_output, pd.DataFrame) and isinstance(expected_output, pd.DataFrame):
      return user_output.equals(expected_output)
  else:
    return user_output == expected_output
  
def grade_conditions(conditions: List[Any], user_code_result: Any) -> Tuple[bool, dict]:
  """
  Goes through all conditions (python_pass_if, python_fail_if) and
  returns the first condition that comes True.
  """
  result = False
  condition = None
  for cond in conditions:
    condition = cond
    result = compare_output(cond['x'], user_code_result)
    if result:
      return result, condition
  return result, condition

def evaluate_code(code: List[str]):
  """ Evaluate check code so that expected output is ready """
  # Note: because Python is eager evaluation, we already have introduced
  # the `r` object when entering `python_grade_learnr`
  return eval("".join(code), {}, r)
    
def python_grade_learnr(label: str = None,
                        solution_code: str = None, 
                        user_code: str = None, 
                        check_code: Callable = None, 
                        envir_result: dict = None, 
                        evaluate_result: List = None,
                        envir_prep: dict = None, 
                        last_value: List = None, 
                        **kwargs) -> dict:
    """
    This function mirrors the `grade_learnr` function from {gradethis} package so that
    we can check Python exercises.
    """
    # evaluate check code so that expected output is ready
    if check_code != None and user_code != None:
      # TODO we need to be better about checking the user actually used pass if/fail functions
      check_code_conditions = evaluate_code(check_code)
      # evaluate user code so that we can compare to expected
      user_code_result = evaluate_code(user_code)
      # grade python_pass_if/fail_if conditions against user's code output
      result, condition = grade_conditions(check_code_conditions, user_code_result)
      # return a list representing a graded condition for learnr to process for feedback
      if result:
        praising = condition['message'] if condition['message'] != "" else praise()
        return dict(message = praising, correct = condition['correct'], type = "success", location = "append")
      else:
        encouraging = condition['message'] if condition['message'] != "" else encourage()
        return dict(message = encouraging, correct = condition['correct'], type = "error", location = "append")
    else:
      return dict(message = "I didn't receive your code. Did you write any?", correct = False, type = "error", location = "append")

if __name__ == '__main__':
  # for now we don't have any additional setup
  pass
else:
  # this is so that when we use `reticulate::import_from_path` to selectively
  # expose functions, we make sure to also import `r` which normally doesn't get
  # imported unless we do `reticulate::source`
  from __main__ import r
  

