from typing import List


class SecretScope:
    @property
    def name(self) -> str:
        pass

    def getName(self) -> str:
        pass


class SecretMetadata:
    @property
    def key(self) -> str:
        pass


class Secrets:
    """
    Provides utilities for leveraging secrets within notebooks.
    Databricks documentation for more info: https://docs.databricks.com/security/secrets/index.html
    """

    def list(self, scope: str) -> List[SecretMetadata]:
        """
        Lists secret metadata for secrets within a scope

        :param scope: a secret scope name
        :return: a list of SecretMetadata object in the selected scope
        """
        pass

    def get(self, scope: str, key: str) -> str:
        """
        Gets the string representation of a secret value with scope and key

        :param scope: a secret scope name
        :param key: a secret name
        :return: a string which is representing the secret value
        """
        pass

    def getBytes(self, scope: str, key: str) -> bytes:
        """
        Gets the bytes representation of a secret value with scope and key

        :param scope: a secret scope name
        :param key: a secret name
        :return: a binary representation of  the secret value
        """

    def listScopes(self) -> List[SecretScope]:
        """
        Lists secret scopes

        :return: a list with all available secret scopes
        """
        pass
