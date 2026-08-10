# CloudSyncConfig

云同步配置信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-relationalStore-interface CloudSyncConfig--><!--Device-relationalStore-interface CloudSyncConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## enablePredicate

```TypeScript
enablePredicate?: boolean
```

是否启用表级同步开关。true表示启用表级同步，false表示不启用。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudSyncConfig-enablePredicate?: boolean--><!--Device-CloudSyncConfig-enablePredicate?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

## mode

```TypeScript
mode: SyncMode
```

数据库同步模式。

**Type:** [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudSyncConfig-mode: SyncMode--><!--Device-CloudSyncConfig-mode: SyncMode-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

## predicate

```TypeScript
predicate?: RdbPredicates
```

表级同步谓词。仅当enablePredicate为true时，此参数有效。

**Type:** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudSyncConfig-predicate?: RdbPredicates--><!--Device-CloudSyncConfig-predicate?: RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

