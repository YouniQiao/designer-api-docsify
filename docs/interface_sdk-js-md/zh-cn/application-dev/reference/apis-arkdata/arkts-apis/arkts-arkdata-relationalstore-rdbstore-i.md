# RdbStore

提供管理关系数据库（RDB）方法的接口。在使用以下API前，请先通过[getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md)方法获取RdbStore实例，并使用该实例调用对应接口方法。在此基础上，建议优先使用[execute](#execute)方法完成数据库表结构和初始数据的 初始化，以确保相关接口调用的前置条件已满足。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## attach

```TypeScript
attach(fullPath: string, attachName: string, waitTime?: number) : Promise<number>
```

将一个数据库文件附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。数据库文件来自文件，且此API不支持附加加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullPath | string | 是 |
| attachName | string | 是 |
| waitTime | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800010](../errorcode-data-rdb.md#14800010-数据库路径不合法) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800016](../errorcode-data-rdb.md#14800016-数据库别名已被使用) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## attach

```TypeScript
attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number) : Promise<number>
```

将一个当前应用的数据库附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。此API不支持加密数据库附加非加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。除此之外，attach附加加密数据库时，可能受到并发的影响，出现解密失败的情况，报错14800011，需要显式指定加密参数并重试。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | 是 |
| attachName | string | 是 |
| waitTime | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800010](../errorcode-data-rdb.md#14800010-数据库路径不合法) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800016](../errorcode-data-rdb.md#14800016-数据库别名已被使用) |
| [14801001](../errorcode-data-rdb.md#14801001-上下文环境非stage模型) |
| [14801002](../errorcode-data-rdb.md#14801002-storeconfig中传入的datagroupid参数非法) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## backup

```TypeScript
backup(destName: string, callback: AsyncCallback<void>): void
```

以指定名称备份数据库，使用callback异步回调。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| destName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800010](../errorcode-data-rdb.md#14800010-数据库路径不合法) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## backup

```TypeScript
backup(destName: string): Promise<void>
```

以指定名称备份数据库，使用Promise异步回调。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| destName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

向目标表中插入一组数据，使用callback异步回调。接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md)策略写入，参数数量计算方式为插入 数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。从API version 20开始，支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array & lt;ValuesBucket & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

向目标表中插入一组数据，使用Promise异步回调。接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md)策略写入，参数数量计算方式为插入 数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。从API version 20开始，该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 9

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## batchInsertSync

```TypeScript
batchInsertSync(table: string, values: Array<ValuesBucket>): number
```

向目标表中插入一组数据。接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md)策略写入，参数数量计算方式为插入 数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## batchInsertWithConflictResolution

```TypeScript
batchInsertWithConflictResolution(
        table: string,
        values: Array<ValuesBucket>, 
        conflict: ConflictResolution
    ): Promise<number>
```

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)。使用Promise异步回调。单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 18

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## batchInsertWithConflictResolutionSync

```TypeScript
batchInsertWithConflictResolutionSync(
        table: string,
        values: Array<ValuesBucket>,
        conflict: ConflictResolution
    ): number
```

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)。单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 18

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## batchInsertWithReturning

```TypeScript
batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，返回 [Result](arkts-arkdata-relationalstore-result-i.md)。使用Promise异步回调。单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## batchInsertWithReturningSync

```TypeScript
batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，返回 [Result](arkts-arkdata-relationalstore-result-i.md)。单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## beginTrans

```TypeScript
beginTrans(): Promise<number>
```

在开始执行SQL语句之前，开始事务，使用Promise异步回调。与[beginTransaction](#begintransaction)的区别在于：该接口会返回事务ID， [execute](#execute)可以指定不同事务ID达到事务 隔离目的。该接口仅支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## beginTransaction

```TypeScript
beginTransaction(): void
```

在开始执行SQL语句之前，开始事务。此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void
```

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| cursor | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, callback: AsyncCallback<void>): void
```

清理云端删除的数据同步到本地后，未自动清理的所有数据。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, cursor?: number): Promise<void>
```

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据，使用Promise异步回调。若无cursor参数，将全部清理。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## close

```TypeScript
close(): Promise<void>
```

关闭数据库，使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void
```

主动执行对所有分布式表的端云同步，使用callback异步回调。使用该接口需要实现云服务功能。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>
```

主动执行对所有分布式表的端云同步，使用Promise异步回调。使用该接口需要实现云服务功能。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSync

```TypeScript
cloudSync(
      mode: SyncMode,
      tables: string[],
      progress: Callback<ProgressDetails>,
      callback: AsyncCallback<void>
    ): void
```

主动执行对指定表的端云同步，使用callback异步回调。使用该接口需要实现云服务功能。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | string[] | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>
```

主动执行对指定表的端云同步，使用Promise异步回调。使用该接口需要实现云服务功能。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | string[] | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## cloudSyncEx

```TypeScript
cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>
```

主动执行端云同步，根据云同步配置信息进行同步，使用Promise异步回调。使用该接口需要实现云服务功能。

> **说明：**&gt;
> [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i.md)中仅支持以下谓词：&gt;
> - [beginWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginwrap)&gt;
> - [endWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#endwrap)&gt;
> - [or](arkts-arkdata-relationalstore-rdbpredicates-c.md#or)&gt;
> - [and](arkts-arkdata-relationalstore-rdbpredicates-c.md#and)&gt;
> - 以下谓词的数据字段类型[ValueType](arkts-arkdata-relationalstore-valuetype-t.md)仅支持number类型的整数和string：&gt;
> - [equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)&gt;
> - [notEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#notequalto)&gt;
> - [in](arkts-arkdata-relationalstore-rdbpredicates-c.md#in)&gt;
> - [notIn](arkts-arkdata-relationalstore-rdbpredicates-c.md#notin)&gt;
> - 以下谓词的数据字段类型[ValueType](arkts-arkdata-relationalstore-valuetype-t.md)仅支持number类型的整数：&gt;
> - [greaterThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthan)&gt;
> - [lessThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthan)&gt;
> - [greaterThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthanorequalto)&gt;
> - [lessThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthanorequalto)&gt;
> 谓词中支持使用主键（必填）和资产（可选）作为同步条件：当选择资产作为同步条件时，同步模式需要设置为relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST；指定资产的数量较多时（最多支持
> 指定50个资产），建议谓词中仅使用主键作为同步条件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## commit

```TypeScript
commit(): void
```

提交已执行的SQL语句，跟[beginTransaction](#begintransaction)配合使用。此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## commit

```TypeScript
commit(txId : number): Promise<void>
```

提交已执行的SQL语句，跟[beginTrans](#begintrans)配合使用，使用Promise异步回调。该接口仅支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| txId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## createTransaction

```TypeScript
createTransaction(options?: TransactionOptions): Promise<Transaction>
```

创建一个事务对象并开始事务，使用Promise异步回调。与[beginTransaction](#begintransaction)的区别在于：createTransaction接口会返回一个事务对象，不同事务对象之间是隔 离的。使用事务对象进行插入、删除或更新数据等操作，无法被注册数据变更通知[on('dataChange')](#on)监听到。一个store最多支持同时存在四个事务对象，超过后会返回14800015错误码，此时需要检查是否持有事务对象时间过长或并发事务过多，若确认无法通过上述优化解决问题，建议等待现有事务释放后，再尝试新建事务对象。优先使用createTransaction，不再推荐使用beginTransaction。

**起始版本：** 14

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TransactionOptions](arkts-arkdata-relationalstore-transactionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Transaction](arkts-arkdata-relationalstore-transaction-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## delete

```TypeScript
delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

根据RdbPredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**起始版本：** 9

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## deleteSync

```TypeScript
deleteSync(predicates: RdbPredicates): number
```

根据RdbPredicates的指定实例对象从数据库中删除数据。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## deleteWithReturning

```TypeScript
deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>
```

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-arkdata-relationalstore-result-i.md)，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## deleteWithReturningSync

```TypeScript
deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result
```

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-arkdata-relationalstore-result-i.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## detach

```TypeScript
detach(attachName: string, waitTime?: number) : Promise<number>
```

将附加的数据库从当前数据库中分离，使用Promise异步回调。当所有的附加的数据库被分离后，数据库会重新切换为WAL模式。在detach之前，所有的数据库操作要确保已经结束，所有的ResultSet已经Close。并且不能并发调用，可能出现未响应情况，需要重试。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attachName | string | 是 |
| waitTime | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## emit

```TypeScript
emit(event: string): void
```

通知通过[on](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/apis-arkdata/arkts-apis-data-relationalStore-RdbStore.md#on10)注册的进程间或者进程内监听事件。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800050](../errorcode-data-rdb.md#14800050-获取订阅服务失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## execute

```TypeScript
execute(sql: string, args?: Array<ValueType>): Promise<ValueType>
```

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType，使用Promise异步回调。该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。此接口不支持执行查询、附加数据库和事务操作，可以使用 [querySql](#querysql)、 [query](#query)、 [attach](#attach)、 [beginTransaction](#begintransaction)、 [commit](#commit)等接口代替。向量数据库使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持部分字段插入。不支持分号分隔的多条语句。不支持开头包含注释的语句。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## execute

```TypeScript
execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>
```

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。该接口仅支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持 部分字段插入。此接口不支持执行查询，可以使用 [querySql](#querysql)接口代替。不支持分号分隔的多条语句。不支持开头包含注释的语句。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| txId | number | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ValueType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## executeSql

```TypeScript
executeSql(sql: string, callback: AsyncCallback<void>): void
```

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。此接口不支持执行查询、附加数据库和事务操作，可以使用 [querySql](#querysql)、 [query](#query)、 [attach](#attach)、 [beginTransaction](#begintransaction)、 [commit](#commit)等接口代替。不支持分号分隔的多条语句。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void
```

执行指定的SQL语句，支持传入SQL语句中参数的值，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。此接口不支持执行查询、附加数据库和事务操作，可以使用 [querySql](#querysql)、 [query](#query)、 [attach](#attach)、 [beginTransaction](#begintransaction)、 [commit](#commit)等接口代替。不支持分号分隔的多条语句。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>
```

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。此接口不支持执行查询、附加数据库和事务操作，可以使用 [querySql](#querysql)、 [query](#query)、 [attach](#attach)、 [beginTransaction](#begintransaction)、 [commit](#commit)等接口代替。不支持分号分隔的多条语句。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## executeSync

```TypeScript
executeSync(sql: string, args?: Array<ValueType>): ValueType
```

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType。该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。此接口不支持执行查询、附加数据库和事务操作，可以使用 [querySql](#querysql)、 [query](#query)、 [attach](#attach)、 [beginTransaction](#begintransaction)、 [commit](#commit)等接口代替。不支持分号分隔的多条语句。不支持开头包含注释的语句。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## getModifyTime

```TypeScript
getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>
```

获取数据库表中数据的最后修改时间，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| columnName | string | 是 |
| primaryKeys | [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## getModifyTime

```TypeScript
getModifyTime(
      table: string,
      columnName: string,
      primaryKeys: PRIKeyType[],
      callback: AsyncCallback<ModifyTime>
    ): void
```

获取数据库表中数据的最后修改时间，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| columnName | string | 是 |
| primaryKeys | [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md)[] | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void
```

向目标表中插入一行数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>): void
```

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket): Promise<number>
```

向目标表中插入一行数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<number>
```

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## insertSync

```TypeScript
insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number
```

向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 12

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
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## insertSync

```TypeScript
insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number
```

传入Sendable数据，向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | sendableRelationalStore.ValuesBucket | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## lockRow

```TypeScript
lockRow(predicates: RdbPredicates): Promise<void>
```

根据RdbPredicates的指定实例对象从数据库中锁定数据，锁定数据不执行端云同步，使用Promise异步回调。该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。该接口不支持对已删除数据的操作。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800018](../errorcode-data-rdb.md#14800018-查询结果没有数据符合条件) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void
```

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用callback异步回调。

> **说明：**&gt;
> 其中device通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | string | 是 |
| table | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string): Promise<string>
```

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用Promise异步回调。

> **说明：**&gt;
> 其中device通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

取消数据变更的事件监听。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(
      event: 'dataChange',
      type: SubscribeType,
      observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>
    ): void
```

取消数据变更的事件监听。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: string, interProcess: boolean, observer?: Callback<void>): void
```

取消数据库的进程内或者进程间事件监听。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| interProcess | boolean | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800050](../errorcode-data-rdb.md#14800050-获取订阅服务失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void
```

取消订阅自动同步进度的通知。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'autoSyncProgress' | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: 'statistics', observer?: Callback<SqlExecutionInfo> ): void
```

取消订阅SQL统计信息。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'statistics' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void
```

取消订阅SQL统计信息。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'perfStat' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## off

```TypeScript
off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void
```

停止记录SQL执行过程中的异常日志。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'sqliteErrorOccurred' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

注册数据库的数据变更的事件监听。当分布式数据库中的数据发生更改时，将调用回调。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void
```

注册数据库的数据变更的事件监听。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: string, interProcess: boolean, observer: Callback<void>): void
```

注册数据库的进程内或者进程间事件监听。当调用emit接口时，将调用回调。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| interProcess | boolean | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800050](../errorcode-data-rdb.md#14800050-获取订阅服务失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void
```

在已打开端云同步，并且网络状态正常的条件下，注册自动同步进度通知，自动同步进行时调用回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'autoSyncProgress' | 是 |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'statistics', observer: Callback<SqlExecutionInfo> ): void
```

订阅SQL统计信息。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'statistics' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void
```

订阅SQL统计信息。使用[createTransaction](#createtransaction)创建的事务进行相关操作（ [Transaction](arkts-arkdata-relationalstore-transaction-i.md)），只会在事务结束（COMMIT/ROLLBACK）时通知一次统计信息。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'perfStat' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## on

```TypeScript
on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void
```

记录执行SQL语句时的异常日志。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'sqliteErrorOccurred' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## query

```TypeScript
query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void
```

根据指定条件查询数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## query

```TypeScript
query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

根据指定条件查询数据库中的数据，支持指定要查询的列，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用 [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、[getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法 时将无法成功获取数据，并可能导致操作失败或抛出异常。

**起始版本：** 9

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## queryByStep

```TypeScript
queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符不超过1000个，使用Promise异步回调。该接口按行逐步获取结果，不存在2MB的单条数据大小限制。聚合函数不支持嵌套使用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## queryByStep

```TypeScript
queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据指定条件查询数据库中的数据，使用Promise异步回调。该接口按行逐步获取结果，不存在2MB的单条数据大小限制。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## queryLockedRow

```TypeScript
queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

根据指定条件查询数据库中锁定的数据，使用Promise异步回调。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## querySql

```TypeScript
querySql(sql: string, callback: AsyncCallback<ResultSet>): void
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此 限制，使用此接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用，当前支持的语法见 [规格限制](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/database/data-persistence-by-vector-store.md#规格限制)。聚合函数不支持嵌套使用。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## querySql

```TypeScript
querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，支持传入SQL语句中参数的值，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格 小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用，当前支持的语法见 [规格限制](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/database/data-persistence-by-vector-store.md#规格限制)。聚合函数不支持嵌套使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## querySql

```TypeScript
querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限 制，使用此接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用，当前支持的语法见 [规格限制](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/database/data-persistence-by-vector-store.md#规格限制)。聚合函数不支持嵌套使用。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## querySqlSync

```TypeScript
querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet
```

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤 放到[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md)线程中执行。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |
| bindArgs | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## querySqlWithoutRowCount

```TypeScript
querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>
```

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于 [querySql](#querysql)接口。SQL语句中的各种表达式和操作符之 间的关系操作符号不超过1000个。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySqlWithoutRowCountSync

```TypeScript
querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet
```

根据指定SQL语句查询数据库中的数据，查询时不计算行数。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对querySqlWithoutRowCountSync同步接口获得的LiteResultSet进行操 作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md)线程中执行。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## querySync

```TypeScript
querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet
```

根据指定条件查询数据库中的数据。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到 [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md)线程中执行。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |

## queryWithoutRowCount

```TypeScript
queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>
```

根据指定条件查询数据库中的数据，查询时不计算行数，性能优于 [query](#query)接口。使用Promise异步回 调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## queryWithoutRowCountSync

```TypeScript
queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet
```

根据指定条件查询数据库中的数据，查询时不计算行数。对queryWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到 [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md)线程中执行。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## rekey

```TypeScript
rekey(cryptoParam?: CryptoParam): Promise<void>
```

手动更新加密数据库的密钥。使用Promise异步回调。从API版本26.0.0开始，支持使用该接口更新向量数据库（创建数据库时配置StoreConfig的vector字段为true）的密钥。仅支持加密数据库进行密钥更新，不支持非加密数据库变加密数据库及加密数据库变非加密数据库，且需要保持加密参数和密钥生成方式与建库时一致。不支持对非WAL模式的数据库进行密钥更新。手动更新密钥时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会引发失败。数据库越大，密钥更新所需的时间越长。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cryptoParam](arkts-arkdata-relationalstore-storeconfig-i.md) | [CryptoParam](arkts-arkdata-relationalstore-cryptoparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |

## rekeyEx

```TypeScript
rekeyEx(cryptoParam: CryptoParam): Promise<void>
```

手动更新数据库的密钥或加密参数，使用Promise异步回调。不支持对非WAL模式的数据库进行密钥更新。手动更新时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会导致更新失败。支持加密数据库的参数更新，以及加密数据库与非加密数据库之间的相互转换。数据库越大，执行更新所需的时间越长。

> **说明：**&gt;
> 加密参数变更需谨慎，在完成rekeyEx操作后，getRdbStore时必须使用新的参数来打开数据库，否则可能会导致开库失败。&gt;
> 如果rekey过程因设备断电等原因中断，操作可能成功也可能失败。因此，建议业务方做好兜底保障（使用RekeyEx前后的参数进行冗余重试），确保不会错误地判断数据库的状态，从而避免出现数据库无法打开的问题。&gt;
> 如果有加密参数变更，不建议getRdbStore时使用AllowedRebuild参数，防止因为传入的错误加密参数导致数据库发生重建。

**起始版本：** 22

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cryptoParam](arkts-arkdata-relationalstore-storeconfig-i.md) | [CryptoParam](arkts-arkdata-relationalstore-cryptoparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |

## remoteQuery

```TypeScript
remoteQuery(
      device: string,
      table: string,
      predicates: RdbPredicates,
      columns: Array<string>,
      callback: AsyncCallback<ResultSet>
    ): void
```

根据指定条件查询远程设备数据库中的数据。使用callback异步回调。

> **说明：**&gt;
> 其中device通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | string | 是 |
| table | string | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## remoteQuery

```TypeScript
remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>
```

根据指定条件查询远程设备数据库中的数据。使用Promise异步回调。

> **说明：**&gt;
> 其中device通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | string | 是 |
| table | string | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| columns | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## restore

```TypeScript
restore(srcName: string, callback: AsyncCallback<void>): void
```

从指定的数据库备份文件恢复数据库，使用callback异步回调。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## restore

```TypeScript
restore(srcName: string): Promise<void>
```

从指定的数据库备份文件恢复数据库，使用Promise异步回调。该接口支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## rollBack

```TypeScript
rollBack(): void
```

回滚已经执行的SQL语句。此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## rollback

```TypeScript
rollback(txId : number): Promise<void>
```

回滚已经执行的SQL语句，跟[beginTrans](#begintrans)配合使用，使用Promise异步回调。该接口仅支持向量数据库（在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置vector为true）使用。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| txId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void
```

设置分布式数据库表，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>): Promise<void>
```

设置分布式数据库表，使用Promise异步回调。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void
```

设置分布式数据库表，支持指定表的分布式类型，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800051](../errorcode-data-rdb.md#14800051-分布式表类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## setDistributedTables

```TypeScript
setDistributedTables(
      tables: Array<string>,
      type: DistributedType,
      config: DistributedConfig,
      callback: AsyncCallback<void>
    ): void
```

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | 是 |
| config | [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800051](../errorcode-data-rdb.md#14800051-分布式表类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>
```

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | 是 |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | 否 |
| config | [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800051](../errorcode-data-rdb.md#14800051-分布式表类型不匹配) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## setLocale

```TypeScript
setLocale(locale: string) : Promise<void>
```

设置自定义排序的语言。使用Promise异步回调。该值符合ISO 639标准，但是仅支持ICU中的部分语言，对于不支持的语言，设置自定义排序的语言时会报错14800001。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## stopCloudSync

```TypeScript
stopCloudSync(): Promise<void>
```

停止与云端的数据同步，使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void
```

在设备之间同步数据，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>
```

在设备之间同步数据，使用Promise异步回调。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## syncEx

```TypeScript
syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>
```

在设备之间同步数据，使用Promise异步回调，可以返回具体的同步状态信息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;SyncResult & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |

## unlockRow

```TypeScript
unlockRow(predicates: RdbPredicates): Promise<void>
```

根据RdbPredicates的指定实例对象从数据库中解锁数据，使用Promise异步回调。该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。该接口不支持对已删除数据的操作。

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800018](../errorcode-data-rdb.md#14800018-查询结果没有数据符合条件) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

根据RdbPredicates的指定实例对象更新数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## update

```TypeScript
update(
      values: ValuesBucket,
      predicates: RdbPredicates,
      conflict: ConflictResolution,
      callback: AsyncCallback<number>
    ): void
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式 [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<number>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式 [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | 是 |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | 是 |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |

## updateSync

```TypeScript
updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number
```

根据RdbPredicates的指定实例对象更新数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的 [query](#query) 或 [querySql](#querysql) 接口获取ResultSet后，调用[getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue)、 [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。如需读取超过2MB的数据，请使用 [queryByStep](#querybystep)接口。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14800000](../errorcode-data-rdb.md#14800000-内部错误) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800015](../errorcode-data-rdb.md#14800015-数据库没有响应) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite异步回调请求被中止) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite访问权限被拒绝) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite数据库内存不足) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlitetext或blob超出大小限制) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800034](../errorcode-data-rdb.md#14800034-sqlite库使用不正确) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## updateWithReturning

```TypeScript
updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式 [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，返回[Result](arkts-arkdata-relationalstore-result-i.md)，使用Promise 异步回调。conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## updateWithReturningSync

```TypeScript
updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式 [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md)，返回[Result](arkts-arkdata-relationalstore-result-i.md)。conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800014](../errorcode-data-rdb.md#14800014-目标实例已关闭) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite数据库文件已锁定) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite数据库中的表被锁定) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite由于违反约束而中止) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite数据类型不匹配) |
| [14800047](../errorcode-data-rdb.md#14800047-wal文件大小超过默认上限) |

## rebuilt

```TypeScript
rebuilt: RebuildType
```

rebuilt: [RebuildType](arkts-arkdata-relationalstore-rebuildtype-e.md)用于获取数据库是否进行过重建或修复。

**类型：** [RebuildType](arkts-arkdata-relationalstore-rebuildtype-e.md)

**起始版本：** 12

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## version

```TypeScript
version: number
```

version: int设置和获取数据库版本，值为正整数。读取和设置version属性会占用数据库连接，避免对该属性进行频繁操作。使用临时变量保存读取到的version值，在数据库变更完成后将其赋值给RdbStore实例的version属性。数据库升 级时变更version属性的场景，请参考[开发步骤](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/database/data-persistence-by-rdb-store.md#开发步骤)。

**类型：** number

**起始版本：** 10

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core
