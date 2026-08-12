# @ohos.data.distributedKVStore

The **distributedKVStore** module implements collaboration between databases for different devices that form a Super Device. You can use the APIs provided by this module to save application data to a distributed key-value (KV) store and perform operations, such as adding, deleting, modifying, and querying data, and synchronizing data across devices.The **distributedKVStore** module provides the following functionalities:

- [KVManager](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md#KVManagerConfig): provides a **KVManager** instance to obtain KV store  
information.  
- [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md#KVStoreResultSet): provides APIs for accessing the results obtained  
from a KV store.  
- [Query](arkts-arkdata-distributedkvstore-query-c.md#Query): provides APIs for setting predicates for data query.  
- [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#SingleKVStore): provides APIs for querying data in single KV stores and  
synchronizing data across devices. The single KV stores manage data without distinguishing devices.  
- [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i.md#DeviceKVStore): provides APIs for querying data in device KV stores and  
synchronizing data across devices. This class inherits from [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#SingleKVStore).The device KV stores manage data by device.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace distributedKVStore--><!--Device-unnamed-declare namespace distributedKVStore-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKVManager](arkts-arkdata-distributedkvstore-createkvmanager-f.md#createkvmanager) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FieldNode](arkts-arkdata-distributedkvstore-fieldnode-c.md) |
| [Query](arkts-arkdata-distributedkvstore-query-c.md) |
| [Schema](arkts-arkdata-distributedkvstore-schema-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BackupConfig](arkts-arkdata-distributedkvstore-backupconfig-i.md) |
| [ChangeNotification](arkts-arkdata-distributedkvstore-changenotification-i.md) |
| [Constants](arkts-arkdata-distributedkvstore-constants-i.md) |
| [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i.md) |
| [Entry](arkts-arkdata-distributedkvstore-entry-i.md) |
| [KVManager](arkts-arkdata-distributedkvstore-kvmanager-i.md) |
| [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) |
| [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md) |
| [Options](arkts-arkdata-distributedkvstore-options-i.md) |
| [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md) |
| [Value](arkts-arkdata-distributedkvstore-value-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i-sys.md) |
| [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KVStoreType](arkts-arkdata-distributedkvstore-kvstoretype-e.md) | Enumerates the distributed KV store types.  \| Name \| Value\| Description \|  \| -------------------- \| - \| ------------------------------------------------------------ \|  \| DEVICE_COLLABORATION \| 0 \| Device KV store. & lt;br & gt;The device KV store manages data by device, which eliminates conflicts. Data can be queried by device. & lt;br & gt;**System capability**:SystemCapability.DistributedDataManager.KVStore.DistributedKVStore\ |  \| SINGLE_VERSION \| 1 \| Single KV store. & lt;br & gt;The single KV store does not differentiate data by device. If entries with the same key are modified on different devices, the value will be overwritten. & lt;br & gt;**System capability**: SystemCapability.DistributedDataManager.KVStore.Core\ |
| [SecurityLevel](arkts-arkdata-distributedkvstore-securitylevel-e.md) |
| [SubscribeType](arkts-arkdata-distributedkvstore-subscribetype-e.md) |
| [SyncMode](arkts-arkdata-distributedkvstore-syncmode-e.md) |
| [ValueType](arkts-arkdata-distributedkvstore-valuetype-e.md) |
