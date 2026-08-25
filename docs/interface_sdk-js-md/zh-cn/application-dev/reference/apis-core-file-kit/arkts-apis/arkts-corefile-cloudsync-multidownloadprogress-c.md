# MultiDownloadProgress

云文件批量缓存的进度信息。

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## 导入模块

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## getFailedFiles

```TypeScript
getFailedFiles(): Array<FailedFileInfo>
```

获取批量缓存失败的文件列表。

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[FailedFileInfo](arkts-corefile-cloudsync-failedfileinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 22400005 |

## getSuccessfulFiles

```TypeScript
getSuccessfulFiles(): Array<string>
```

获取批量缓存成功的文件列表。

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 22400005 |

## downloadedSize

```TypeScript
downloadedSize: number
```

已缓存的文件大小，取值范围为 [0, INT64_MAX)，单位：Byte。如果进度异常，返回值为 INT64_MAX。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## errType

```TypeScript
errType: DownloadErrorType
```

返回批量缓存任务执行失败时的错误类型。

**类型：** [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md)

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## failedCount

```TypeScript
failedCount: number
```

缓存失败的文件数，取值范围为0至400，单位：个。如果进度异常，返回值为-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## state

```TypeScript
state: State
```

批量缓存任务的执行状态。

**类型：** State

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## successfulCount

```TypeScript
successfulCount: number
```

缓存成功的文件数量，取值范围为0至400，单位：个。如果进度异常，返回值为-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## taskId

```TypeScript
taskId: number
```

批量缓存任务的ID，取值范围为0到INT64_MAX。如果进度异常，返回值为-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## totalCount

```TypeScript
totalCount: number
```

文件总数，取值范围为0至400，单位：个。如果进度异常，返回值为-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## totalSize

```TypeScript
totalSize: number
```

待缓存的文件总大小，取值范围为 [0, INT64_MAX)，单位为 Byte。如果进度异常，返回值为 INT64_MAX。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
