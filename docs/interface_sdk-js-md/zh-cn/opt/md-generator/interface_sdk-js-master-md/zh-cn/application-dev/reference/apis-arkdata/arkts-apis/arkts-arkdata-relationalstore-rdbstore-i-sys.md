# RdbStore

提供管理关系数据库（RDB）方法的接口。 在使用以下API前，请先通过[getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore)方法获取RdbStore实例，并使用该实例调用对应接口方法。 在此基础上，建议优先使用[execute](arkts-arkdata-relationalstore-rdbstore-i.md#execute)方法完成数据库表结构和初始数据的 初始化，以确保相关接口调用的前置条件已满足。

**起始版本：** 23

<!--Device-relationalStore-interface RdbStore--><!--Device-relationalStore-interface RdbStore-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
```

## cleanDeviceDirtyData

```TypeScript
cleanDeviceDirtyData(table: string, cursor?: number): Promise<void>
```

本端手动清理对端删除后同步过来的数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>--><!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| cursor | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| 14800043 |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSync

```TypeScript
cloudSync(
      mode: SyncMode,
      predicates: RdbPredicates,
      progress: Callback<ProgressDetails>,
      callback: AsyncCallback<void>
    ): void
```

手动执行按条件进行端云同步，使用callback异步回调。使用该接口需要实现云同步功能。 > **说明：** > > 从API version 18开始，手动执行端云同步时，设置谓词条件时新增支持指定资产下载能力。此时，同步模式需要设置为`relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST`。 > > 谓词中支持使用主键（必填）和资产（可选）作为同步条件：选择资产作为同步条件时，谓词仅支持[equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)；指定资产的数量较多时（最 > 多支持指定50个资产），建议谓词中仅使用主键作为同步条件。

**起始版本：** 23

<!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void--><!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>
```

手动执行按条件进行端云同步，使用Promise异步回调。使用该接口需要实现云同步功能。 > **说明：** > > 从API version 18开始，手动执行端云同步时，设置谓词条件时新增支持指定资产下载能力。此时，同步模式需要设置为`relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST`。 > > 谓词中支持使用主键（必填）和资产（可选）作为同步条件：选择资产作为同步条件时，谓词仅支持[equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)；指定资产的数量较多时（最 > 多支持指定50个资产），建议谓词中仅使用主键作为同步条件。

**起始版本：** 23

<!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## delete

```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

根据DataSharePredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## delete

```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

根据DataSharePredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## lockCloudContainer

```TypeScript
lockCloudContainer(): Promise<number>
```

手动对应用云端数据库加锁，使用Promise异步回调。 > **说明：** > > 若手动加锁成功，则其他同账户设备的同应用禁止同步到云端。使用该接口需要实现云同步功能。

**起始版本：** 23

<!--Device-RdbStore-lockCloudContainer(): Promise<int>--><!--Device-RdbStore-lockCloudContainer(): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## query

```TypeScript
query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void
```

根据指定条件查询数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns: Array<string>,
      callback: AsyncCallback<ResultSet>
    ): void
```

根据指定条件查询数据库中的数据，支持指定要查询的列，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns?: Array<string>
    ): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据谓词条件匹配的数据记录查找对应记录的共享资源标识，返回查找的结果集。如果指定了列字段，则返回结果集中同时包含对应列的字段值，使用Promise异步回调。

**起始版本：** 23

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

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
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void
```

根据谓词条件匹配的数据记录查找对应记录的共享资源，返回查找的结果集，使用callback异步回调。

**起始版本：** 23

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

根据谓词条件匹配的数据记录查找对应记录的共享资源，返回查找到的共享资源的结果集，同时在结果集中返回谓词条件匹配的指定列名的字段值，使用callback异步回调。

**起始版本：** 23

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## restore

```TypeScript
restore(): Promise<void>
```

从副本关系型数据库文件恢复数据库，使用Promise异步回调。此接口仅供[HAMode](arkts-arkdata-relationalstore-hamode-e-sys.md#hamode系统接口)为MAIN_REPLICA时使用，且不支持在事务中使用。

**起始版本：** 23

<!--Device-RdbStore-restore(): Promise<void>--><!--Device-RdbStore-restore(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800010](../errorcode-data-rdb.md#14800010-数据库路径不合法) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## retainDeviceData

```TypeScript
retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>
```

保留对应[单版本表模式](../../../database/data-sync-of-rdb-store.md#数据同步存储机制)分布式数据表中对应设备同步过来的数据，删除其他设备同步过来的数据，使用Promise异步回 调。 不支持对[多设备协同表模式](../../../database/data-sync-of-rdb-store.md#数据同步存储机制)分布式数据表进行删除。 要删除数据越多，执行所需的时间越长。 > **说明：** > > 入参允许为空，数据库表名对应的设备id列表也允许为空，但是数据库表名和设备id不允许为空字符串。 > > 入参如果为空，则删除当前数据库所有单版本分布式表中所有其他设备同步过来的数据。 > > 入参中如果数据库表名对应的设备id列表为空，则删除该表下所有其他设备同步过来的数据。 > > 保留本地写入以及传入设备id同步过来的数据，其他设备id同步过来的数据会被删除。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>--><!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| retainDevices | Record & lt;string, Array & lt;string & gt; & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| 14800043 |
| 14800042 |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## unlockCloudContainer

```TypeScript
unlockCloudContainer(): Promise<void>
```

手动对应用云端数据库解锁，使用Promise异步回调。使用该接口需要实现云同步功能。

**起始版本：** 23

<!--Device-RdbStore-unlockCloudContainer(): Promise<void>--><!--Device-RdbStore-unlockCloudContainer(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## update

```TypeScript
update(
      table: string,
      values: ValuesBucket,
      predicates: dataSharePredicates.DataSharePredicates,
      callback: AsyncCallback<number>
    ): void
```

根据DataSharePredicates的指定实例对象更新数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过 RdbStore的 [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) 或 [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void--><!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## update

```TypeScript
update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

根据DataSharePredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore 的 [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) 或 [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## updateDistributedInfo

```TypeScript
updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<number>
```

更新分布式信息，只支持单版本表模式，使用Promise异步回调。 不支持对多设备协同表模式分布式数据表进行更新。 要更新数据越多，执行所需的时间越长。 > **说明：** > > 入参info中若要传入设备id信息，则设备id必须是已与当前设备建立网络连接的设备id。 > > 入参predicates中若要传入[ORIGIN_ORIDEVICE](arkts-arkdata-relationalstore-distributedfield-e-sys.md#distributedfield系统接口)，则只允许使用等于空或不等于空。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>--><!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [DistributedInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-distributedaccount-distributedinfo-i.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| 14800043 |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
