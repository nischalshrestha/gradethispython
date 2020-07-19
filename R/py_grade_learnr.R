
#' R wrapper around `python_grade_learnr`
#'
#' @param ... All learnr arguments required for checking
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

