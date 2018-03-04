load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

py_binary(
    name = "LiquibaseViewer",
    srcs = ["LiquibaseViewer.py"],
    deps = [":LiquibaseXMLReader"]
)

py_library (
  name = "LiquibaseXMLReader",
  srcs = ["LiquibaseXMLReader.py", "LiquibaseData.py"]
)
