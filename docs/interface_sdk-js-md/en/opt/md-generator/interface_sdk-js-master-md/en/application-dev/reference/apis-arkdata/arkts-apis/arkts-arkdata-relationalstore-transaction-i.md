# Transaction

Provides APIs for managing databases in transaction mode. A transaction object is created by using [createTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#createtransaction). Operations on different transaction objects are isolated. For details about the transaction types, see [TransactionType](arkts-arkdata-relationalstore-transactiontype-e.md#transactiontype). Currently, an RDB store supports only one write transaction at a time. If the current [RdbStore](arkts-data-relationalstore.md#ohosdatarelationalstore) has a write transaction that is not released, creating an **IMMEDIATE** or **EXCLUSIVE** transaction object will return error 14800024. If a **DEFERRED** transaction object is created, error 14800024 may be returned when it is used to invoke a write operation for the first time. After a write transaction is created using **IMMEDIATE** or **EXCLUSIVE**, or a **DEFERRED** transaction is upgraded to a write transaction, write operations in the [RdbStore](arkts-data-relationalstore.md#ohosdatarelationalstore) will also return error 14800024. When the number of concurrent transactions is large and the write transaction duration is long, the frequency of returning error 14800024 may increase. You can reduce the occurrence of error 14800024 by shortening the transaction duration or by handling the error 14800024 through retries. Before using the following APIs, you should obtain a **Transaction** instance by calling the [createTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#createtransaction) method and then call the corresponding method through the instance. **System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core **Example**: For details about the definition of **this.context** in the sample code, see the application [context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#context) of the stage model.

**Since:** 23

<!--Device-relationalStore-interface Transaction--><!--Device-relationalStore-interface Transaction-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
```

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

Inserts data into a table in batches. This API uses a promise to return the result. Data is written in batches of up to 32,766 parameters each with the [ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution) policy. The total number of parameters is calculated as the number of inserted data records multiplied by the size of the union set of all fields in the inserted data. If the operation fails, an error is returned. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

<!--Device-Transaction-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>--><!--Device-Transaction-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## batchInsertSync

```TypeScript
batchInsertSync(table: string, values: Array<ValuesBucket>): number
```

Inserts data into a table in batches. This API returns the result synchronously. Data is written in batches of up to 32,766 parameters each with the [ConflictResolution.ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution) policy. The total number of parameters is calculated as the number of inserted data records multiplied by the size of the union set of all fields in the inserted data. If the operation fails, an error is returned. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

<!--Device-Transaction-batchInsertSync(table: string, values: Array<ValuesBucket>): long--><!--Device-Transaction-batchInsertSync(table: string, values: Array<ValuesBucket>): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## batchInsertWithConflictResolution

```TypeScript
batchInsertWithConflictResolution(
        table: string,
        values: Array<ValuesBucket>,
        conflict: ConflictResolution
    ): Promise<number>
```

Inserts data into a table with conflict resolutions in batches. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution). This API uses a promise to return the result. A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code 14800000 is returned. The number of inserted data records multiplied by the size of the union across all fields in the inserted data equals the number of parameters. For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327 60). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since:** 23

<!--Device-Transaction-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): Promise<long>--><!--Device-Transaction-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## batchInsertWithConflictResolutionSync

```TypeScript
batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,
      conflict: ConflictResolution): number
```

Inserts data into a table with conflict resolutions in batches. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution). A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code 14800000 is returned. The number of inserted data records multiplied by the size of the union across all fields in the inserted data equals the number of parameters. For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327 60). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

<!--Device-Transaction-batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,      conflict: ConflictResolution): long--><!--Device-Transaction-batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>,      conflict: ConflictResolution): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## batchInsertWithReturning

```TypeScript
batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

Inserts data into a table in batches. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution), and [Result](arkts-arkdata-relationalstore-result-i.md#result) is returned. This API uses a promise to return the result. A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code 14800001 is returned. The number of inserted data records multiplied by the size of the union across all fields in the inserted data equals the number of parameters. For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327 60). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters. It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent the return of correct results. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-Transaction-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## batchInsertWithReturningSync

```TypeScript
batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

Inserts data into a table in batches. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution), and [Result](arkts-arkdata-relationalstore-result-i.md#result) is returned. A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code 14800001 is returned. The number of inserted data records multiplied by the size of the union across all fields in the inserted data equals the number of parameters. For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327 60). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters. It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent the return of correct results. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-Transaction-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## commit

```TypeScript
commit(): Promise<void>
```

Commits this executed SQL statement. This API uses a promise to return the result. When using asynchronous APIs to execute SQL statements, ensure that **commit()** is called after the asynchronous API execution is completed. Otherwise, the SQL operations may be lost. After **commit()** is called, the transaction object and the created **ResultSet** object will be closed.

**Since:** 23

<!--Device-Transaction-commit(): Promise<void>--><!--Device-Transaction-commit(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**Since:** 23

<!--Device-Transaction-delete(predicates: RdbPredicates): Promise<long>--><!--Device-Transaction-delete(predicates: RdbPredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## deleteSync

```TypeScript
deleteSync(predicates: RdbPredicates): number
```

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API returns the result synchronously.

**Since:** 23

<!--Device-Transaction-deleteSync(predicates: RdbPredicates): long--><!--Device-Transaction-deleteSync(predicates: RdbPredicates): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## deleteWithReturning

```TypeScript
deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>
```

Deletes data from the RDB store based on the specified **RdbPredicates** object and returns [Result](arkts-arkdata-relationalstore-result-i.md#result). This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>--><!--Device-Transaction-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## deleteWithReturningSync

```TypeScript
deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result
```

Deletes data from the RDB store based on the specified **RdbPredicates** object and returns [Result](arkts-arkdata-relationalstore-result-i.md#result).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result--><!--Device-Transaction-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## execute

```TypeScript
execute(sql: string, args?: Array<ValueType>): Promise<ValueType>
```

Executes an SQL statement that contains parameters but does not return data. This API returns the result synchronously. The SQL statement can be used to create, delete, query, and modify a table. The type of the return value varies, depending on the execution result. This API does not support query, database attachment, and transaction operations. You can use [querySql](#querysql) or [query](#query) to query data, and use [attach] [attach](arkts-arkdata-relationalstore-rdbstore-i.md#attach) to attach a database. Statements separated by semicolons (\;) are not supported. Statements starting with comments are not supported.

**Since:** 23

<!--Device-Transaction-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>--><!--Device-Transaction-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ValueType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## executeSync

```TypeScript
executeSync(sql: string, args?: Array<ValueType>): ValueType
```

Executes an SQL statement that contains specified arguments. The number of relational operators between expressions and operators in the statement cannot exceed 1,000. This API returns a value of the **ValueType** type. This API can be used to add, delete, and modify data, run SQL statements of the PRAGMA syntax, and create, delete, and modify a table. The type of the return value varies, depending on the execution result. This API does not support query, database attachment, and transaction operations. You can use [querySql](#querysql) or [query](#query) to query data, and use [attach] [attach](arkts-arkdata-relationalstore-rdbstore-i.md#attach) to attach a database. Statements separated by semicolons (\;) are not supported. Statements starting with comments are not supported.

**Since:** 23

<!--Device-Transaction-executeSync(sql: string, args?: Array<ValueType>): ValueType--><!--Device-Transaction-executeSync(sql: string, args?: Array<ValueType>): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>
```

Inserts a row of data into a table. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue) and [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring) after **ResultSet** is obtained through the [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) or [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 23

<!--Device-Transaction-insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<long>--><!--Device-Transaction-insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## insertSync

```TypeScript
insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,
      conflict?: ConflictResolution): number
```

Inserts a row of data into a table. This API returns the result synchronously. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue) and [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring) after **ResultSet** is obtained through the [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) or [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown. A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.

**Since:** 14

<!--Device-Transaction-insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,      conflict?: ConflictResolution): number--><!--Device-Transaction-insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket,      conflict?: ConflictResolution): number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | ValuesBucket \| sendableRelationalStore.ValuesBucket | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## insertSync

```TypeScript
insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number
```

Inserts a row of data into the target table with sync interface, just use in TaskPool or Worker.

**Since:** 23

<!--Device-Transaction-insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): long--><!--Device-Transaction-insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Queries data from the RDB store based on specified conditions. This API uses a promise to return the result.

**Since:** 23

<!--Device-Transaction-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-Transaction-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySql

```TypeScript
querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>
```

Queries data in the RDB store using the specified SQL statement. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1,000. This API uses a promise to return the result.

**Since:** 23

<!--Device-Transaction-querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>--><!--Device-Transaction-querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySqlSync

```TypeScript
querySqlSync(sql: string, args?: Array<ValueType>): ResultSet
```

Queries data in the RDB store using the specified SQL statement. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1,000. If complex logic and a large number of loops are involved in the operations on the **resultSet** obtained by **querySync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#ohostaskpool) thread.

**Since:** 23

<!--Device-Transaction-querySqlSync(sql: string, args?: Array<ValueType>): ResultSet--><!--Device-Transaction-querySqlSync(sql: string, args?: Array<ValueType>): ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySqlWithoutRowCount

```TypeScript
querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>
```

Queries data from the RDB store based on specified conditions without calculating the row count. This API uses a promise to return the result and delivers better performance than the [querySql](#querysql) API. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1,000.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>--><!--Device-Transaction-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySqlWithoutRowCountSync

```TypeScript
querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet
```

Queries data from the RDB store based on specified SQL statements without calculating the row count. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1,000. If complex logic and a large number of loops are involved in the operations on the **LiteResultSet** obtained by **querySqlWithoutRowCountSync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#ohostaskpool) thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet--><!--Device-Transaction-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySync

```TypeScript
querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet
```

Queries data in a database based on specified conditions. This API returns the result synchronously. If complex logic and a large number of loops are involved in the operations on the **resultSet** obtained by **querySync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#ohostaskpool) thread.

**Since:** 23

<!--Device-Transaction-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet--><!--Device-Transaction-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryWithoutRowCount

```TypeScript
queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>
```

Queries data from the RDB store based on specified conditions without calculating the row count. This API delivers better performance than the [query](#query) API. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>--><!--Device-Transaction-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryWithoutRowCountSync

```TypeScript
queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet
```

Queries data from the RDB store based on specified conditions without calculating the row count. If complex logic and a large number of loops are involved in the operations on the **LiteResultSet** obtained by **queryWithoutRowCountSync**, the freeze problem may occur. You are advised to perform this operation in the [taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#ohostaskpool) thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet--><!--Device-Transaction-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## rollback

```TypeScript
rollback(): Promise<void>
```

Rolls back this executed SQL statement. This API uses a promise to return the result. After **rollback()** is called, the transaction object and the created **ResultSet** object will be closed.

**Since:** 23

<!--Device-Transaction-rollback(): Promise<void>--><!--Device-Transaction-rollback(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>
```

Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue) and [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring) after **ResultSet** is obtained through the [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) or [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**Since:** 23

<!--Device-Transaction-update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<long>--><!--Device-Transaction-update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## updateSync

```TypeScript
updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number
```

Updates data in the RDB store based on the specified **RdbPredicates** object. This API returns the result synchronously. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get** methods such as [getValue](arkts-arkdata-relationalstore-resultset-i.md#getvalue) and [getString](arkts-arkdata-relationalstore-resultset-i.md#getstring) after **ResultSet** is obtained through the [query](arkts-arkdata-relationalstore-rdbstore-i.md#query) or [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querysqlwithoutrowcount) API of **RdbStore**. As a result, the operation may fail or an exception may be thrown.

**Since:** 23

<!--Device-Transaction-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long--><!--Device-Transaction-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800031](../errorcode-data-rdb.md#14800031-sqlite-text-or-blob-exceeds-the-limit) |

## updateWithReturning

```TypeScript
updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

Updates data in the RDB store based on the specified **RdbPredicates** instance object. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution), and [Result](arkts-arkdata-relationalstore-result-i.md#result) is returned. This API uses a promise to return the result. It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent the return of correct results.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-Transaction-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## updateWithReturningSync

```TypeScript
updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

Updates data in the RDB store based on the specified **RdbPredicates** instance object. You can use the **conflict** parameter to specify [ConflictResolution](arkts-arkdata-relationalstore-conflictresolution-e.md#conflictresolution), and [Result](arkts-arkdata-relationalstore-result-i.md#result) is returned. It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent the return of correct results.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Transaction-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-Transaction-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| config | [ReturningConfig](arkts-arkdata-relationalstore-returningconfig-i.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Result](arkts-arkdata-relationalstore-result-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800025](../errorcode-data-rdb.md#14800025-sqlite-database-table-locked) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
