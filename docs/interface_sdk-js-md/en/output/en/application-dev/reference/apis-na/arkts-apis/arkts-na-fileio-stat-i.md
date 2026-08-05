# Stat

Represents detailed file information. Before calling any API of the Stat() class, use stat() to create a Stat instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-fileIo-interface Stat--><!--Device-fileIo-interface Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## isBlockDevice

```TypeScript
isBlockDevice(): boolean
```

Checks whether this file is a block special file. A block special file supports access by block only, and it is cached when accessed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isBlockDevice(): boolean--><!--Device-Stat-isBlockDevice(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a block device or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isCharacterDevice

```TypeScript
isCharacterDevice(): boolean
```

Checks whether this file is a character special file. A character special device supports random access, and it is not cached when accessed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isCharacterDevice(): boolean--><!--Device-Stat-isCharacterDevice(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a character device or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isDirectory

```TypeScript
isDirectory(): boolean
```

Checks whether this file is a directory.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isDirectory(): boolean--><!--Device-Stat-isDirectory(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a directory or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isFIFO

```TypeScript
isFIFO(): boolean
```

Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isFIFO(): boolean--><!--Device-Stat-isFIFO(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a fifo file or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isFile

```TypeScript
isFile(): boolean
```

Checks whether this file is a regular file.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isFile(): boolean--><!--Device-Stat-isFile(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a normal file or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isSocket

```TypeScript
isSocket(): boolean
```

Checks whether this file is a socket.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isSocket(): boolean--><!--Device-Stat-isSocket(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a socket file or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## isSymbolicLink

```TypeScript
isSymbolicLink(): boolean
```

Checks whether this file is a symbolic link.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-isSymbolicLink(): boolean--><!--Device-Stat-isSymbolicLink(): boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the path/fd point to a symbolic link or not. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900005 | I/O error |
| 13900042 | Unknown error |

## atime

```TypeScript
readonly atime: long
```

Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970. NOTE: Currently, user data partitions are mounted in noatime mode by default, and atime update is disabled.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly atime: long--><!--Device-Stat-readonly atime: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## atimeNs

```TypeScript
readonly atimeNs?:bigint
```

Time of the last access to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970. NOTE: Currently, user data partitions are mounted in noatime mode by default, and atime update is disabled.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly atimeNs?:bigint--><!--Device-Stat-readonly atimeNs?:bigint-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## ctime

```TypeScript
readonly ctime: long
```

Time when the file metadata was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly ctime: long--><!--Device-Stat-readonly ctime: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## ctimeNs

```TypeScript
readonly ctimeNs?:bigint
```

Time of the last status change of the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly ctimeNs?:bigint--><!--Device-Stat-readonly ctimeNs?:bigint-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## gid

```TypeScript
readonly gid: long
```

ID of the user group of the file.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly gid: long--><!--Device-Stat-readonly gid: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## ino

```TypeScript
readonly ino: bigint
```

File identifier, which varies with files on the same device.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly ino: bigint--><!--Device-Stat-readonly ino: bigint-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## location

```TypeScript
readonly location: LocationType
```

File location, which indicates whether the file is stored in a local device or in the cloud.

**Type:** LocationType

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly location: LocationType--><!--Device-Stat-readonly location: LocationType-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## mode

```TypeScript
readonly mode: long
```

File permissions. The meaning of each bit is as follows: The following values are in octal format. The return values are in decimal format. You need to convert the values. 0o400: The user has the read permission on a regular file or a directory entry. 0o200: The user has the permission to write a regular file or create and delete a directory entry. 0o100: The user has the permission to execute a regular file or search for the specified path in a directory. 0o040: The user group has the read permission on a regular file or a directory entry. 0o020: The user group has the permission to write a regular file or create and delete a directory entry. 0o010: The user group has the permission to execute a regular file or search for the specified path in a directory. 0o004: Other users have the permission to read a regular file or read a directory entry. 0o002: Other users have the permission to write a regular file or create and delete a directory entry. 0o001: Other users have the permission to execute a regular file or search for the specified path in a directory.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly mode: long--><!--Device-Stat-readonly mode: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## mtime

```TypeScript
readonly mtime: long
```

Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly mtime: long--><!--Device-Stat-readonly mtime: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## mtimeNs

```TypeScript
readonly mtimeNs?:bigint
```

Time of the last modification to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly mtimeNs?:bigint--><!--Device-Stat-readonly mtimeNs?:bigint-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## size

```TypeScript
readonly size: long
```

File size, in bytes. This parameter is valid only for regular files.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly size: long--><!--Device-Stat-readonly size: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## uid

```TypeScript
readonly uid: long
```

ID of the file owner.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Stat-readonly uid: long--><!--Device-Stat-readonly uid: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

