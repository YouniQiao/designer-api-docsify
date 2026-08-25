# @ohos.data.relationalStore(关系型数据库)

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户 输入的SQL语句来满足复杂的场景需要。支持通过[ResultSet.getSendableRow](arkts-arkdata-relationalstore-resultset-i.md#getsendablerow)方法获取Sendable数据，进行跨线程 传递。为保证插入并读取数据成功，建议一条数据不超过2MB。如果数据超过2MB，插入操作将成功，读取操作将失败。大数据量场景下查询数据可能会导致耗时长甚至应用卡死，如有相关操作可参考文档[批量数据写数据库场景](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/arkts-utils/batch-database-operations-guide.md)，且有建议如下：  
- 单次查询数据量不超过5000条。  
- 在[TaskPool](../../apis-arkts/arkts-apis/arkts-taskpool.md)中查询。  
- 拼接SQL语句尽量简洁。  
- 合理地分批次查询。  
该模块提供以下关系型数据库相关的常用功能：  
- [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的谓词，主要用来定义数据库的操作条件。  
- [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md)：提供管理关系数据库（RDB）方法的接口。  
- [ResultSet](arkts-arkdata-relationalstore-resultset-i.md)：提供用户调用关系型数据库查询接口之后返回的结果集合。  
- [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)：提供用户调用关系型数据库  
[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querywithoutrowcount)、 [querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount)等查询接口之后返回的结果集合。与 [ResultSet](arkts-arkdata-relationalstore-resultset-i.md)相比，LiteResultSet不包含查询结果的总行数信息。  
- [Transaction](arkts-arkdata-relationalstore-transaction-i.md)：提供管理事务对象的接口。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [deleteRdbStore(关系型数据库)](arkts-arkdata-relationalstore-deleterdbstore-f.md) |
| [deleteRdbStore(关系型数据库)](arkts-arkdata-relationalstore-deleterdbstore-f.md) |
| [deleteRdbStore(关系型数据库)](arkts-arkdata-relationalstore-deleterdbstore-f.md) |
| [deleteRdbStore(关系型数据库)](arkts-arkdata-relationalstore-deleterdbstore-f.md) |
| [getDeleteSqlInfo(关系型数据库)](arkts-arkdata-relationalstore-getdeletesqlinfo-f.md) |
| [getInsertSqlInfo(关系型数据库)](arkts-arkdata-relationalstore-getinsertsqlinfo-f.md) |
| [getQuerySqlInfo(关系型数据库)](arkts-arkdata-relationalstore-getquerysqlinfo-f.md) |
| [getRdbStore(关系型数据库)](arkts-arkdata-relationalstore-getrdbstore-f.md) | 创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用callback异步回调。对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \| \| ------- \| -------------------------------- \| ---- \| \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \| \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getRdbStore(关系型数据库)](arkts-arkdata-relationalstore-getrdbstore-f.md) | 创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \| \| ------- \| -------------------------------- \| ---- \| \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \| \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getRdbStoreSync(关系型数据库)](arkts-arkdata-relationalstore-getrdbstoresync-f.md) | 创建或打开已有的关系型数据库。开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。这是一个同步方法，会阻塞线程直到获取到RdbStore。对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。如果有修改参数，则会报错误码。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \| \| ------- \| -------------------------------- \| ---- \| \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \| \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getUpdateSqlInfo(关系型数据库)](arkts-arkdata-relationalstore-getupdatesqlinfo-f.md) |
| [isTokenizerSupported(关系型数据库)](arkts-arkdata-relationalstore-istokenizersupported-f.md) |
| [isVectorSupported(关系型数据库)](arkts-arkdata-relationalstore-isvectorsupported-f.md) |

### 类

| 名称 |
| --- |
| [LiteResultSet(关系型数据库)](arkts-arkdata-relationalstore-literesultset-c.md) |
| [RdbPredicates(关系型数据库)](arkts-arkdata-relationalstore-rdbpredicates-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [LiteResultSet(关系型数据库)](arkts-arkdata-relationalstore-literesultset-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [Asset(关系型数据库)](arkts-arkdata-relationalstore-asset-i.md) |
| [ChangeInfo(关系型数据库)](arkts-arkdata-relationalstore-changeinfo-i.md) |
| [CloudSyncConfig(关系型数据库)](arkts-arkdata-relationalstore-cloudsyncconfig-i.md) |
| [CryptoParam(关系型数据库)](arkts-arkdata-relationalstore-cryptoparam-i.md) |
| [DistributedConfig(关系型数据库)](arkts-arkdata-relationalstore-distributedconfig-i.md) |
| [ExceptionMessage(关系型数据库)](arkts-arkdata-relationalstore-exceptionmessage-i.md) |
| [ProgressDetails(关系型数据库)](arkts-arkdata-relationalstore-progressdetails-i.md) |
| [RdbStore(关系型数据库)](arkts-arkdata-relationalstore-rdbstore-i.md) |
| [Result(关系型数据库)](arkts-arkdata-relationalstore-result-i.md) |
| [ResultSet(关系型数据库)](arkts-arkdata-relationalstore-resultset-i.md) |
| [ReturningConfig(关系型数据库)](arkts-arkdata-relationalstore-returningconfig-i.md) |
| [SqlExecutionInfo(关系型数据库)](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md) |
| [SqlInfo(关系型数据库)](arkts-arkdata-relationalstore-sqlinfo-i.md) |
| [Statistic(关系型数据库)](arkts-arkdata-relationalstore-statistic-i.md) |
| [StoreConfig(关系型数据库)](arkts-arkdata-relationalstore-storeconfig-i.md) |
| [SyncResult(关系型数据库)](arkts-arkdata-relationalstore-syncresult-i.md) |
| [TableDetails(关系型数据库)](arkts-arkdata-relationalstore-tabledetails-i.md) |
| [Transaction(关系型数据库)](arkts-arkdata-relationalstore-transaction-i.md) |
| [TransactionOptions(关系型数据库)](arkts-arkdata-relationalstore-transactionoptions-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CloudSyncConfig(关系型数据库)](arkts-arkdata-relationalstore-cloudsyncconfig-i-sys.md) |
| [DistributedConfig(关系型数据库)](arkts-arkdata-relationalstore-distributedconfig-i-sys.md) |
| [DistributedInfo(关系型数据库)](arkts-arkdata-relationalstore-distributedinfo-i-sys.md) |
| [RdbStore(关系型数据库)](arkts-arkdata-relationalstore-rdbstore-i-sys.md) |
| [Reference(关系型数据库)](arkts-arkdata-relationalstore-reference-i-sys.md) |
| [ResultSet(关系型数据库)](arkts-arkdata-relationalstore-resultset-i-sys.md) |
| [StoreConfig(关系型数据库)](arkts-arkdata-relationalstore-storeconfig-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AssetConflictPolicy(关系型数据库)](arkts-arkdata-relationalstore-assetconflictpolicy-e.md) |
| [AssetStatus(关系型数据库)](arkts-arkdata-relationalstore-assetstatus-e.md) |
| [ChangeType(关系型数据库)](arkts-arkdata-relationalstore-changetype-e.md) |
| [ColumnType(关系型数据库)](arkts-arkdata-relationalstore-columntype-e.md) |
| [ConflictResolution(关系型数据库)](arkts-arkdata-relationalstore-conflictresolution-e.md) |
| [DistributedTableType(关系型数据库)](arkts-arkdata-relationalstore-distributedtabletype-e.md) |
| [DistributedType(关系型数据库)](arkts-arkdata-relationalstore-distributedtype-e.md) |
| [EncryptionAlgo(关系型数据库)](arkts-arkdata-relationalstore-encryptionalgo-e.md) |
| [Field(关系型数据库)](arkts-arkdata-relationalstore-field-e.md) |
| [HmacAlgo(关系型数据库)](arkts-arkdata-relationalstore-hmacalgo-e.md) |
| [KdfAlgo(关系型数据库)](arkts-arkdata-relationalstore-kdfalgo-e.md) |
| [Origin(关系型数据库)](arkts-arkdata-relationalstore-origin-e.md) |
| [Progress(关系型数据库)](arkts-arkdata-relationalstore-progress-e.md) |
| [ProgressCode(关系型数据库)](arkts-arkdata-relationalstore-progresscode-e.md) |
| [RebuildType(关系型数据库)](arkts-arkdata-relationalstore-rebuildtype-e.md) |
| [SecurityLevel(关系型数据库)](arkts-arkdata-relationalstore-securitylevel-e.md) |
| [SubscribeType(关系型数据库)](arkts-arkdata-relationalstore-subscribetype-e.md) |
| [SyncMode(关系型数据库)](arkts-arkdata-relationalstore-syncmode-e.md) |
| [SyncResultCode(关系型数据库)](arkts-arkdata-relationalstore-syncresultcode-e.md) |
| [Tokenizer(关系型数据库)](arkts-arkdata-relationalstore-tokenizer-e.md) |
| [TransactionType(关系型数据库)](arkts-arkdata-relationalstore-transactiontype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DistributedField(关系型数据库)](arkts-arkdata-relationalstore-distributedfield-e-sys.md) |
| [DistributedOrigin(关系型数据库)](arkts-arkdata-relationalstore-distributedorigin-e-sys.md) |
| [HAMode(关系型数据库)](arkts-arkdata-relationalstore-hamode-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [Assets(关系型数据库)](arkts-arkdata-relationalstore-assets-t.md) |
| [ModifyTime(关系型数据库)](arkts-arkdata-relationalstore-modifytime-t.md) |
| [PRIKeyType(关系型数据库)](arkts-arkdata-relationalstore-prikeytype-t.md) |
| [RowData(关系型数据库)](arkts-arkdata-relationalstore-rowdata-t.md) |
| [RowsData(关系型数据库)](arkts-arkdata-relationalstore-rowsdata-t.md) |
| [UTCTime(关系型数据库)](arkts-arkdata-relationalstore-utctime-t.md) |
| [ValuesBucket(关系型数据库)](arkts-arkdata-relationalstore-valuesbucket-t.md) |
| [ValueType(关系型数据库)](arkts-arkdata-relationalstore-valuetype-t.md) |
