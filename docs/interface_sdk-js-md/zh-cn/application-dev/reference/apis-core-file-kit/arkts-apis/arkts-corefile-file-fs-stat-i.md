# Stat

文件具体信息，包含文件大小、权限模式、访问时间、修改时间等属性。在调用Stat的方法前，需要先通过[stat()](../../../reference/apis-core-file-kit/js-apis-file-fs.md#fileiostat)方法（同步或异步）构建一个 Stat实例。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## isBlockDevice

```TypeScript
isBlockDevice(): boolean
```

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isCharacterDevice

```TypeScript
isCharacterDevice(): boolean
```

判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isDirectory

```TypeScript
isDirectory(): boolean
```

判断文件是否为目录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isFIFO

```TypeScript
isFIFO(): boolean
```

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isFile

```TypeScript
isFile(): boolean
```

用于判断文件是否是普通文件。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isSocket

```TypeScript
isSocket(): boolean
```

判断文件是否是套接字。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## isSymbolicLink

```TypeScript
isSymbolicLink(): boolean
```

判断文件是否为符号链接。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900005 |
| 13900042 |

## atime

```TypeScript
readonly atime: number
```

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。  
**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## atimeNs

```TypeScript
readonly atimeNs?:bigint
```

上次访问该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。  
**注意**：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。

**类型：** bigint

**起始版本：** 15

**系统能力：** SystemCapability.FileManagement.File.FileIO

## ctime

```TypeScript
readonly ctime: number
```

最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## ctimeNs

```TypeScript
readonly ctimeNs?:bigint
```

最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的纳秒数。

**类型：** bigint

**起始版本：** 15

**系统能力：** SystemCapability.FileManagement.File.FileIO

## gid

```TypeScript
readonly gid: number
```

文件所有组的ID。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## ino

```TypeScript
readonly ino: bigint
```

标识该文件。通常同设备上的不同文件的INO不同。

**类型：** bigint

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## location

```TypeScript
readonly location: LocationType
```

文件的位置，表示该文件是本地文件或者云端文件。

**类型：** [LocationType](arkts-corefile-file-fs-locationtype-e.md)

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.File.FileIO

## mode

```TypeScript
readonly mode: number
```

表示文件权限，各特征位的含义如下：  
**说明：**以下值为八进制，取得的返回值为十进制，请换算后查看。
- 0o400：用户读。对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。
- 0o200：用户写。对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。
- 0o100：用户执行。对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。
- 0o040：用户组读。对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。
- 0o020：用户组写。对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。
- 0o010：用户组执行。对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。
- 0o004：其他读。对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。
- 0o002：其他写。对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。
- 0o001：其他执行。对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## mtime

```TypeScript
readonly mtime: number
```

上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## mtimeNs

```TypeScript
readonly mtimeNs?:bigint
```

上次修改该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。

**类型：** bigint

**起始版本：** 15

**系统能力：** SystemCapability.FileManagement.File.FileIO

## size

```TypeScript
readonly size: number
```

文件的大小，单位为Byte。仅对普通文件有效。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

## uid

```TypeScript
readonly uid: number
```

文件所有者的ID。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO
