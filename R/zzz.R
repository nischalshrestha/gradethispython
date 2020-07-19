
# source the python module `python_grade_learnr` so that learnr can access it
.onLoad <- function(libname, pkgname) {
  reticulate::source_python(system.file("python/python_grade_learnr.py", package="pygradethis"), envir=globalenv())
}
