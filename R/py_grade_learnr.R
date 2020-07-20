
#' R wrapper around `python_grade_learnr`
#'
#' To enable exercise checking in your learnr tutorial, set
#' `tutorial_options(exercise.checker = py_grade_learnr)` in the setup chunk
#' of your tutorial.
#'
#' @param label Label for exercise chunk
#' @param solution_code Code provided within the “-solution” chunk for the
#'   exercise.
#' @param user_code R code submitted by the user
#' @param check_code Code provided within the “-check” chunk for the exercise.
#' @param envir_result The R environment after the execution of the chunk.
#' @param evaluate_result The return value from the `evaluate::evaluate`
#'   function.
#' @param envir_prep A copy of the R environment before the execution of the
#'   chunk.
#' @param last_value The last value from evaluating the exercise.
#' @param ... Extra arguments supplied by learnr
#'
#' @return An R list which contains several fields indicating the result of the
#'   check.
#' @export
#'
py_grade_learnr <- function(label = NULL,
                            solution_code = NULL,
                            user_code = NULL,
                            check_code = NULL,
                            envir_result = NULL,
                            evaluate_result = NULL,
                            envir_prep = NULL,
                            last_value = NULL,
                            ...) {
  # need to cast environment types to a list so reticulate can translate to Python's dicts
  python_grade_learnr(
    label,
    solution_code,
    user_code,
    check_code,
    as.list(envir_result),
    evaluate_result,
    as.list(envir_prep),
    last_value,
    ...
  )
}

