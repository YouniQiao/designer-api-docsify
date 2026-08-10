# UserdataDirInfo (System API)

用户设备中/data目录下的空间占用详情。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-storageStatistics-export interface UserdataDirInfo--><!--Device-storageStatistics-export interface UserdataDirInfo-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## path

```TypeScript
path: string
```

路径名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserdataDirInfo-path: string--><!--Device-UserdataDirInfo-path: string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## totalCnt

```TypeScript
totalCnt: int
```

路径下目录和文件总数量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserdataDirInfo-totalCnt: int--><!--Device-UserdataDirInfo-totalCnt: int-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

## totalSize

```TypeScript
totalSize: long
```

路径占用的总空间大小，单位Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserdataDirInfo-totalSize: long--><!--Device-UserdataDirInfo-totalSize: long-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

