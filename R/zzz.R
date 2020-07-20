
# import the `python_grade_learnr.py` module, selecting only the "public" facing functions
.onLoad <- function(libname, pkgname) {
  grade_module <- reticulate::import_from_path(module = "python_grade_learnr", path = system.file("python", package = packageName()))
  # expose only certain functions from Python so we don't pollute R global space in learnr
  module_names <- names(grade_module)
  # for now, the filter list is basic but we can imagine expanding it in the future
  filter_list <- c('Any', 'Callable', 'List', 'Tuple')
  filtered_names <- module_names[!(module_names %in% filter_list)]
  lapply(filtered_names, function(name) assign(name, grade_module[[name]], globalenv()))
}
