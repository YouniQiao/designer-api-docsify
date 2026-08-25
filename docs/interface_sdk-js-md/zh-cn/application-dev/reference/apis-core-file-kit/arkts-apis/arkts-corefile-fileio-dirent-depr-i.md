# Dirent

在调用Dirent的方法前，需要先通过[dir.read()](arkts-corefile-fileio-read-f.md)方法（同步或异步）来构建一个Dirent实例。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## isBlockDevice

```TypeScript
isBlockDevice(): boolean
```

用于判断当前目录项是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isCharacterDevice

```TypeScript
isCharacterDevice(): boolean
```

用于判断当前目录项是否是字符特殊设备。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isDirectory

```TypeScript
isDirectory(): boolean
```

用于判断当前目录项是否是目录。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isFIFO

```TypeScript
isFIFO(): boolean
```

用于判断当前目录项是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isFile

```TypeScript
isFile(): boolean
```

用于判断当前目录项是否是普通文件。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isSocket

```TypeScript
isSocket(): boolean
```

用于判断当前目录项是否是套接字。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## isSymbolicLink

```TypeScript
isSymbolicLink(): boolean
```

用于判断当前目录项是否是符号链接。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 |
| --- |
| boolean |

## name

```TypeScript
readonly name: string
```

目录项的名称。

**类型：** string

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO
