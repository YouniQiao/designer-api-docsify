# KVStoreType

Enumerates the distributed KV store types. | Name | Value| Description | | -------------------- | - | ------------------------------------------------------------ | | DEVICE_COLLABORATION | 0 | Device KV store.&lt;br&gt;The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.&lt;br&gt;**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore| | SINGLE_VERSION | 1 | Single KV store.&lt;br&gt;The single KV store does not differentiate data by device. If entries with the same key are modified on different devices, the value will be overwritten.&lt;br&gt;**System capability**: SystemCapability.DistributedDataManager.KVStore.Core|

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-distributedKVStore-enum KVStoreType--><!--Device-distributedKVStore-enum KVStoreType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## DEVICE_COLLABORATION

```TypeScript
DEVICE_COLLABORATION
```

Device-collaboration database, as specified by {@code DeviceKVStore}

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-DEVICE_COLLABORATION--><!--Device-KVStoreType-DEVICE_COLLABORATION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## SINGLE_VERSION

```TypeScript
SINGLE_VERSION
```

Single-version database, as specified by {@code SingleKVStore}

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-SINGLE_VERSION--><!--Device-KVStoreType-SINGLE_VERSION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

