# SingleKVStore

SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据端端同步完成的方法。在调用SingleKVStore的方法前，需要先通过 getKVStore 构建一个SingleKVStore实例。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## backup

```TypeScript
backup(file: string, callback: AsyncCallback<void>): void
```

以指定名称备份数据库到默认路径（context.databaseDir），使用callback异步回调。如需备份到自定义路径，请使用 [backupEx](#backupex)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## backup

```TypeScript
backup(file: string): Promise<void>
```

以指定名称备份数据库到默认路径（context.databaseDir），使用Promise异步回调。如需备份到自定义路径，请使用 [backupEx](#backupex)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## backupEx

```TypeScript
backupEx(backupConfig: BackupConfig): Promise<void>
```

以指定名称和路径备份数据库，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| backupConfig | [BackupConfig](arkts-arkdata-distributedkvstore-backupconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100000](../errorcode-distributedKVStore.md#15100000-无效的参数) |

## closeResultSet

```TypeScript
closeResultSet(resultSet: KVStoreResultSet, callback: AsyncCallback<void>): void
```

关闭由[SingleKVStore.getResultSet](#getresultset)返回的 KVStoreResultSet对象，使用callback异步回调。关闭结果集后，该结果集对象将不可再用，相关数据库资源被释放。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## closeResultSet

```TypeScript
closeResultSet(resultSet: KVStoreResultSet): Promise<void>
```

关闭由[SingleKVStore.getResultSet](#getresultset)返回的 KVStoreResultSet对象，使用Promise异步回调。关闭结果集后，该结果集对象将不可再用，相关数据库资源被释放。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## commit

```TypeScript
commit(callback: AsyncCallback<void>): void
```

提交SingleKVStore数据库中的事务，使用callback异步回调。需先调用 [startTransaction](#starttransaction)启动事务后再调 用本接口提交事务。提交成功后，事务期间的所有数据变更将永久生效并写入数据库。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## commit

```TypeScript
commit(): Promise<void>
```

提交SingleKVStore数据库中的事务，使用Promise异步回调。需先调用 [startTransaction](#starttransaction)启动事务后再调 用本接口提交事务。提交成功后，事务期间的所有数据变更将永久生效并写入数据库。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

从数据库中删除指定键值的数据，使用callback异步回调。删除成功后，指定键值对将被永久删除，无法再通过get等方法查询；若已订阅数据变更通知，将触发变更通知回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## delete

```TypeScript
delete(key: string): Promise<void>
```

从数据库中删除指定键值的数据，使用Promise异步回调。删除成功后，指定键值对将被永久删除，无法再通过get等方法查询；若已订阅数据变更通知，将触发变更通知回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## deleteBackup

```TypeScript
deleteBackup(files: Array<string>, callback: AsyncCallback<Array<[string, number]>>): void
```

根据指定名称从默认路径（context.databaseDir）删除备份文件，使用callback异步回调。删除备份文件后，将无法再通过 [restore](#restore)接口恢复该备份文件中的数据。如需从自定义路径删除备份，请使用 [deleteBackupEx](#deletebackupex)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## deleteBackup

```TypeScript
deleteBackup(files: Array<string>): Promise<Array<[string, number]>>
```

根据指定名称从默认路径（context.databaseDir）删除备份文件，使用Promise异步回调。删除备份文件后，将无法再通过 [restore](#restore)接口恢复该备份文件中的 数据。如需从自定义路径删除备份，请使用[deleteBackupEx](#deletebackupex)接口。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| files | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, number] & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## deleteBackupEx

```TypeScript
deleteBackupEx(backupConfig: BackupConfig): Promise<void>
```

根据指定名称和路径删除备份文件，使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| backupConfig | [BackupConfig](arkts-arkdata-distributedkvstore-backupconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100000](../errorcode-distributedKVStore.md#15100000-无效的参数) |

## deleteBatch

```TypeScript
deleteBatch(keys: string[], callback: AsyncCallback<void>): void
```

批量删除SingleKVStore数据库中的键值对，使用callback异步回调。删除成功后，指定键值对将被永久删除，无法再通过get等方法查询；若已订阅数据变更通知，将触发变更通知回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## deleteBatch

```TypeScript
deleteBatch(keys: string[]): Promise<void>
```

批量删除SingleKVStore数据库中的键值对，使用Promise异步回调。删除成功后，指定键值对将被永久删除，无法再通过get等方法查询；若已订阅数据变更通知，将触发变更通知回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## enableSync

```TypeScript
enableSync(enabled: boolean, callback: AsyncCallback<void>): void
```

设定是否开启端端同步，使用callback异步回调。开启端端同步后，数据库中的数据可在多设备间自动同步；关闭后则不会自动同步，需要手动调用 [sync](#sync)接口触发同步。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## enableSync

```TypeScript
enableSync(enabled: boolean): Promise<void>
```

设定是否开启端端同步，使用Promise异步回调。开启端端同步后，数据库中的数据可在多设备间自动同步；关闭后则不会自动同步，需要手动调用 [sync](#sync)接口触发同步。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## get

```TypeScript
get(key: string, callback: AsyncCallback<boolean | string | number | number | Uint8Array>): void
```

获取指定键的值，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean \| string \| number \| number \| Uint8Array & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |

## get

```TypeScript
get(key: string): Promise<boolean | string | number | number | Uint8Array>
```

获取指定键的值，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean \ | string \| number \| number \| Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |

## getEntries

```TypeScript
getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void
```

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(keyPrefix: string): Promise<Entry[]>
```

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(query: Query, callback: AsyncCallback<Entry[]>): void
```

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getEntries

```TypeScript
getEntries(query: Query): Promise<Entry[]>
```

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entry[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void
```

从SingleKVStore数据库中获取具有指定前缀的结果集，使用callback异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](#closeresultset) 关闭结果集释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSet

```TypeScript
getResultSet(keyPrefix: string): Promise<KVStoreResultSet>
```

从SingleKVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](#closeresultset) 关闭结果集释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyPrefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSet

```TypeScript
getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](#closeresultset) 关闭结果集释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSet

```TypeScript
getResultSet(query: Query): Promise<KVStoreResultSet>
```

获取与指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。获取结果集后，在使用完毕时需调用 [closeResultSet](#closeresultset) 关闭结果集释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getResultSize

```TypeScript
getResultSize(query: Query, callback: AsyncCallback<number>): void
```

获取与指定Query对象匹配的结果数，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |

## getResultSize

```TypeScript
getResultSize(query: Query): Promise<number>
```

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |

## getSecurityLevel

```TypeScript
getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void
```

获取数据库的安全级别，使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SecurityLevel&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## getSecurityLevel

```TypeScript
getSecurityLevel(): Promise<SecurityLevel>
```

获取数据库的安全级别，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;SecurityLevel & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## off

```TypeScript
off(event: 'dataChange', listener?: Callback<ChangeNotification>): void
```

取消订阅数据变更通知。必须先调用 on('dataChange') 订阅后，才能调用off取消订阅。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## off

```TypeScript
off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void
```

取消订阅端端同步完成事件回调通知。必须先调用 on('syncComplete') 订阅后，才能调用off取消订阅。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'syncComplete' | 是 |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void
```

订阅指定类型的数据变更通知。调用on订阅后，在不需要监听时必须调用 off('dataChange') 取消订阅。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100001](../errorcode-distributedKVStore.md#15100001-超过最大订阅数量或结果集数量) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## on

```TypeScript
on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void
```

订阅端端同步完成事件回调通知。调用on订阅后，在不需要监听时必须调用 off('syncComplete') 取消订阅。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'syncComplete' | 是 |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## put

```TypeScript
put(key: string, value: Uint8Array | string | number | number | boolean, callback: AsyncCallback<void>): void
```

添加指定类型键值对到数据库，使用callback异步回调。若Key已存在则更新对应Value；若已订阅数据变更通知，将触发变更通知回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | Uint8Array \| string \| number \| number \| boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## put

```TypeScript
put(key: string, value: Uint8Array | string | number | number | boolean): Promise<void>
```

添加指定类型键值对到数据库，使用Promise异步回调。若Key已存在则更新对应Value；若已订阅数据变更通知，将触发变更通知回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | Uint8Array \| string \| number \| number \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## putBatch

```TypeScript
putBatch(entries: Entry[], callback: AsyncCallback<void>): void
```

批量插入键值对到SingleKVStore数据库中，使用callback异步回调。若Key已存在则更新对应Value；若已订阅数据变更通知，将触发变更通知回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| entries | [Entry[]](arkts-arkdata-distributeddata-entry-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## putBatch

```TypeScript
putBatch(entries: Entry[]): Promise<void>
```

批量插入键值对到SingleKVStore数据库中，使用Promise异步回调。若Key已存在则更新对应Value；若已订阅数据变更通知，将触发变更通知回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| entries | [Entry[]](arkts-arkdata-distributeddata-entry-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## rekey

```TypeScript
rekey(): Promise<void>
```

更新数据库的加密密钥，使用Promise异步回调。

> **说明：**&gt;
> rekey仅对创建时已启用加密的数据库有效，即Options中encrypt需设置为true，非加密数据库调用此接口将返回错误。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [15100006](../errorcode-distributedKVStore.md#15100006-更新数据库加密密钥失败) |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void
```

删除指定设备的数据，使用callback异步回调。删除成功后，指定设备的所有数据将从本地数据库中永久移除，无法再通过get等方法查询该设备的数据。

> **说明：**&gt;
> 其中deviceId为[DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)中的
> networkId，通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](#sync)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string): Promise<void>
```

删除指定设备的数据，使用Promise异步回调。删除成功后，指定设备的所有数据将从本地数据库中永久移除，无法再通过get等方法查询该设备的数据。

> **说明：**&gt;
> 其中deviceId为[DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)中的
> networkId，通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](#sync)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## restore

```TypeScript
restore(file: string, callback: AsyncCallback<void>): void
```

从数据库默认路径（context.databaseDir）下指定名称的备份文件恢复数据库，使用callback异步回调。恢复成功后，当前数据库中的数据将被替换为备份文件中的数据，原有的未备份数据将丢失。如需从自定义路径恢复，请 使用[restoreEx](#restoreex)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## restore

```TypeScript
restore(file: string): Promise<void>
```

从数据库默认路径（context.databaseDir）下指定名称的备份文件恢复数据库，使用Promise异步回调。恢复成功后，当前数据库中的数据将被替换为备份文件中的数据，原有的未备份数据将丢失。如需从自定义路径恢复，请使 用[restoreEx](#restoreex)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## restoreEx

```TypeScript
restoreEx(backupConfig: BackupConfig): Promise<void>
```

从指定路径和名称的备份文件恢复数据库，使用Promise异步回调。恢复成功后，当前数据库中的数据将被替换为备份文件中的数据，原有的未备份数据将丢失。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| backupConfig | [BackupConfig](arkts-arkdata-distributedkvstore-backupconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100000](../errorcode-distributedKVStore.md#15100000-无效的参数) |

## rollback

```TypeScript
rollback(callback: AsyncCallback<void>): void
```

在SingleKVStore数据库中回滚事务，使用callback异步回调。需先调用 [startTransaction](#starttransaction)启动事务后再调 用本接口回滚事务。回滚成功后，事务期间的所有数据变更将被丢弃，不会写入数据库。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## rollback

```TypeScript
rollback(): Promise<void>
```

在SingleKVStore数据库中回滚事务，使用Promise异步回调。需先调用 [startTransaction](#starttransaction)启动事务后再调 用本接口回滚事务。回滚成功后，事务期间的所有数据变更将被丢弃，不会写入数据库。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |

## setSyncParam

```TypeScript
setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void
```

设置数据库端端同步允许的默认延时，使用callback异步回调。

> **说明：**&gt;
> 设置默认延时后，调用
> [sync](#sync)接口不会立即触发
> 端端同步，而是等待指定的延时时间后再执行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| defaultAllowedDelayMs | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSyncParam

```TypeScript
setSyncParam(defaultAllowedDelayMs: number): Promise<void>
```

设置数据库端端同步允许的默认延时，使用Promise异步回调。

> **说明：**&gt;
> 设置默认延时后，调用
> [sync](#sync)接口不会立即触发
> 端端同步，而是等待指定的延时时间后再执行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| defaultAllowedDelayMs | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSyncRange

```TypeScript
setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void
```

设置同步范围标签，使用callback异步回调。通过设置本地设备和远程设备的同步标签，决定哪些设备间可以进行数据同步。只有当本地设备的标签与远程设备的标签存在交集时，两端才允许同步数据。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localLabels | string[] | 是 |
| remoteSupportLabels | string[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSyncRange

```TypeScript
setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>
```

设置同步范围标签，使用Promise异步回调。通过设置本地设备和远程设备的同步标签，决定哪些设备间可以进行数据同步。只有当本地设备的标签与远程设备的标签存在交集时，两端才允许同步数据。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localLabels | string[] | 是 |
| remoteSupportLabels | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## startTransaction

```TypeScript
startTransaction(callback: AsyncCallback<void>): void
```

启动SingleKVStore数据库中的事务，使用callback异步回调。启动事务后，后续的数据库操作将纳入此事务范围，直到调用 [commit](#commit)提交或 [rollback](#rollback)回滚才会结束事务。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## startTransaction

```TypeScript
startTransaction(): Promise<void>
```

启动SingleKVStore数据库中的事务，使用Promise异步回调。启动事务后，后续的数据库操作将纳入此事务范围，直到调用 [commit](#commit)提交或 [rollback](#rollback)回滚才会结束事务。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15100005](../errorcode-distributedKVStore.md#15100005-数据库或查询结果集已关闭) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## sync

```TypeScript
sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void
```

在手动同步方式下，触发数据库端端同步。同步结果可通过订阅 on('syncComplete') 事件获取。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](../../../database/data-sync-of-kv-store.md)。

> **说明：**&gt;
> 其中deviceIds为[DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)中的
> networkId, 通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceIds | string[] | 是 |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| delayMs | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |

## sync

```TypeScript
sync(deviceIds: string[], query: Query, mode: SyncMode, delayMs?: number): void
```

在手动同步方式下，触发数据库端端同步，支持按查询条件过滤同步数据。同步结果可通过订阅 on('syncComplete') 事件获取。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](../../../database/data-sync-of-kv-store.md)。

> **说明：**&gt;
> 其中deviceIds为[DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)中的
> networkId, 通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceIds | string[] | 是 |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | 是 |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| delayMs | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15100003](../errorcode-distributedKVStore.md#15100003-数据库损坏) |
| [15100004](../errorcode-distributedKVStore.md#15100004-未找到相关数据) |
