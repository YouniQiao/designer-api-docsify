# DataMigrationProgress (System API)

描述数据迁移的进度信息，包含进度百分比和预估剩余时间。该接口为数据迁移回调onProgress方法的参数类型。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fontManager-interface DataMigrationProgress--><!--Device-fontManager-interface DataMigrationProgress-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## progressPercentage

```TypeScript
progressPercentage: int
```

数据迁移百分比进度，进度值根据已迁移的字体文件数量或大小计算，可能不是均匀增长。当progressPercentage为100时，迁移任务即将完成，onResult回调即将被调用。取值范围为[0, 100]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationProgress-progressPercentage: int--><!--Device-DataMigrationProgress-progressPercentage: int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## timeRemaining

```TypeScript
timeRemaining: int
```

预计剩余时间，可能因设备性能、文件大小、系统负载等因素而有所差异。取值范围为非负整数，最小值为0。单位为s。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationProgress-timeRemaining: int--><!--Device-DataMigrationProgress-timeRemaining: int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

