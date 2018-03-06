load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)

py_binary(
    name = "LiquibaseViewer",
    srcs = ["LiquibaseViewer.py"],
    deps = [
        "//liquibaseXML:LiquibaseXMLReader",
        "//liquibaseXML:LiquibaseXMLWriter"
      ]
)

exports_files(["LiquibaseData.py"])