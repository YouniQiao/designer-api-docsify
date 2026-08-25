# @ohos.data.distributedKVStore(分布式键值数据库)

分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、端端同步等操作。该模块提供以下常用功能：  
- [KVManager](arkts-arkdata-distributedkvstore-kvmanager-i.md)：分布式键值数据库管理实例，用于获取数据库的相关信息。  
- [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)：提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。  
- [Query](arkts-arkdata-distributedkvstore-query-c.md)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。  
- [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md)：单版本分布式键值数据库，不对数据所属设备进行区分，提供查询数据和端端同步数据的方法。  
- [DeviceKVStore](arkts-arkdata-distributedkvstore-devicekvstore-i.md)：设备协同数据库，继承自  
[SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md)，以设备维度对数据进行区分，提供查询数据和端端同步数据的方法。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createKVManager(分布式键值数据库)](arkts-arkdata-distributedkvstore-createkvmanager-f.md) |

### 类

| 名称 |
| --- |
| [FieldNode(分布式键值数据库)](arkts-arkdata-distributedkvstore-fieldnode-c.md) |
| [Query(分布式键值数据库)](arkts-arkdata-distributedkvstore-query-c.md) |
| [Schema(分布式键值数据库)](arkts-arkdata-distributedkvstore-schema-c.md) |

### 接口

| 名称 |
| --- |
| [BackupConfig(分布式键值数据库)](arkts-arkdata-distributedkvstore-backupconfig-i.md) |
| [ChangeNotification(分布式键值数据库)](arkts-arkdata-distributedkvstore-changenotification-i.md) |
| [Constants(分布式键值数据库)](arkts-arkdata-distributedkvstore-constants-i.md) |
| [DeviceKVStore(分布式键值数据库)](arkts-arkdata-distributedkvstore-devicekvstore-i.md) |
| [Entry(分布式键值数据库)](arkts-arkdata-distributedkvstore-entry-i.md) |
| [KVManager(分布式键值数据库)](arkts-arkdata-distributedkvstore-kvmanager-i.md) |
| [KVManagerConfig(分布式键值数据库)](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) |
| [KVStoreResultSet(分布式键值数据库)](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md) |
| [Options(分布式键值数据库)](arkts-arkdata-distributedkvstore-options-i.md) |
| [SingleKVStore(分布式键值数据库)](arkts-arkdata-distributedkvstore-singlekvstore-i.md) |
| [Value(分布式键值数据库)](arkts-arkdata-distributedkvstore-value-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceKVStore(分布式键值数据库)](arkts-arkdata-distributedkvstore-devicekvstore-i-sys.md) |
| [SingleKVStore(分布式键值数据库)](arkts-arkdata-distributedkvstore-singlekvstore-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [KVStoreType(分布式键值数据库)](arkts-arkdata-distributedkvstore-kvstoretype-e.md) |
| [SecurityLevel(分布式键值数据库)](arkts-arkdata-distributedkvstore-securitylevel-e.md) |
| [SubscribeType(分布式键值数据库)](arkts-arkdata-distributedkvstore-subscribetype-e.md) |
| [SyncMode(分布式键值数据库)](arkts-arkdata-distributedkvstore-syncmode-e.md) |
| [ValueType(分布式键值数据库)](arkts-arkdata-distributedkvstore-valuetype-e.md) |
