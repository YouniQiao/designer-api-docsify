# SyncMode

同步模式枚举。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.SyncMode

<!--Device-distributedData-enum SyncMode--><!--Device-distributedData-enum SyncMode-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PULL_ONLY

```TypeScript
PULL_ONLY = 0
```

表示只能从远端拉取数据到本端。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.SyncMode#PULL_ONLY

<!--Device-SyncMode-PULL_ONLY = 0--><!--Device-SyncMode-PULL_ONLY = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PUSH_ONLY

```TypeScript
PUSH_ONLY = 1
```

表示只能从本端推送数据到远端。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.SyncMode#PUSH_ONLY

<!--Device-SyncMode-PUSH_ONLY = 1--><!--Device-SyncMode-PUSH_ONLY = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## PUSH_PULL

```TypeScript
PUSH_PULL = 2
```

表示从本端推送数据到远端，然后从远端拉取数据到本端。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.SyncMode#PUSH_PULL

<!--Device-SyncMode-PUSH_PULL = 2--><!--Device-SyncMode-PUSH_PULL = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

