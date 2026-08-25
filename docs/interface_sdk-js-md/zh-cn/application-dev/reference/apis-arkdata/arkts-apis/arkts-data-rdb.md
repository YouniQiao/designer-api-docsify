# @ohos.data.rdb

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户 输入的SQL语句来满足复杂的场景需要。不支持Worker线程。该模块提供以下关系型数据库相关的常用功能：  
- [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md)：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。  
- [RdbStore](arkts-arkdata-rdb-rdbstore-i.md)：提供管理关系数据库（RDB）方法的接口。

> **说明：**&gt;
> - 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.relationalStore](arkts-data-relationalstore.md)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [relationalStore](arkts-data-relationalstore.md)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [deleteRdbStore](arkts-arkdata-rdb-deleterdbstore-f.md) |
| [deleteRdbStore](arkts-arkdata-rdb-deleterdbstore-f.md) |
| [getRdbStore](arkts-arkdata-rdb-getrdbstore-f.md) |
| [getRdbStore](arkts-arkdata-rdb-getrdbstore-f.md) |

### 类

| 名称 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

### 接口

| 名称 |
| --- |
| [RdbStore](arkts-arkdata-rdb-rdbstore-i.md) |
| [StoreConfig](arkts-arkdata-rdb-storeconfig-i.md) |

### 枚举

| 名称 |
| --- |
| [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) |
| [SyncMode](arkts-arkdata-rdb-syncmode-e.md) |

### 类型

| 名称 |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |
| [ValueType](arkts-arkdata-rdb-valuetype-t.md) |
