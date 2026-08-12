# KVStoreType

Enumerates the distributed KV store types.  
| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](arkts-arkdata-distributeddata-value-i.md) | Description |
| -------------------- | - | ------------------------------------------------------------ |
| [DEVICE_COLLABORATION](#device_collaboration) | 0 | Device KV store. & lt;br & gt;The device KV store manages data by device, which eliminates conflicts. Data can be queried by device. & lt;br & gt;**System capability**:SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| [SINGLE_VERSION](#single_version) | 1 |

**Since:** 9

<!--Device-distributedKVStore-enum KVStoreType--><!--Device-distributedKVStore-enum KVStoreType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## DEVICE_COLLABORATION

```TypeScript
DEVICE_COLLABORATION
```

Device-collaboration database, as specified by {@code DeviceKVStore}

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-DEVICE_COLLABORATION--><!--Device-KVStoreType-DEVICE_COLLABORATION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## SINGLE_VERSION

```TypeScript
SINGLE_VERSION
```

Single-version database, as specified by {@code SingleKVStore}

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVStoreType-SINGLE_VERSION--><!--Device-KVStoreType-SINGLE_VERSION-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core
