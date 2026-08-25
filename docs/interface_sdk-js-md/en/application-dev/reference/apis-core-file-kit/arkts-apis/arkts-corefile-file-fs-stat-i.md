# Stat

Represents detailed file information. Before calling any API of the **Stat()** class, use [stat()](../../../reference/apis-core-file-kit/js-apis-file-fs.md#fileiostat) to create a **Stat** instance.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## isBlockDevice

```TypeScript
isBlockDevice(): boolean
```

Checks whether this file is a block special file. A block special file supports access by block only, and it is cached when accessed.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isBLockDevice = fs.statSync(filePath).isBlockDevice();
```

## isCharacterDevice

```TypeScript
isCharacterDevice(): boolean
```

Checks whether this file is a character special file. A character special device supports random access, and it is not cached when accessed.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fs.statSync(filePath).isCharacterDevice();
```

## isDirectory

```TypeScript
isDirectory(): boolean
```

Checks whether this file is a directory.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let dirPath = pathDir + "/test";
let isDirectory = fs.statSync(dirPath).isDirectory();
```

## isFIFO

```TypeScript
isFIFO(): boolean
```

Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isFIFO = fs.statSync(filePath).isFIFO();
```

## isFile

```TypeScript
isFile(): boolean
```

Checks whether this file is a regular file.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isFile = fs.statSync(filePath).isFile();
```

## isSocket

```TypeScript
isSocket(): boolean
```

Checks whether this file is a socket.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isSocket = fs.statSync(filePath).isSocket();
```

## isSymbolicLink

```TypeScript
isSymbolicLink(): boolean
```

Checks whether this file is a symbolic link.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let isSymbolicLink = fs.statSync(filePath).isSymbolicLink();
```

## atime

```TypeScript
readonly atime: number
```

Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.  
**Note：**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is disabled.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## atimeNs

```TypeScript
readonly atimeNs?:bigint
```

Time of the last access to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 19 70.  
**Note：**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is disabled.

**Type:** bigint

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**System capability:** SystemCapability.FileManagement.File.FileIO

## ctime

```TypeScript
readonly ctime: number
```

Time when the file metadata was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

## ctimeNs

```TypeScript
readonly ctimeNs?:bigint
```

Time of the last status change of the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970.

**Type:** bigint

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**System capability:** SystemCapability.FileManagement.File.FileIO

## gid

```TypeScript
readonly gid: number
```

ID of the user group of the file.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

## ino

```TypeScript
readonly ino: bigint
```

File ID. Different files on the same device have different **ino**s.

**Type:** bigint

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

## location

```TypeScript
readonly location: LocationType
```

File location, which indicates whether the file is stored in a local device or in the cloud.

**Type:** [LocationType](arkts-corefile-file-fs-locationtype-e.md)

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## mode

```TypeScript
readonly mode: number
```

File permissions. The meaning of each bit is as follows:Note: The following values are in octal format. The return values are in decimal format. You need to convert the values.  
- **0o400**: The user has the read permission on a regular file or a directory entry. - **0o200**: The user has the permission to write a regular file or create and delete a directory entry. - **0o100**: The user has the permission to execute a regular file or search for the specified path in a directory. - **0o040**: The user group has the read permission on a regular file or a directory entry. - **0o020**: The user group has the permission to write a regular file or create and delete a directory entry. - **0o010**: The user group has the permission to execute a regular file or search for the specified path in a directory. - **0o004**: Other users have the permission to read a regular file or read a directory entry. - **0o002**: Other users have the permission to write a regular file or create and delete a directory entry. - **0o001**: Other users have the permission to execute a regular file or search for the specified path in a directory.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## mtime

```TypeScript
readonly mtime: number
```

Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## mtimeNs

```TypeScript
readonly mtimeNs?:bigint
```

Time of the last modification to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 1970.

**Type:** bigint

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**System capability:** SystemCapability.FileManagement.File.FileIO

## size

```TypeScript
readonly size: number
```

File size, in bytes. This parameter is valid only for regular files.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## uid

```TypeScript
readonly uid: number
```

ID of the file owner.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO
