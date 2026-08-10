# BundleStats

获取捆绑包统计信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-storageStatistics-export interface BundleStats--><!--Device-storageStatistics-export interface BundleStats-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## appSize

```TypeScript
appSize: long
```

应用安装文件大小（单位为Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleStats-appSize: long--><!--Device-BundleStats-appSize: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

## cacheSize

```TypeScript
cacheSize: long
```

应用缓存文件大小（单位为Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleStats-cacheSize: long--><!--Device-BundleStats-cacheSize: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

## dataSize

```TypeScript
dataSize: long
```

应用文件存储大小（除应用安装文件）（单位为Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleStats-dataSize: long--><!--Device-BundleStats-dataSize: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

