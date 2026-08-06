# KVStoreType

Enumerates the distributed KV store types.  
| Name | Value| Description |  
| -------------------- | - | ------------------------------------------------------------ |  
| DEVICE\_COLLABORATION | 0 | Device KV store.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**System capability**:  
SystemCapability.DistributedDataManager.KVStore.DistributedKVStore|  
| SINGLE\_VERSION | 1 | Single KV store.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_The single KV store does not differentiate data by device. If entries with the same key are modified on different devices, the value will be overwritten.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_**System capability**: SystemCapability.DistributedDataManager.KVStore.Core|

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-enum KVStoreType--><!--Device-distributedKVStore-enum KVStoreType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## DEVICE_COLLABORATION

```TypeScript
DEVICE_COLLABORATION
```

Device-collaboration database, as specified by {@code DeviceKVStore}

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-DEVICE_COLLABORATION--><!--Device-KVStoreType-DEVICE_COLLABORATION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## SINGLE_VERSION

```TypeScript
SINGLE_VERSION
```

Single-version database, as specified by {@code SingleKVStore}

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-SINGLE_VERSION--><!--Device-KVStoreType-SINGLE_VERSION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

