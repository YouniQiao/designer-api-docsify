# @ohos.data.relationalStore

The relational database (RDB) manages data based on relational models. The **relationalStore** module provides a complete mechanism for managing local databases based on the underlying SQLite. You can use the APIs to perform operations such as adding, deleting, modifying, and querying data, and directly run SQL statements. In addition, you can obtain sendable data using [ResultSet.getSendableRow](arkts-arkdata-relationalstore-resultset-i.md#getSendableRow) and transfer the data across threads. To ensure successful data access, limit the size of a data record to 2 MB. If a data record exceeds 2 MB, it can be inserted successfully but cannot be read. Querying data from a large amount of data may take time or even cause application suspension. In this case, you can perform batch operations. For details, see [Batch Database Operations](../../../arkts-utils/batch-database-operations-guide.md). Moreover, observe the following: - The number of data records to be queried at a time should not exceed 5000. - Use [TaskPool](../../apis-arkts/arkts-apis/arkts-taskpool.md#@ohos.taskpool) if there is a large amount of data needs to be queried. - Keep concatenated SQL statements as concise as possible. - Query data in batches. The **relationalStore** module provides the following functionalities: - [RdbPredicates](#@ohos.data.relationalStore): provides predicates indicating the nature, feature, or relationship of a data entity in an RDB store. It is used to define the operation conditions for an RDB store. - [RdbStore](#@ohos.data.relationalStore): provides APIs for managing data in an RDB store. - [ResultSet](#@ohos.data.relationalStore): provides APIs for accessing the result set obtained from the RDB store. - [LiteResultSet](#@ohos.data.relationalStore): provides APIs for accessing the result set obtained from the RDB store, such as [queryWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#queryWithoutRowCount) and [querySqlWithoutRowCount](arkts-arkdata-relationalstore-rdbstore-i.md#querySqlWithoutRowCount). Unlike [ResultSet](#@ohos.data.relationalStore), **LiteResultSet** does not include the total number of rows in the query result. - [Transaction](#@ohos.data.relationalStore): provides APIs for managing transaction objects.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace relationalStore--><!--Device-unnamed-declare namespace relationalStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore) |
| [deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleteRdbStore) |
| [getDeleteSqlInfo](arkts-arkdata-relationalstore-getdeletesqlinfo-f.md#getDeleteSqlInfo) |
| [getInsertSqlInfo](arkts-arkdata-relationalstore-getinsertsqlinfo-f.md#getInsertSqlInfo) |
| [getQuerySqlInfo](arkts-arkdata-relationalstore-getquerysqlinfo-f.md#getQuerySqlInfo) |
| [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getRdbStore) | Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses an asynchronous callback to return the result. If no database file exists in the corresponding sandbox directory, a database file is created. For details, see [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig). If a database file exists in the corresponding directory, the existing database file is opened. When creating a database, you should consider whether to configure the [encrypt](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig) parameter. Once the database is created, you are not allowed to change this parameter. \| Encryption Type When the RDB Store Is Opened \| Encryption Type When the RDB Store Is Created \| Result\| \| ------- \| -------------------------------- \| ---- \| \| Non-encryption\| Encryption \| The RDB store is opened in encrypted mode. \| \| Encryption\| Non-encryption \| The RDB store is opened in non-encrypted mode. \|
| [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getRdbStore) | Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses a promise to return the result. If no database file exists in the corresponding sandbox directory, a database file is created. For details, see [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig). If a database file exists in the corresponding directory, the existing database file is opened. When creating a database, you should consider whether to configure the [encrypt](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig) parameter. Once the database is created, you are not allowed to change this parameter. \| Encryption Type When the RDB Store Is Opened \| Encryption Type When the RDB Store Is Created \| Result\| \| ------- \| -------------------------------- \| ---- \| \| Non-encryption\| Encryption \| The RDB store is opened in encrypted mode. \| \| Encryption\| Non-encryption \| The RDB store is opened in non-encrypted mode. \|
| [getRdbStoreSync](arkts-arkdata-relationalstore-getrdbstoresync-f.md#getRdbStoreSync) |
| [getUpdateSqlInfo](arkts-arkdata-relationalstore-getupdatesqlinfo-f.md#getUpdateSqlInfo) |
| [isTokenizerSupported](arkts-arkdata-relationalstore-istokenizersupported-f.md#isTokenizerSupported) |
| [isVectorSupported](arkts-arkdata-relationalstore-isvectorsupported-f.md#isVectorSupported) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i-sys.md) |
| [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i-sys.md) |
| [DistributedInfo](arkts-arkdata-relationalstore-distributedinfo-i-sys.md) |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i-sys.md) |
| [Reference](arkts-arkdata-relationalstore-reference-i-sys.md) |
| [ResultSet](arkts-arkdata-relationalstore-resultset-i-sys.md) |
| [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DistributedField](arkts-arkdata-relationalstore-distributedfield-e-sys.md) |
| [DistributedOrigin](arkts-arkdata-relationalstore-distributedorigin-e-sys.md) |
| [HAMode](arkts-arkdata-relationalstore-hamode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Assets](arkts-arkdata-relationalstore-assets-t.md) |
| [ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md) |
| [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md) |
| [RowData](arkts-arkdata-relationalstore-rowdata-t.md) |
| [RowsData](arkts-arkdata-relationalstore-rowsdata-t.md) |
| [UTCTime](arkts-arkdata-relationalstore-utctime-t.md) |
| [ValueType](arkts-arkdata-relationalstore-valuetype-t.md) |
| [ValuesBucket](arkts-arkdata-relationalstore-valuesbucket-t.md) |
