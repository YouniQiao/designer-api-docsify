# ResourceInfo

预下载的资源信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cacheDownload-interface ResourceInfo--><!--Device-cacheDownload-interface ResourceInfo-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## size

```TypeScript
readonly size: long
```

预下载资源解压后的大小，单位为字节（B）。当值为正整数时表示资源下载成功，-1表示下载失败。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ResourceInfo-readonly size: long--><!--Device-ResourceInfo-readonly size: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

