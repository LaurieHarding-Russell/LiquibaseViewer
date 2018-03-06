load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

py_library (
  name = "LiquibaseXMLReader",
  srcs = ["LiquibaseXMLReader.py", "//:LiquibaseData.py"],
  visibility = [ "//visibility:public" ]
)

py_library (
  name = "LiquibaseXMLWriter",
  srcs = ["LiquibaseXMLWriter.py", "//:LiquibaseData.py"],
  visibility = [ "//visibility:public" ]
)
