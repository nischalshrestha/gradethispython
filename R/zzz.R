
# import the `pygradethis` module,
.onLoad <- function(libname, pkgname) {
  # environment where the `pygradethis` objects will be stored
  pkg_ns_env <- parent.env(environment())
  # import `pygradethis` and the two main modules
  pygradethis <- reticulate::import("pygradethis", convert = FALSE, delay_load = FALSE)
  # `python_grade_learnr` is our entry point function
  python_grade_learnr_module <- pygradethis$python_grade_learnr
  # `conditions` provides the conditions functions like `python_pass_if`
  conditions_module <- pygradethis$conditions
  # select only the "public" facing functions
  # for now, the filter list is basic but we can imagine expanding it in the future
  filter_list <- c('Any', 'Callable', 'List', 'Tuple')
  # assign functions to the `pkg_ns_env` environment
  lapply(
    names(python_grade_learnr_module),
    function(name) {
      if (!(name %in% filter_list)) {
        assign(name, python_grade_learnr_module[[name]], pkg_ns_env)
      }
    }
  )
  lapply(
    names(conditions_module),
    function(name) {
      if (!(name %in% filter_list)) {
        assign(name, conditions_module[[name]], pkg_ns_env)
      }
    }
  )
}
