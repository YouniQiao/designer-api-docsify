# RootInfo（系统接口）

表示设备的根属性信息和接口能力。

**起始版本：** 9

**废弃版本：** 23

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { fileAccess } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
listFile(filter?: Filter): FileIterator
```

以同步方法从某个目录，基于过滤器，获取下一级符合条件的文件(夹)信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md)。目前仅支持内置存储设备过滤，外置存储设备不支持过滤。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** listFile

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## scanFile

```TypeScript
scanFile(filter?: Filter): FileIterator
```

以同步方法从某设备根节点开始，基于过滤器，递归获取符合条件的文件信息的迭代器对象FileIterator，然后通过[next](arkts-corefile-fileaccess-fileiterator-i-sys.md#next)方法返回 [FileInfo](arkts-corefile-fileaccess-fileinfo-i-sys.md)。目前仅支持内置存储设备。

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-corefile-file-fs-filter-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FileIterator](arkts-corefile-fileaccess-fileiterator-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900002 |
| 13900004 |
| 13900006 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900029 |
| 13900030 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900041 |
| 13900042 |
| 14000001 |
| 14000002 |
| 14000003 |
| 14000004 |
| 14300001 |
| 14300002 |
| 14300003 |
| 14300004 |

## deviceFlags

```TypeScript
deviceFlags: number
```

设备支持的能力。

**类型：** number

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## deviceType

```TypeScript
deviceType: number
```

设备支持的能力。

**类型：** number

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## displayName

```TypeScript
displayName: string
```

设备支持的能力。

**类型：** string

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## relativePath

```TypeScript
relativePath: string
```

根目录的相对路径。

**类型：** string

**起始版本：** 10

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。

## uri

```TypeScript
uri: string
```

设备支持的能力。

**类型：** string

**起始版本：** 9

**废弃版本：** 23

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**系统接口：** 此接口为系统接口。
