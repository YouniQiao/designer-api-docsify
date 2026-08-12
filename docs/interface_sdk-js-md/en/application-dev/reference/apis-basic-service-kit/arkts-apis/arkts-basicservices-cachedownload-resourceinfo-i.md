# ResourceInfo

Describes the pre-downloaded resource information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cacheDownload-interface ResourceInfo--><!--Device-cacheDownload-interface ResourceInfo-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## size

```TypeScript
readonly size: long
```

Size of a pre-downloaded resource after decompression, in bytes. If the value is a positive integer, the resource is successfully downloaded; if the value is **-1**, the resource fails to be downloaded.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ResourceInfo-readonly size: long--><!--Device-ResourceInfo-readonly size: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

