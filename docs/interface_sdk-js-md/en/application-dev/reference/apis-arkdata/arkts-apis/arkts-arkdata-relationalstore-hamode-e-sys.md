# HAMode (System API)

描述关系型数据库存储的高可用性模式的枚举。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-relationalStore-enum HAMode--><!--Device-relationalStore-enum HAMode-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## SINGLE

```TypeScript
SINGLE = 0
```

表示将数据写入单个关系型数据库存储。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-HAMode-SINGLE = 0--><!--Device-HAMode-SINGLE = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## MAIN_REPLICA

```TypeScript
MAIN_REPLICA = 1
```

表示将数据写入主关系型数据库存储和副本关系型数据库存储，不支持加密场景和attach场景，会导致数据库写入性能的劣化。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-HAMode-MAIN_REPLICA = 1--><!--Device-HAMode-MAIN_REPLICA = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

