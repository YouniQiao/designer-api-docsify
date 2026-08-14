# ResourceInfo

Describes the pre-downloaded resource information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cacheDownload-interface ResourceInfo--><!--Device-cacheDownload-interface ResourceInfo-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'cacheDownload';
```

## size

```TypeScript
readonly size: long
```

Size of a pre-downloaded resource after decompression, in bytes. If the value is a positive integer, the resource is successfully downloaded; if the value is **-1**, the resource fails to be downloaded.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ResourceInfo-readonly size: long--><!--Device-ResourceInfo-readonly size: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

