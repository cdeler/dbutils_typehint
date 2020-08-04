from typing import Dict, Iterable, Optional

from dataclasses import dataclass


@dataclass
class FileInfo:
    name: str
    length: int
    path: str
    dir: bool

    def isDir(self) -> bool:
        return self.dir

    def isFile(self) -> bool:
        return not self.dir


class FS:
    """
    dbutils.fs provides utilities for working with FileSystems.
    Most methods in this package can take either a DBFS path (e.g., "/foo" or "dbfs:/foo"),
        or another FileSystem URI. For more info about a method, use dbutils.fs.help("methodName").
    """

    def cp(self, _from: str, to: str, recurse: bool = False) -> bool:
        """
        Copies a file or directory, possibly across FileSystems..

        Example: dbutils.cp("/mnt/my-folder/a", "s3n://bucket/b")

        :param _from: FileSystem URI of the source file or directory
        :param to: FileSystem URI of the destination file or directory
        :param recurse: if True, all files and directories will be recursively copied
        :return True if all files were successfully copied
        """
        pass

    def head(self, file: str, max_bytes: int = 65536) -> str:
        """
        Returns up to the first 'max_bytes' bytes of the given file as a String encoded in UTF-8.
        *
        Example: dbutils.head("/mnt/my-folder/my-file")

        :param file: FileSystem URI
        :param max_bytes: Maximum number of bytes to read
        :return String containing contents of the file, possibly truncated to the max bytes.
        """
        pass

    def ls(self, dirname: str) -> Iterable[FileInfo]:
        """
        Lists the contents of a directory.

        Example:
            import pprint
            for file in ls("/mnt/my-folder/"):
                pprint.pprint(file)

        :param dirname: FileSystem URI
        :return Ordered sequence of FileInfos containing the name and size of each file.
        """
        pass

    def mkdirs(self, dirname: str) -> bool:
        """
        Creates the given directory if it does not exist, also creating any necessary parent
            directories.

        Example: dbutils.mkdirs("/mnt/my-folder/a/b/c")

        :param dirname: FileSystem URI
        :return True if the directory was successfully created
        """

    def mv(self, _from: str, to: str, recurse: bool = False) -> bool:
        """
        Moves a file or directory, possibly across FileSystems.
            This is implemented as a copy followed by delete, even for intra-FileSystem moves.

        Example: dbutils.mv("/mnt/my-folder/a", "s3n://bucket/b")

        :param _from: FileSystem URI of the source file or directory
        :param to: FileSystem URI of the destination file or directory
        :param recurse: if True, all files and directories will be recursively moved
        :return True if the move was successful (so '_from' is deleted and 'to' contains the data)
        """
        pass

    def put(self, file: str, contents: str, overwrite: bool = False) -> bool:
        """
        Writes the given String out to a file, encoded in UTF-8.

        Example: dbutils.put("/mnt/my-folder/my-file", "Hello world!", true)

        :param file: FileSystem URI
        :param contents: Contents of file to write, encoded in System default charset.
        :param overwrite: If set to True, the file will be overwritten if it existed already.
                            Note that if overwrite is True and the the write fails, the original file
                            may still be deleted.
        :return True if the put was successful
        """
        pass

    def rm(self, dir_name: str, recurse: bool = False) -> bool:
        """
        Removes a file or directory.

        Example: dbutils.rm("/mnt/my-folder/", true)

        :param dir_name: FileSystem URI for a single file or a directory
        :param recurse: if True, all files and directories will be recursively deleted
        :return true if the file or directory was present and is now deleted
        """
        pass

    def mount(self,
              source: str,
              mount_point: str,
              encryption_type: str = "",
              owner: Optional[str] = None,
              extra_configs: Optional[Dict[str, str]] = None) -> bool:
        """
        Mounts the given source directory into DBFS at the given mount point.

        Examples:
            dbutils.mount("s3n://ACCESS_KEY:SECRET_KEY@my-twitter-bucket/tweets2013/", "/mnt/tweets")
            dbutils.ls("/mnt/tweets")

            dbutils.mount("s3n://ACCESS_KEY:SECRET_KEY@my-twitter-bucket/tweets2013/",
                          "/mnt/tweets",
                          "sse-s3")

        Mount points are persistent -- they will not be lost upon cluster or instance termination.
            The mount point metadata will remain until termination of your Databricks service
            (or until the point is explicitly unmounted). Once a directory is mounted, it can be
            treated like a normal DBFS directory.

        Mounting a directory will securely persist any provided credentials, enabling access
            to the data within the mounted directory without having to re-provide credentials.
            It is not possible to access or view the credentials used to support a mount point after
            the mount point is created and the command used to mount the data has been removed. Thus,
            one Databricks user can mount a bucket, delete the mount command and share the data
            with other Databricks users in the same organization, without sharing the security
            credentials with them.

        Mounting with encryption is possible. Currently, SSE-S3 and SSE-KMS are supported. Use
            encryptionType = "sse-s3" for sse-s3 encryption, "sse-kms" for sse-kms encryption with
            default kms master key, and "sse-kms:key-id" for sse-kms encryption with separate kms key.
            The source directory will not be mounted if an invalid encryption type is passed in.

        Once this method returns, the mount should be accessible from every instance within your
            shard. However, since this information may be cached, you may have to run refreshMounts()
            in a cluster for it to show up. Note that mount() actually runs refreshMounts() on the
            current cluster.

        :param source: FileSystem URI that contains the source data. This cannot be a DBFS URI.
        :param mount_point: The directory within DBFS to mount the source. This must be within /mnt.
        :param encryption_type: Encryption type with which we mount the source. This means every new
                                object written using this mount will be written with encryption.
        :param owner: Deprecated. This parameter is deprecated, please do not set it.
        :param extra_configs: A map containing extra configurations that will be used when
                                accessing the mount point. For every entry in the map, key
                                is the config name and the value is the value of the config.
                                Please only provide configs that are advised by Databricks documentations.
        :return True if the path was successfully mounted.
        """
        pass

    def mounts(self) -> Iterable:
        """
        Displays information about what is mounted within DBFS. The returned information includes
            the mount point, source directory, and encryption type. Any credentials used to mount the
            mount points listed will not be displayed
        """
        pass

    def refreshMounts(self) -> bool:
        """
        Forces all machines in this cluster to refresh their mount cache, ensuring they receive
            the most recent information.

        You may have to call this method if you mount or unmount a directory inside one cluster,
            and then quickly switch to another cluster (where it may be cached but not updated).

        Creating or deleting a mount automatically calls this method in the current cluster.

        :return True if the mount points were refreshed successfully.
        """
        pass

    def unmount(self, mountPoint: str) -> bool:
        """
        Deletes a DBFS mount point. Once this method returns, the mount point metadata is
            guaranteed to be deleted from persistent storage and should be inaccessible from every
            instance within your shard. However, since this information may be cached, you may have to
            run refreshMounts() in a cluster for it to disappear. Note that unmount() actually runs
            refreshMounts() on the current cluster.

        Example:
            dbutils.unmount("/mnt/tweets")

        :param mountPoint: DBFS directory previously mounted
        :return True if the mount point was successfully unmounted, or wasn't mounted originally.
        """
        pass
