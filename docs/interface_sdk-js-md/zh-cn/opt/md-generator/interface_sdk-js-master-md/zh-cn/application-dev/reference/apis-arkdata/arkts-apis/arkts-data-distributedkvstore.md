# @ohos.data.distributedKVStore

分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、端端同步等操作。 该模块提供以下常用功能： - [KVManager](arkts-arkdata-distributedkvstore-kvmanager-i.md#kvmanager)：分布式键值数据库管理实例，用于获取数据库的相关信息。 - [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md#kvstoreresultset)：提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。 - [Query](arkts-arkdata-distributedkvstore-query-c.md#query)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。 - [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#singlekvstore)：单版本分布式键值数据库，不对数据所属设备进行区分，提供查询数据和端端同步数据的方法。 - [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i.md#devicekvstore)：设备协同数据库，继承自 [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#singlekvstore)，以设备维度对数据进行区分，提供查询数据和端端同步数据的方法。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace distributedKVStore--><!--Device-unnamed-declare namespace distributedKVStore-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [createKVManager](arkts-arkdata-distributedkvstore-createkvmanager-f.md#createkvmanager) |

### 类

| 名称 |
| --- |
| [FieldNode](arkts-arkdata-distributedkvstore-fieldnode-c.md) |
| [Query](arkts-arkdata-distributedkvstore-query-c.md) |
| [Schema](arkts-arkdata-distributedkvstore-schema-c.md) |

### 接口

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i-sys.md) |
| [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Constants](arkts-arkdata-distributedkvstore-constants-e.md) |
| [KVStoreType](arkts-arkdata-distributedkvstore-kvstoretype-e.md) |
| [SecurityLevel](arkts-arkdata-distributedkvstore-securitylevel-e.md) |
| [SubscribeType](arkts-arkdata-distributedkvstore-subscribetype-e.md) |
| [SyncMode](arkts-arkdata-distributedkvstore-syncmode-e.md) |
| [ValueType](arkts-arkdata-distributedkvstore-valuetype-e.md) |
