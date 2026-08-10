# DownloadProgress

云文件下载过程。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudSync-interface DownloadProgress--><!--Device-cloudSync-interface DownloadProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## error

```TypeScript
error: DownloadErrorType
```

下载的错误类型。

**Type:** [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-error: DownloadErrorType--><!--Device-DownloadProgress-error: DownloadErrorType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## processed

```TypeScript
processed: long
```

已下载数据大小，取值范围[0，9223372036854775807]（单位：Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-processed: long--><!--Device-DownloadProgress-processed: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## size

```TypeScript
size: long
```

当前云文件大小，取值范围[0，9223372036854775807]（单位：Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-size: long--><!--Device-DownloadProgress-size: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## state

```TypeScript
state: State
```

枚举值，云文件下载状态。

**Type:** [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-state: State--><!--Device-DownloadProgress-state: State-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## uri

```TypeScript
uri: string
```

当前云文件URI。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-uri: string--><!--Device-DownloadProgress-uri: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

