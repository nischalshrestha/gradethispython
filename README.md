<!-- badges: start -->
[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-blue.svg)](https://www.tidyverse.org/lifecycle/#experimental)
<!-- badges: end -->

# gradethispython

`gradethispython` is a package that is in development for Python exercise checking in [learnr](http://rstudio.github.io/learnr/). It is designed to mirror the functionalities of [gradethis](https://rstudio-education.github.io/gradethis/). Currently, it supports output checking and basic static code checking (ast analysis), using gradethis-like feedback messages when output or code is incorrect.

For exercise grading, we wrap a Python library called [pygradethis](https://github.com/nischalshrestha/pygradethis), which can either be used with this `gradethispython` R wrapper package, or by itself making it accessible for general Python grading use. At a minimum, we will mirror existing `{gradethis}` functionality but may provide more if we find Python specific grading needs. This will also simplify maintenance by allowing R issues to be opened on this R package, while Python issues to be opened on the Python repository.
