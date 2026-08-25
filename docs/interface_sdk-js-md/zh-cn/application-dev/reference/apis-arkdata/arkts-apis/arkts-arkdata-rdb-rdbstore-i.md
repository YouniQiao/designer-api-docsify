# RdbStore

提供管理关系数据库（RDB）方法的接口。在使用以下相关接口前，请使用 [executeSql](#executesql) 接口初始化数据库表结构和相关数据。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
```

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

向目标表中插入一组数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [batchInsert](arkts-arkdata-relationalstore-rdbstore-i.md#batchinsert)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

向目标表中插入一组数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [batchInsert](arkts-arkdata-relationalstore-rdbstore-i.md#batchinsert)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## beginTransaction

```TypeScript
beginTransaction(): void
```

在开始执行SQL语句之前，开始事务。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [beginTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#begintransaction)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## commit

```TypeScript
commit(): void
```

提交已执行的SQL语句。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [commit](arkts-arkdata-relationalstore-rdbstore-i.md#commit)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## delete

```TypeScript
delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

根据RdbPredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [delete](arkts-arkdata-relationalstore-rdbstore-i.md#delete)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [delete](arkts-arkdata-relationalstore-rdbstore-i.md#delete)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void
```

执行包含指定参数但不返回值的SQL语句，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [executeSql](arkts-arkdata-relationalstore-rdbstore-i.md#executesql)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>
```

执行包含指定参数但不返回值的SQL语句，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [executeSql](arkts-arkdata-relationalstore-rdbstore-i.md#executesql)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void
```

向目标表中插入一行数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [insert](arkts-arkdata-relationalstore-rdbstore-i.md#insert)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## insert

```TypeScript
insert(table: string, values: ValuesBucket): Promise<number>
```

向目标表中插入一行数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [insert](arkts-arkdata-relationalstore-rdbstore-i.md#insert)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void
```

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用callback异步回调。

> **说明：**&gt;
> 其中device通过调用<!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP1End-->deviceManager模块的接口均为系统接口，仅系统应用可用。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [obtainDistributedTableName](arkts-arkdata-relationalstore-rdbstore-i.md#obtaindistributedtablename)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | string | 是 |
| table | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string): Promise<string>
```

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用Promise异步回调。

> **说明：**&gt;
> 其中device通过调用<!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP1End-->deviceManager模块的接口均为系统接口，仅系统应用可用。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [obtainDistributedTableName](arkts-arkdata-relationalstore-rdbstore-i.md#obtaindistributedtablename)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | string | 是 |
| table | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## off

```TypeScript
off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

从数据库中删除指定类型的指定观察者，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-arkdata-relationalstore-rdbstore-i.md#off)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

注册数据库的观察者。当分布式数据库中的数据发生更改时，将调用回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [on](arkts-arkdata-relationalstore-rdbstore-i.md#on)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## query

```TypeScript
query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

根据指定条件查询数据库中的数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [query](arkts-arkdata-relationalstore-rdbstore-i.md#query)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [query](arkts-arkdata-relationalstore-rdbstore-i.md#query)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

## querySql

```TypeScript
querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void
```

根据指定SQL语句查询数据库中的数据，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

## querySql

```TypeScript
querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

根据指定SQL语句查询数据库中的数据，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

## rollBack

```TypeScript
rollBack(): void
```

回滚已经执行的SQL语句。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [rollBack](arkts-arkdata-relationalstore-rdbstore-i.md#rollback)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void
```

设置分布式列表，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setDistributedTables](arkts-arkdata-relationalstore-rdbstore-i.md#setdistributedtables)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>): Promise<void>
```

设置分布式列表，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setDistributedTables](arkts-arkdata-relationalstore-rdbstore-i.md#setdistributedtables)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void
```

在设备之间同步数据，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>
```

在设备之间同步数据，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, number] & gt; & gt; |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

根据RdbPredicates的指定实例对象更新数据库中的数据，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [update](arkts-arkdata-relationalstore-rdbstore-i.md#update)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [update](arkts-arkdata-relationalstore-rdbstore-i.md#update)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
