# @ohos.data.relationalStore(关系型数据库)

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。支持通过[ResultSet.getSendableRow](arkts-arkdata-relationalstore-resultset-i.md#getsendablerow)方法获取Sendable数据，进行跨线程传递。

为保证插入并读取数据成功，建议一条数据不超过2MB。如果数据超过2MB，插入操作将成功，读取操作将失败。

大数据量场景下查询数据可能会导致耗时长甚至应用卡死，如有相关操作可参考文档[批量数据写数据库场景](../../../arkts-utils/batch-database-operations-guide.md)，且有建议如下：

- 单次查询数据量不超过5000条。  
- 在[TaskPool](../../apis-arkts/arkts-apis/arkts-taskpool.md/arkts-taskpool.md)中查询。  
- 拼接SQL语句尽量简洁。  
- 合理地分批次查询。

该模块提供以下关系型数据库相关的常用功能：

- [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的谓词，主要用来定义数据库的操作条件。  
- [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md)：提供管理关系数据库（RDB）方法的接口。  
- [ResultSet](arkts-arkdata-relationalstore-resultset-i.md)：提供用户调用关系型数据库查询接口之后返回的结果集合。  
- [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)：提供用户调用关系型数据库  
[queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querywithoutrowcount)、  
[querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount)等查询接口之后返回的结果集合。与  
[ResultSet](arkts-arkdata-relationalstore-resultset-i.md)相比，LiteResultSet不包含查询结果的总行数信息。  
- [Transaction](arkts-arkdata-relationalstore-transaction-i.md)：提供管理事务对象的接口。

**起始版本：** 9

<!--Device-unnamed-declare namespace relationalStore--><!--Device-unnamed-declare namespace relationalStore-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 汇总

### 函数

| 名称 |
| --- |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore-1) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore-2) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore-3) |
| [getDeleteSqlInfo](arkts-arkdata-relationalstore-getdeletesqlinfo-f.md#getdeletesqlinfo) |
| [getInsertSqlInfo](arkts-arkdata-relationalstore-getinsertsqlinfo-f.md#getinsertsqlinfo) |
| [getQuerySqlInfo](arkts-arkdata-relationalstore-getquerysqlinfo-f.md#getquerysqlinfo) |
| [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore) | 创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用callback异步回调。  对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。  开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \|  \| ------- \| -------------------------------- \| ---- \|  \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \|  \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore-1) | 创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。  对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。  开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \|  \| ------- \| -------------------------------- \| ---- \|  \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \|  \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getRdbStoreSync](arkts-arkdata-relationalstore-getrdbstoresync-f.md#getrdbstoresync) | 创建或打开已有的关系型数据库。开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。这是一个同步方法，会阻塞线程直到获取到RdbStore。  对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。  开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。如果有修改参数，则会报错误码。  \| 当前打开数据库时配置的加密类型 \| 本设备上创建该数据库时的加密类型 \| 结果 \|  \| ------- \| -------------------------------- \| ---- \|  \| 非加密 \| 加密 \| 使用加密配置（encrypt=true）打开数据库。 \|  \| 加密 \| 非加密 \| 使用非加密配置（encrypt=false）打开数据库。 \|
| [getUpdateSqlInfo](arkts-arkdata-relationalstore-getupdatesqlinfo-f.md#getupdatesqlinfo) |
| [isTokenizerSupported](arkts-arkdata-relationalstore-istokenizersupported-f.md#istokenizersupported) |
| [isVectorSupported](arkts-arkdata-relationalstore-isvectorsupported-f.md#isvectorsupported) |

### 类

| 名称 |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [Asset](arkts-arkdata-relationalstore-asset-i.md) |
| [ChangeInfo](arkts-arkdata-relationalstore-changeinfo-i.md) |
| [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i.md) |
| [CryptoParam](arkts-arkdata-relationalstore-cryptoparam-i.md) |
| [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i.md) |
| [ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md) |
| [ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md) |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md) |
| [Result](arkts-arkdata-relationalstore-result-i.md) |
| [ResultSet](arkts-arkdata-relationalstore-resultset-i.md) |
| [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) |
| [SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md) |
| [SqlInfo](arkts-arkdata-relationalstore-sqlinfo-i.md) |
| [Statistic](arkts-arkdata-relationalstore-statistic-i.md) |
| [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) |
| [SyncResult](arkts-arkdata-relationalstore-syncresult-i.md) |
| [TableDetails](arkts-arkdata-relationalstore-tabledetails-i.md) |
| [Transaction](arkts-arkdata-relationalstore-transaction-i.md) |
| [TransactionOptions](arkts-arkdata-relationalstore-transactionoptions-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i-sys.md) |
| [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i-sys.md) |
| [DistributedInfo](arkts-arkdata-relationalstore-distributedinfo-i-sys.md) |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i-sys.md) |
| [Reference](arkts-arkdata-relationalstore-reference-i-sys.md) |
| [ResultSet](arkts-arkdata-relationalstore-resultset-i-sys.md) |
| [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AssetConflictPolicy](arkts-arkdata-relationalstore-assetconflictpolicy-e.md) |
| [AssetStatus](arkts-arkdata-relationalstore-assetstatus-e.md) |
| [ChangeType](arkts-arkdata-relationalstore-changetype-e.md) |
| [ColumnType](arkts-arkdata-relationalstore-columntype-e.md) |
| [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md) |
| [DistributedTableType](arkts-arkdata-relationalstore-distributedtabletype-e.md) |
| [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) |
| [EncryptionAlgo](arkts-arkdata-relationalstore-encryptionalgo-e.md) |
| [Field](arkts-arkdata-relationalstore-field-e.md) |
| [HmacAlgo](arkts-arkdata-relationalstore-hmacalgo-e.md) |
| [KdfAlgo](arkts-arkdata-relationalstore-kdfalgo-e.md) |
| [Origin](arkts-arkdata-relationalstore-origin-e.md) |
| [Progress](arkts-arkdata-relationalstore-progress-e.md) |
| [ProgressCode](arkts-arkdata-relationalstore-progresscode-e.md) |
| [RebuildType](arkts-arkdata-relationalstore-rebuildtype-e.md) |
| [SecurityLevel](arkts-arkdata-relationalstore-securitylevel-e.md) |
| [SubscribeType](arkts-arkdata-relationalstore-subscribetype-e.md) |
| [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) |
| [SyncResultCode](arkts-arkdata-relationalstore-syncresultcode-e.md) |
| [Tokenizer](arkts-arkdata-relationalstore-tokenizer-e.md) |
| [TransactionType](arkts-arkdata-relationalstore-transactiontype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DistributedField](arkts-arkdata-relationalstore-distributedfield-e-sys.md) |
| [DistributedOrigin](arkts-arkdata-relationalstore-distributedorigin-e-sys.md) |
| [HAMode](arkts-arkdata-relationalstore-hamode-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [Assets](arkts-arkdata-relationalstore-assets-t.md) |
| [ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md) |
| [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md) |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) |
| [RowsData](arkts-arkdata-relationalstore-rowsdata-t.md) |
| [UTCTime](arkts-arkdata-relationalstore-utctime-t.md) |
| [ValueType](arkts-arkdata-relationalstore-valuetype-t.md) |
| [ValuesBucket](arkts-arkdata-relationalstore-valuesbucket-t.md) |
