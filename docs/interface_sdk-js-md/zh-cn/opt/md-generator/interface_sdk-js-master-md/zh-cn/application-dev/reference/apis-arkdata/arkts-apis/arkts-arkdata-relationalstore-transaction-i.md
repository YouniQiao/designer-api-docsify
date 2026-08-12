# Transaction

提供以事务方式管理数据库的方法。事务对象是通过[createTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#createTransaction)接口创建的，不同事务对象之间的操作是隔离的，不同类型事务的区别见[TransactionType](arkts-arkdata-relationalstore-transactiontype-e.md#TransactionType) 。

当前关系型数据库同一时刻仅支持一个写事务，所以如果当前[RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md#RdbStore)存在写事务未释放，创建IMMEDIATE或EXCLUSIVE事务会返回14800024错误码。如果是创建的DEFERRED事务，则可能在首次使用DEFERRED事务调用写操作时返回14800024错误码。通过IMMEDIATE或EXCLUSIVE创建写事务或者DEFERRED事务升级到写事务之后，  
[RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md#RdbStore)的写操作也会返回14800024错误码。

当事务并发量较高且写事务持续时间较长时，返回14800024错误码的次数可能会变多，开发者可以通过减少事务占用时长减少14800024出现的次数，也可以通过重试的方式处理14800024错误码。

在使用以下API前，请先通过[createTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#createTransaction)方法获取Transaction实例，再通过此实例调用对应方法。

> **说明：**
> 
> - 本Interface首批接口从API version 14开始支持。

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](./app/context)。

**起始版本：** 14

<!--Device-relationalStore-interface Transaction--><!--Device-relationalStore-interface Transaction-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

向目标表中插入一组数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

**起始版本：** 14

<!--Device-Transaction-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>--><!--Device-Transaction-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>-End-->

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

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## batchInsertSync

```TypeScript
batchInsertSync(table: string, values: Array<ValuesBucket>): number
```

向目标表中插入一组数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

**起始版本：** 14

<!--Device-Transaction-batchInsertSync(table: string, values: Array<ValuesBucket>): long--><!--Device-Transaction-batchInsertSync(table: string, values: Array<ValuesBucket>): long-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## batchInsertWithConflictResolution

```TypeScript
batchInsertWithConflictResolution(
        table: string,
        values: Array<ValuesBucket>,
        conflict: ConflictResolution
    ): Promise<number>
```

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**起始版本：** 18

<!--Device-Transaction-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): Promise<long>--><!--Device-Transaction-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## batchInsertWithConflictResolutionSync

```TypeScript
batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,
      conflict: ConflictResolution): number
```

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**起始版本：** 18

<!--Device-Transaction-batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,      conflict: ConflictResolution): long--><!--Device-Transaction-batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,      conflict: ConflictResolution): long-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## batchInsertWithReturning

```TypeScript
batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)，返回  
[Result](arkts-arkdata-relationalstore-result-i.md#Result)。使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-Transaction-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## batchInsertWithReturningSync

```TypeScript
batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)，返回  
[Result](arkts-arkdata-relationalstore-result-i.md#Result)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-Transaction-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## commit

```TypeScript
commit(): Promise<void>
```

提交已执行的SQL语句，使用Promise异步回调。如果是使用异步接口执行SQL语句，请确保异步接口执行完成之后再调用commit接口，否则可能会丢失SQL操作。调用commit接口之后，该Transaction对象及创建的ResultSet对象都将被关闭。

**起始版本：** 14

<!--Device-Transaction-commit(): Promise<void>--><!--Device-Transaction-commit(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**起始版本：** 14

<!--Device-Transaction-delete(predicates: RdbPredicates): Promise<long>--><!--Device-Transaction-delete(predicates: RdbPredicates): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## deleteSync

```TypeScript
deleteSync(predicates: RdbPredicates): number
```

根据RdbPredicates的指定实例对象从数据库中删除数据。

**起始版本：** 14

<!--Device-Transaction-deleteSync(predicates: RdbPredicates): long--><!--Device-Transaction-deleteSync(predicates: RdbPredicates): long-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## deleteWithReturning

```TypeScript
deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>
```

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-arkdata-relationalstore-result-i.md#Result)，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>--><!--Device-Transaction-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## deleteWithReturningSync

```TypeScript
deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result
```

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-arkdata-relationalstore-result-i.md#Result)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result--><!--Device-Transaction-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## execute

```TypeScript
execute(sql: string, args?: Array<ValueType>): Promise<ValueType>
```

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType，使用Promise异步回调。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](#querySql)、  
[query](#query)接口代替、附加数据库可以使用  
[attach](arkts-arkdata-relationalstore-rdbstore-i.md#attach)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**起始版本：** 14

<!--Device-Transaction-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>--><!--Device-Transaction-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ValueType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## executeSync

```TypeScript
executeSync(sql: string, args?: Array<ValueType>): ValueType
```

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](#querySql)、  
[query](#query)接口代替、附加数据库可以使用  
[attach](arkts-arkdata-relationalstore-rdbstore-i.md#attach)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**起始版本：** 14

<!--Device-Transaction-executeSync(sql: string, args?: Array<ValueType>): ValueType--><!--Device-Transaction-executeSync(sql: string, args?: Array<ValueType>): ValueType-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>
```

向目标表中插入一行数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 14

<!--Device-Transaction-insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<long>--><!--Device-Transaction-insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## insertSync

```TypeScript
insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,
      conflict?: ConflictResolution): number
```

向目标表中插入一行数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 14

<!--Device-Transaction-insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,      conflict?: ConflictResolution): number--><!--Device-Transaction-insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,      conflict?: ConflictResolution): number-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | ValuesBucket \| sendableRelationalStore.ValuesBucket | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。

**起始版本：** 14

<!--Device-Transaction-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-Transaction-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySql

```TypeScript
querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

**起始版本：** 14

<!--Device-Transaction-querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>--><!--Device-Transaction-querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySqlSync

```TypeScript
querySqlSync(sql: string, args?: Array<ValueType>): ResultSet
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#taskpool)线程中执行。

**起始版本：** 14

<!--Device-Transaction-querySqlSync(sql: string, args?: Array<ValueType>): ResultSet--><!--Device-Transaction-querySqlSync(sql: string, args?: Array<ValueType>): ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySqlWithoutRowCount

```TypeScript
querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>
```

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于[querySql](#querySql)接口。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>--><!--Device-Transaction-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySqlWithoutRowCountSync

```TypeScript
querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet
```

根据指定SQL语句查询数据库中的数据，查询时不计算行数。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对querySqlWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#taskpool)线程中执行。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet--><!--Device-Transaction-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySync

```TypeScript
querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet
```

根据指定条件查询数据库中的数据。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到  
[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#taskpool)线程中执行。

**起始版本：** 14

<!--Device-Transaction-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet--><!--Device-Transaction-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## queryWithoutRowCount

```TypeScript
queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>
```

根据指定条件查询数据库中的数据，查询时不计算行数，性能优于[query](#query)接口。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>--><!--Device-Transaction-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## queryWithoutRowCountSync

```TypeScript
queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet
```

根据指定条件查询数据库中的数据，查询时不计算行数。对queryWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到  
[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#taskpool)线程中执行。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet--><!--Device-Transaction-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## rollback

```TypeScript
rollback(): Promise<void>
```

回滚已经执行的SQL语句，使用Promise异步回调。调用rollback接口之后，该Transaction对象及创建的ResultSet对象都会被关闭。

**起始版本：** 14

<!--Device-Transaction-rollback(): Promise<void>--><!--Device-Transaction-rollback(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 14

<!--Device-Transaction-update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<long>--><!--Device-Transaction-update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## updateSync

```TypeScript
updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number
```

根据RdbPredicates的指定实例对象更新数据库中的数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 14

<!--Device-Transaction-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long--><!--Device-Transaction-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |

## updateWithReturning

```TypeScript
updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式  
[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)，返回[Result](arkts-arkdata-relationalstore-result-i.md#Result)，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-Transaction-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |

## updateWithReturningSync

```TypeScript
updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式  
[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#ConflictResolution)，返回[Result](arkts-arkdata-relationalstore-result-i.md#Result)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getValue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getString)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用  
[queryByStep](arkts-arkdata-relationalstore-rdbstore-i.md#queryByStep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Transaction-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-Transaction-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800001-无效的参数) |
| [14800033](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800032](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800047](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800014-目标实例已关闭) |
