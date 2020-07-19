
#' R wrapper around `python_grade_learnr`
#'
#' @param ... All learnr arguments required for checking
#'
#' @return An R list which contains several fields indicating the result of the
#'   check.
#' @export
#'
py_grade_learnr <- function(...) {
  python_grade_learnr(...)
}

