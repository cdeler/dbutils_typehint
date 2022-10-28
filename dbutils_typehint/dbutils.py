from collections import namedtuple
import dbutils_typehint.fs as fs
import dbutils_typehint.secrets as secrets

class NotebookExit(Exception):
    """Raised by dbutils.notebook.exit() to return a value from Notebook execution."""

class JobsHandler:
    def help(self, method_name=""):
        pass

class TaskValuesHandler:
    def get(self, taskKey, key, default=None, debugValue=None):
        pass
    def set(self, key, value):
        pass
    def help(self, method_name=""):
        pass

class NotebookHandler:
    def help(self, method_name=""):
        pass
    def exit(self, value): 
        pass
    def run(self, path, timeout_seconds, arguments={}, __databricks_internal_cluster_spec=None):
        pass

class WidgetsHandlerImpl:
    def help(self, method_name=""):
        pass
    def get(self, name):
        pass
    def getArgument(self, name, defaultValue=None):
        pass
    def text(self, name, defaultValue, label=None):
        pass
    def dropdown(self, name, defaultValue, choices, label=None):
        pass
    def combobox(self, name, defaultValue, choices, label=None):
        pass
    def multiselect(self, name, defaultValue, choices, label=None):
        pass
    def remove(self, name):
        pass
    def removeAll(self):
        pass

class CredentialsHandler:
    def help(self, method_name=None):
        pass
    def assumeRole(self, role):
        pass
    def showCurrentRole(self):
        pass
    def showRoles(self):
        pass
    def getCurrentCredentials(self):
        pass

class LibraryHandler:
    def help(self, method_name=None):
        pass
    def install(self, path):
        pass
    def installPyPI(self, project, version="", repo="", extras=""):
        pass
    def restartPython(self):
        pass
    def list(self):
        pass

class DataHandler:
    def help(self, method_name=None):
        pass
    def summarize(self, df, precise=False):
        pass


class DBUtils:
    """
    This class provides dbutils functionality for python notebooks, just like dbutils_v1.scala does
    it for Scala. For each of the calls here, we do two things: check whether the passed types are
    correct, and if so make a corresponding call to FSUtils object in Scala. For ls and mounts we do
    one extra thing - instead of returning result directly, we create a PythonSchemaSeq from it
    first. This is done to enable further operations with the result (e.g. call display function
    on it, or perform list operations on it)
    """

    @property
    def shell(self):
        pass

    @property
    def fs(self) -> fs.FS:
        pass
    @property
    def jobs(self) -> JobsHandler:
        pass
    @property
    def notebook(self) -> NotebookHandler:
        pass
    @property
    def secrets(self) -> secrets.Secrets:
        pass
    @property
    def widgets(self) -> WidgetsHandlerImpl:
        pass
    @property
    def library(self) -> LibraryHandler:
        pass
    @property
    def credentials(self) -> CredentialsHandler:
        pass
    @property
    def data(self) -> DataHandler:
        pass

    def help(self, method_name=""):
        pass
