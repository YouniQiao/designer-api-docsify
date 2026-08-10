# ExtBundleStats (System API)

系统应用或系统服务的空间占用详情。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-storageStatistics-export interface ExtBundleStats--><!--Device-storageStatistics-export interface ExtBundleStats-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## businessName

```TypeScript
businessName: string
```

系统应用包名或系统服务名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtBundleStats-businessName: string--><!--Device-ExtBundleStats-businessName: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## flag

```TypeScript
flag: boolean
```

系统应用或系统服务的空间占用是否需要在“设置-存储”界面单独展示。true表示单独显示，false表示不单独显示。 该值为false时，空间占用会被归并到businessName指定的应用中。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtBundleStats-flag: boolean--><!--Device-ExtBundleStats-flag: boolean-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## size

```TypeScript
size: long
```

系统应用或系统服务的空间占用大小，单位Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExtBundleStats-size: long--><!--Device-ExtBundleStats-size: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

