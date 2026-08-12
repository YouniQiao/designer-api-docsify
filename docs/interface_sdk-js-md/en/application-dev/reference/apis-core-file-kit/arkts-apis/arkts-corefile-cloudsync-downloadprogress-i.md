# DownloadProgress

Represents information about the download progress of a cloud file.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudSync-interface DownloadProgress--><!--Device-cloudSync-interface DownloadProgress-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## error

```TypeScript
error: DownloadErrorType
```

Download error type.

**Type:** [DownloadErrorType](arkts-corefile-cloudsync-downloaderrortype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-error: DownloadErrorType--><!--Device-DownloadProgress-error: DownloadErrorType-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## processed

```TypeScript
processed: long
```

Size of the downloaded data, in bytes. The value range is [0, 9223372036854775807].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-processed: long--><!--Device-DownloadProgress-processed: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## size

```TypeScript
size: long
```

Size of the cloud file, in bytes. The value range is [0, 9223372036854775807].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-size: long--><!--Device-DownloadProgress-size: long-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## state

```TypeScript
state: State
```

File download state.

**Type:** State

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-state: State--><!--Device-DownloadProgress-state: State-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## uri

```TypeScript
uri: string
```

URI of the cloud file.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DownloadProgress-uri: string--><!--Device-DownloadProgress-uri: string-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

