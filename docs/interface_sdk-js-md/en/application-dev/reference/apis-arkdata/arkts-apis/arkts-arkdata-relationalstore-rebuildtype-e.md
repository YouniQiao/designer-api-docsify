# RebuildType

描述数据库重建类型的枚举。请使用枚举名称而非枚举值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-relationalStore-enum RebuildType--><!--Device-relationalStore-enum RebuildType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## NONE

```TypeScript
NONE = 0
```

表示数据库未进行重建。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RebuildType-NONE = 0--><!--Device-RebuildType-NONE = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## REBUILT

```TypeScript
REBUILT = 1
```

表示数据库进行了重建并且生成了空数据库，需要应用重新建表和恢复数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RebuildType-REBUILT = 1--><!--Device-RebuildType-REBUILT = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## REPAIRED

```TypeScript
REPAIRED = 2
```

表示数据库进行了修复，恢复了未损坏的数据，当前只有向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）具备该能力。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RebuildType-REPAIRED = 2--><!--Device-RebuildType-REPAIRED = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

