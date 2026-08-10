# RdbStore

提供管理关系数据库（RDB）方法的接口。

在使用以下API前，请先通过[getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore)方法获取RdbStore实例，并使用该实例调用对应接口方法。

在此基础上，建议优先使用[execute](arkts-arkdata-relationalstore-rdbstore-i.md#execute)方法完成数据库表结构和初始数据的初始化，以确保相关接口调用的前置条件已满足。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface RdbStore--><!--Device-relationalStore-interface RdbStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## cleanDeviceDirtyData

ArkTS-Dyn:
```TypeScript
cleanDeviceDirtyData(table: string, cursor?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>
```

本端手动清理对端删除后同步过来的数据。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>--><!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 表示需要清理数据库表的名称。数据库表名只能由字母、数字和下划线组成，不能包含其他字符，长度为[1, 256]。 |
| cursor | ArkTS-Dyn: number  <br>ArkTS-Sta：long | No | 表示数据游标，不大于此游标的脏数据将被清理。整数类型，取值应大于0。当传入小于等于0的值时，会抛出异常，异常信息为无效的参数。当此参数不填时，清理当前表的所有脏数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800021 | SQLite: Generic error. |
| 14800024 | SQLite: The database file is locked. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800043 | The database does not support this scenario. Possible causes: 1. The database type is not support;2. The table type is not supported; 3. This is a read-only database. |
| 14800015 | The database does not respond. |
| 14800014 | The target instance is already closed. |

## cloudSync

```TypeScript
cloudSync(
      mode: SyncMode,
      predicates: RdbPredicates,
      progress: Callback<ProgressDetails>,
      callback: AsyncCallback<void>
    ): void
```

手动执行按条件进行端云同步，使用callback异步回调。使用该接口需要实现云同步功能。

> **说明：**
> 
> 从API version 18开始，手动执行端云同步时，设置谓词条件时新增支持指定资产下载能力。此时，同步模式需要设置为`relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST`。
> 
> 谓词中支持使用主键（必填）和资产（可选）作为同步条件：选择资产作为同步条件时，谓词仅支持[equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)；指定资产的数量较多时（最
> 多支持指定50个资产），建议谓词中仅使用主键作为同步条件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void--><!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes | 表示数据库的同步模式。 |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | 表示同步数据的谓词条件。 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProgressDetails&gt; | Yes | 用来处理数据库同步详细信息的回调函数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当同步成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type. 6. The callback must be a function. |
| 801 | Capability not supported. |
| 202 | if permission verification failed, application which is not a system application uses system API. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>
```

手动执行按条件进行端云同步，使用Promise异步回调。使用该接口需要实现云同步功能。

> **说明：**
> 
> 从API version 18开始，手动执行端云同步时，设置谓词条件时新增支持指定资产下载能力。此时，同步模式需要设置为`relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST`。
> 
> 谓词中支持使用主键（必填）和资产（可选）作为同步条件：选择资产作为同步条件时，谓词仅支持[equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)；指定资产的数量较多时（最
> 多支持指定50个资产），建议谓词中仅使用主键作为同步条件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes | 表示数据库的同步模式。 |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | 表示同步数据的谓词条件。 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProgressDetails&gt; | Yes | 用来处理数据库同步详细信息的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。返回同步结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type. |
| 801 | Capability not supported. |
| 202 | if permission verification failed, application which is not a system application uses system API. |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |

## delete

ArkTS-Dyn:
```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void
```

根据DataSharePredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的删除条件。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | 回调函数。当删除数据成功，err为undefined，data为受影响的行数量；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## delete

ArkTS-Dyn:
```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

ArkTS-Sta:
```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>
```

根据DataSharePredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的删除条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回受影响的行数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## lockCloudContainer

ArkTS-Dyn:
```TypeScript
lockCloudContainer(): Promise<number>
```

ArkTS-Sta:
```TypeScript
lockCloudContainer(): Promise<int>
```

手动对应用云端数据库加锁，使用Promise异步回调。

> **说明：**
> 
> 若手动加锁成功，则其他同账户设备的同应用禁止同步到云端。使用该接口需要实现云同步功能。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RdbStore-lockCloudContainer(): Promise<int>--><!--Device-RdbStore-lockCloudContainer(): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。如果加锁成功，返回锁的有效时长；如果加锁失败，返回0，单位：ms。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## query

```TypeScript
query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void
```

根据指定条件查询数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用  
[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的查询条件。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes | 回调函数。返回ResultSet对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns: Array<string>,
      callback: AsyncCallback<ResultSet>
    ): void
```

根据指定条件查询数据库中的数据，支持指定要查询的列，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用  
[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的查询条件。 |
| columns | Array&lt;string&gt; | Yes | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes | 回调函数。返回ResultSet对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns?: Array<string>
    ): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用  
[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的查询条件。 |
| columns | Array&lt;string&gt; | No | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResultSet&gt; | 返回ResultSet对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据谓词条件匹配的数据记录查找对应记录的共享资源标识，返回查找的结果集。如果指定了列字段，则返回结果集中同时包含对应列的字段值，使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | 表示查询的谓词条件。 |
| columns | Array&lt;string&gt; | No | 表示要查找的列字段名。此参数不填时，返回的结果集中只包含共享资源标识字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResultSet&gt; | Promise对象。返回查询的结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The predicates must be an RdbPredicates. 4. The columns must be a string array. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void
```

根据谓词条件匹配的数据记录查找对应记录的共享资源，返回查找的结果集，使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | 表示查询的谓词条件。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes | 回调函数。返回查询的结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The predicates must be an RdbPredicates. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

根据谓词条件匹配的数据记录查找对应记录的共享资源，返回查找到的共享资源的结果集，同时在结果集中返回谓词条件匹配的指定列名的字段值，使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | 表示查询的谓词条件。 |
| columns | Array&lt;string&gt; | Yes | 表示要查找的列字段名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes | 回调函数。返回查询的结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The predicates must be an RdbPredicates. 4. The columns must be a string array. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## restore

```TypeScript
restore(): Promise<void>
```

从副本关系型数据库文件恢复数据库，使用Promise异步回调。此接口仅供[HAMode](arkts-arkdata-relationalstore-hamode-e-sys.md)为MAIN_REPLICA时使用，且不支持在事务中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RdbStore-restore(): Promise<void>--><!--Device-RdbStore-restore(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch. |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800034 | SQLite: Library used incorrectly. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800015 | The database does not respond. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800024 | SQLite: The database file is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800026 | SQLite: The database is out of memory. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800030 | SQLite: Unable to open the database file. |

## retainDeviceData

```TypeScript
retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>
```

保留对应[单版本表模式](../../../database/data-sync-of-rdb-store.md#数据同步存储机制)分布式数据表中对应设备同步过来的数据，删除其他设备同步过来的数据，使用Promise异步回调。

不支持对[多设备协同表模式](../../../database/data-sync-of-rdb-store.md#数据同步存储机制)分布式数据表进行删除。

要删除数据越多，执行所需的时间越长。

> **说明：**
> 
> 入参允许为空，数据库表名对应的设备id列表也允许为空，但是数据库表名和设备id不允许为空字符串。
> 
> 入参如果为空，则删除当前数据库所有单版本分布式表中所有其他设备同步过来的数据。
> 
> 入参中如果数据库表名对应的设备id列表为空，则删除该表下所有其他设备同步过来的数据。
> 
> 保留本地写入以及传入设备id同步过来的数据，其他设备id同步过来的数据会被删除。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>--><!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| retainDevices | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;string&gt;&gt; | No | 指定要保留的分布式数据库表名和对应的设备id，无默认值，不传入则删除当前数据库中所有单版本分布式表中全量同步 数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800021 | SQLite: Generic error. |
| 14800024 | SQLite: The database file is locked. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800043 | The database does not support this scenario. Possible causes: 1. The database type is not supported;2. The table type is not supported; 3. This is a read-only database. |
| 14800042 | The database does not exist. Possible causes: 1. The database is deleted; &lt;br&gt;2. The database is not created. |
| 14800014 | The RdbStore or ResultSet is already closed. |

## unlockCloudContainer

```TypeScript
unlockCloudContainer(): Promise<void>
```

手动对应用云端数据库解锁，使用Promise异步回调。使用该接口需要实现云同步功能。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RdbStore-unlockCloudContainer(): Promise<void>--><!--Device-RdbStore-unlockCloudContainer(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |

## update

ArkTS-Dyn:
```TypeScript
update(
      table: string,
      values: ValuesBucket,
      predicates: dataSharePredicates.DataSharePredicates,
      callback: AsyncCallback<number>
    ): void
```

ArkTS-Sta:
```TypeScript
update(
      table: string,
      values: ValuesBucket,
      predicates: dataSharePredicates.DataSharePredicates,
      callback: AsyncCallback<long>
    ): void
```

根据DataSharePredicates的指定实例对象更新数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void--><!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的更新条件。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | 回调函数。返回受影响的行数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## update

ArkTS-Dyn:
```TypeScript
update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

ArkTS-Sta:
```TypeScript
update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>
```

根据DataSharePredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的  
[query](arkts-arkdata-relationalstore-rdbstore-i.md#query)或  
[querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysql)接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、  
[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | 指定的目标表名，不能为空字符串。 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | DataSharePredicates的实例对象指定的更新条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回受影响的行数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800033 | SQLite: Data type mismatch.<br>**Applicable version:** 12 and later |
| 14800000 | Inner error. |
| 14800032 | SQLite: Abort due to constraint violation.<br>**Applicable version:** 12 and later |
| 14800034 | SQLite: Library used incorrectly.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted.<br>**Applicable version:** 12 and later |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |
| 14800015 | The database does not respond.<br>**Applicable version:** 12 and later |
| 14800014 | The target instance is already closed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.<br>**Applicable version:** 12 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800025 | SQLite: A table in the database is locked.<br>**Applicable version:** 12 and later |
| 14800024 | SQLite: The database file is locked.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800026 | SQLite: The database is out of memory.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## updateDistributedInfo

ArkTS-Dyn:
```TypeScript
updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<number>
```

ArkTS-Sta:
```TypeScript
updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>
```

更新分布式信息，只支持单版本表模式，使用Promise异步回调。

不支持对多设备协同表模式分布式数据表进行更新。

要更新数据越多，执行所需的时间越长。

> **说明：**
> 
> 入参info中若要传入设备id信息，则设备id必须是已与当前设备建立网络连接的设备id。
> 
> 入参predicates中若要传入[ORIGIN_ORIDEVICE](arkts-arkdata-relationalstore-distributedfield-e-sys.md)，则只允许使用等于空或不等于空。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>--><!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [DistributedInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes | 指定要更新的分布式表的日志信息。 |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes | RdbPredicates的实例对象指定的查询条件。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回更新的数据个数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800021 | SQLite: Generic error. |
| 14800024 | SQLite: The database file is locked. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800043 | The database does not support this scenario. Possible causes: 1. The database type is not supported;2. The table type is not supported; 3. This is a read-only database. |
| 14800015 | The database does not respond. |
| 14800014 | The RdbStore or ResultSet is already closed. |

