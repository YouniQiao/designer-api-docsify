# KVStoreType

Enumerates the distributed KV store types.  
| Name | Value| Description |  
| -------------------- | - | ------------------------------------------------------------ |  
| DEVICE_COLLABORATION | 0 | Device KV store.The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.  
**System capability**: SystemCapability.DistributedDataManager.KVStore.DistributedKVStore|  
| SINGLE_VERSION | 1 | Single KV store.The single KV store does not differentiate data by device. If entries with the same key are modified on different devices, the value will be overwritten.  
**System capability**: SystemCapability.DistributedDataManager.KVStore.Core|

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## DEVICE_COLLABORATION

```TypeScript
DEVICE_COLLABORATION
```

Device-collaboration database, as specified by `DeviceKVStore`

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## SINGLE_VERSION

```TypeScript
SINGLE_VERSION
```

Single-version database, as specified by `SingleKVStore`

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core
