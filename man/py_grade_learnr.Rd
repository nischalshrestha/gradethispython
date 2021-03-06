% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/py_grade_learnr.R
\name{py_grade_learnr}
\alias{py_grade_learnr}
\title{R wrapper around `python_grade_learnr`}
\usage{
py_grade_learnr(
  label = NULL,
  solution_code = NULL,
  user_code = NULL,
  check_code = NULL,
  envir_result = NULL,
  evaluate_result = NULL,
  envir_prep = NULL,
  last_value = NULL,
  ...
)
}
\arguments{
\item{label}{Label for exercise chunk}

\item{solution_code}{Code provided within the “-solution” chunk for the
exercise.}

\item{user_code}{Python code submitted by the user}

\item{check_code}{Code provided within the “-check” chunk for the exercise.}

\item{envir_result}{The R environment after the execution of the chunk.}

\item{evaluate_result}{The return value from the `evaluate::evaluate`
function.}

\item{envir_prep}{A copy of the R environment before the execution of the
chunk.}

\item{last_value}{The last value from evaluating the exercise.}

\item{...}{Extra arguments supplied by learnr}
}
\value{
An R list which contains several fields indicating the result of the
  check.
}
\description{
To enable exercise checking in your learnr tutorial, set
`tutorial_options(exercise.checker = gradethispython::py_grade_learnr)` in the setup chunk
of your tutorial. Or, set the `exercise.checker` for an individual Python chunk.
}
