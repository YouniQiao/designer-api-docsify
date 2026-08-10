# SyncMode

同步模式枚举。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-enum SyncMode--><!--Device-distributedKVStore-enum SyncMode-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PULL_ONLY

```TypeScript
PULL_ONLY
```

表示只能从远端拉取数据到本端。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncMode-PULL_ONLY--><!--Device-SyncMode-PULL_ONLY-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PUSH_ONLY

```TypeScript
PUSH_ONLY
```

表示只能从本端推送数据到远端。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncMode-PUSH_ONLY--><!--Device-SyncMode-PUSH_ONLY-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PUSH_PULL

```TypeScript
PUSH_PULL
```

表示从本端推送数据到远端，然后从远端拉取数据到本端。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyncMode-PUSH_PULL--><!--Device-SyncMode-PUSH_PULL-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

