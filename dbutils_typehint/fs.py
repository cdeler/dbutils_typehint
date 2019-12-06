import abc
from typing import Optional, Dict, Iterable


class LsSequenceChunk(abc.ABC):
    path = None  # type: str
    name = None  # type: str
    isDir = None  # type: bool
    size = 0  # type: int


class FS(abc.ABC):
    """
    dbutils.fs provides utilities for working with FileSystems.
    Most methods in this package can take either a DBFS path (e.g., "/foo" or "dbfs:/foo"),
        or another FileSystem URI. For more info about a method, use dbutils.fs.help("methodName").
    """

    @abc.abstractmethod
    def cp(self, _from: str, to: str, recursive: bool = False) -> bool:
        """
        Copies a file or directory, possibly across FileSystems
        """
        pass

    @abc.abstractmethod
    def head(self, file: str, max_bytes: int = 65536) -> str:
        """
        Returns up to the first ‘maxBytes’ bytes of the given file as a String encoded in UTF-8
        """
        pass

    @abc.abstractmethod
    def ls(self, dirname: str) -> Iterable[LsSequenceChunk]:
        """
        ls(dir: String): Seq -> Lists the contents of a directory
        """
        pass

    @abc.abstractmethod
    def mkdirs(self, dirname: str) -> bool:
        """
        Creates the given directory if it does not exist, also creating any necessary parent directories
        """

    @abc.abstractmethod
    def mv(self, _from: str, to: str, recurse: bool = False) -> bool:
        """
        Moves a file or directory, possibly across FileSystems
        """
        pass

    @abc.abstractmethod
    def put(self, file: str, contents: str, overwrite: bool = False) -> bool:
        """
        Writes the given String out to a file, encoded in UTF-8
        """
        pass

    @abc.abstractmethod
    def rm(self, dir: str, recurse: bool = False) -> bool:
        """
        rm(dir: String, recurse: boolean = false): boolean -> Removes a file or directory
        """
        pass

    @abc.abstractmethod
    def mount(self,
              source: str,
              mount_point: str,
              encryption_type: str = "",
              owner: Optional[str] = None,
              extra_configs: Optional[Dict[str, str]] = None) -> bool:
        """
        Mounts the given source directory into DBFS at the given mount point
        """
        pass

    @abc.abstractmethod
    def mounts(self) -> Iterable:
        """
        Displays information about what is mounted within DBFS
        """
        pass

    @abc.abstractmethod
    def refreshMounts(self) -> bool:
        """
        Forces all machines in this cluster to refresh their mount cache,
                ensuring they receive the most recent information
        """
        pass

    @abc.abstractmethod
    def unmount(mountPoint: str) -> bool:
        """
        Deletes a DBFS mount point
        """
        pass
