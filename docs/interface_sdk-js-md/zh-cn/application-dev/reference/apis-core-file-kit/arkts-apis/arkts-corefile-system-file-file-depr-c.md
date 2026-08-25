# File

文件类。

**起始版本：** 3

**废弃版本：** 10

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

## 导入模块

```TypeScript
```

## access

```TypeScript
static access(options: FileAccessOption): void
```

判断指定文件或目录是否存在。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [access](arkts-corefile-file-fs-access-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileAccessOption](arkts-corefile-system-file-fileaccessoption-depr-i.md) | 是 |

## copy

```TypeScript
static copy(options: FileCopyOption): void
```

将指定文件拷贝并存储到指定位置。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileCopyOption](arkts-corefile-system-file-filecopyoption-depr-i.md) | 是 |

## delete

```TypeScript
static delete(options: FileDeleteOption): void
```

删除本地文件。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [unlink](arkts-corefile-file-fs-unlink-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileDeleteOption](arkts-corefile-system-file-filedeleteoption-depr-i.md) | 是 |

## get

```TypeScript
static get(options: FileGetOption): void
```

获取指定本地文件的信息。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [stat](arkts-corefile-file-fs-stat-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileGetOption](arkts-corefile-system-file-filegetoption-depr-i.md) | 是 |

## list

```TypeScript
static list(options: FileListOption): void
```

获取指定路径下全部文件的列表。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [listFile](arkts-corefile-file-fs-listfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileListOption](arkts-corefile-system-file-filelistoption-depr-i.md) | 是 |

## mkdir

```TypeScript
static mkdir(options: FileMkdirOption): void
```

创建指定目录。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileMkdirOption](arkts-corefile-system-file-filemkdiroption-depr-i.md) | 是 |

## move

```TypeScript
static move(options: FileMoveOption): void
```

将指定文件移动到其他指定位置。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [moveFile](arkts-corefile-file-fs-movefile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileMoveOption](arkts-corefile-system-file-filemoveoption-depr-i.md) | 是 |

## readArrayBuffer

```TypeScript
static readArrayBuffer(options: FileReadArrayBufferOption): void
```

从指定文件中读取Buffer内容。仅支持文本文档读写。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [read](arkts-corefile-file-fs-read-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileReadArrayBufferOption](arkts-corefile-system-file-filereadarraybufferoption-depr-i.md) | 是 |

## readText

```TypeScript
static readText(options: FileReadTextOption): void
```

从指定文件中读取文本内容。仅支持文本文档读写。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [readText](arkts-corefile-file-fs-readtext-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileReadTextOption](arkts-corefile-system-file-filereadtextoption-depr-i.md) | 是 |

## rmdir

```TypeScript
static rmdir(options: FileRmdirOption): void
```

删除指定目录。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [rmdir](arkts-corefile-file-fs-rmdir-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileRmdirOption](arkts-corefile-system-file-filermdiroption-depr-i.md) | 是 |

## writeArrayBuffer

```TypeScript
static writeArrayBuffer(options: FileWriteArrayBufferOption): void
```

写Buffer内容到指定文件。仅支持文本文档读写。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [write](arkts-corefile-file-fs-write-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileWriteArrayBufferOption](arkts-corefile-system-file-filewritearraybufferoption-depr-i.md) | 是 |

## writeText

```TypeScript
static writeText(options: FileWriteTextOption): void
```

写文本内容到指定文件。仅支持文本文档读写。

**起始版本：** 3

**废弃版本：** 10

**替代接口：** [write](arkts-corefile-file-fs-write-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FileWriteTextOption](arkts-corefile-system-file-filewritetextoption-depr-i.md) | 是 |
