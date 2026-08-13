# distributedData

The distributed data management module implements collaboration between databases of different devices for applications. The APIs provided by distributed data management can be used to save data to distributed databases and perform operations such as adding, deleting, modifying, querying, and synchronizing data in distributed databases. This module provides the following functions: - [KVManager](arkts-arkdata-distributeddata-kvmanagerconfig-i.md#KVManagerConfig): provides a **KVManager** instance to manage key-value (KV) stores. - [KvStoreResultSet&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkdata-distributeddata-kvstoreresultset-i.md#KvStoreResultSet): provides APIs to obtain the KV store result set and query or move the data read position. - [Query&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkdata-distributeddata-query-c.md#Query): provides APIs to query data from the database through a **Query** instance by using predicates. - [KVStore](arkts-arkdata-distributeddata-kvstoretype-e.md#KVStoreType): provides APIs to add data, delete data, and observe data changes and data sync through a **KVStore** instance. - [SingleKVStore](arkts-arkdata-distributeddata-singlekvstore-i.md#SingleKVStore): provides APIs to query and synchronize data in a single KV store. This class inherits from [KVStore](arkts-arkdata-distributeddata-kvstoretype-e.md#KVStoreType), and data is not distinguished by device. - [DeviceKVStore&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkdata-distributeddata-devicekvstore-i.md#DeviceKVStore): provides APIs to query and synchronize data in a device KV store. This class inherits from [KVStore](arkts-arkdata-distributeddata-kvstoretype-e.md#KVStoreType), and data is distinguished by device. [@ohos.data.distributedKVStore](arkts-data-distributedkvstore.md#@ohos.data.distributedKVStore).

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [distributedKVStore](arkts-data-distributedkvstore.md#@ohos.data.distributedKVStore)

<!--Device-unnamed-declare namespace distributedData--><!--Device-unnamed-declare namespace distributedData-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Constants](arkts-arkdata-distributeddata-constants-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKVManager](arkts-arkdata-distributeddata-createkvmanager-f.md#createKVManager) |
| [createKVManager](arkts-arkdata-distributeddata-createkvmanager-f.md#createKVManager) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Schema](arkts-arkdata-distributeddata-schema-c.md) |
| [FieldNode](arkts-arkdata-distributeddata-fieldnode-c.md) |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KVManagerConfig](arkts-arkdata-distributeddata-kvmanagerconfig-i.md) |
| [UserInfo](arkts-arkdata-distributeddata-userinfo-i.md) |
| [Value](arkts-arkdata-distributeddata-value-i.md) |
| [Entry](arkts-arkdata-distributeddata-entry-i.md) |
| [ChangeNotification](arkts-arkdata-distributeddata-changenotification-i.md) |
| [Options](arkts-arkdata-distributeddata-options-i.md) |
| [KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md) |
| [KVStore](arkts-arkdata-distributeddata-kvstore-i.md) |
| [SingleKVStore](arkts-arkdata-distributeddata-singlekvstore-i.md) |
| [DeviceKVStore](arkts-arkdata-distributeddata-devicekvstore-i.md) |
| [KVManager](arkts-arkdata-distributeddata-kvmanager-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UserType](arkts-arkdata-distributeddata-usertype-e.md) |
| [ValueType](arkts-arkdata-distributeddata-valuetype-e.md) |
| [SyncMode](arkts-arkdata-distributeddata-syncmode-e.md) |
| [SubscribeType](arkts-arkdata-distributeddata-subscribetype-e.md) |
| [KVStoreType](arkts-arkdata-distributeddata-kvstoretype-e.md) |
| [SecurityLevel](arkts-arkdata-distributeddata-securitylevel-e.md) |
