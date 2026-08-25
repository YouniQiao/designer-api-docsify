# MultiDownloadProgress

Represents the batch download progress of a file from the Drive Kit.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## getFailedFiles

```TypeScript
getFailedFiles(): Array<FailedFileInfo>
```

Obtains the list of files that fail to be downloaded in batches.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[FailedFileInfo](arkts-corefile-cloudsync-failedfileinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |

## getSuccessfulFiles

```TypeScript
getSuccessfulFiles(): Array<string>
```

Obtains the list of files that are successfully downloaded in batches.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |

## downloadedSize

```TypeScript
downloadedSize: number
```

Size of the downloaded file, in bytes. The value range is [0, INT64_MAX). If the progress is abnormal, the value **INT64_MAX** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## errType

```TypeScript
errType: DownloadErrorType
```

Type of the error returned when the batch download fails.

**Type:** [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md)

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## failedCount

```TypeScript
failedCount: number
```

Number of files that fail to be downloaded. The value ranges from 0 to 400. If the progress is abnormal, the value **-1** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## state

```TypeScript
state: State
```

Execution state of the batch download.

**Type:** State

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## successfulCount

```TypeScript
successfulCount: number
```

Number of successfully downloaded files. The value ranges from 0 to 400. If the progress is abnormal, the value **-1** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## taskId

```TypeScript
taskId: number
```

ID of a batch download task. The value ranges from 0 to INT64_MAX. If the progress is abnormal, the value **-1** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## totalCount

```TypeScript
totalCount: number
```

Total number of files. The value ranges from 0 to 400. If the progress is abnormal, the value **-1** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## totalSize

```TypeScript
totalSize: number
```

Total size of the files to be downloaded, in bytes. The value range is [0, INT64_MAX). If the progress is abnormal, the value **INT64_MAX** is returned.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
