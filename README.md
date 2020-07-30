<!-- badges: start -->
[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-blue.svg)](https://www.tidyverse.org/lifecycle/#experimental)
<!-- badges: end -->

# gradethispython

`gradethispython` is a package that is in development for Python exercise checking in [learnr](http://rstudio.github.io/learnr/). It is designed to mirror the functionalities of [gradethis](https://rstudio-education.github.io/gradethis/). Currently, it supports output checking and basic static code checking (ast analysis), using gradethis-like feedback messages when output or code is incorrect.

**NOTE:** There will eventually be a standalone Python package (and repository) that can be used with this `gradethispython` R wrapper package, or by itself making it accessible for general Python grading use. This will also simplify maintenance by allowing R issues to be opened on this R package, while Python issues to be opened on the Python repository.
