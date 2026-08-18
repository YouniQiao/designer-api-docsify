# RdbStore

Provides APIs for managing data in an RDB store. Before using the following APIs, you should obtain an **RdbStore** instance by calling the [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore) method and then call the corresponding method through the instance. In addition, use [execute](#execute) to initialize the database table structure and related data first, ensuring that the prerequisites for related API calls are met.

**Since:** 23

<!--Device-relationalStore-interface RdbStore--><!--Device-relationalStore-interface RdbStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
```

## attach

```TypeScript
attach(fullPath: string, attachName: string, waitTime?: number) : Promise<number>
```

Attaches a database file to the currently linked database.

**Since:** 23

<!--Device-RdbStore-attach(fullPath: string, attachName: string, waitTime?: int) : Promise<int>--><!--Device-RdbStore-attach(fullPath: string, attachName: string, waitTime?: int) : Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullPath | string | Yes |
| attachName | string | Yes |
| waitTime | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800016](../errorcode-data-rdb.md#14800016-duplicate-rdb-alias) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## attach

```TypeScript
attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number) : Promise<number>
```

Attaches a database file to the currently linked database.

**Since:** 23

<!--Device-RdbStore-attach(context: Context, config: StoreConfig, attachName: string, waitTime?: int) : Promise<int>--><!--Device-RdbStore-attach(context: Context, config: StoreConfig, attachName: string, waitTime?: int) : Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes |
| attachName | string | Yes |
| waitTime | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14801001](../errorcode-data-rdb.md#14801001-stage-model-required) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14801002](../errorcode-data-rdb.md#14801002-invalid-datagroupid-in-storeconfig) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800016](../errorcode-data-rdb.md#14800016-duplicate-rdb-alias) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## backup

```TypeScript
backup(destName: string, callback: AsyncCallback<void>): void
```

Backs up a database in a specified name.

**Since:** 23

<!--Device-RdbStore-backup(destName: string, callback: AsyncCallback<void>): void--><!--Device-RdbStore-backup(destName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| destName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## backup

```TypeScript
backup(destName: string): Promise<void>
```

Backs up a database in a specified name.

**Since:** 23

<!--Device-RdbStore-backup(destName: string): Promise<void>--><!--Device-RdbStore-backup(destName: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| destName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

Inserts a batch of data into the target table. The data insertion fails if the API returns an error, or if it returns -1 without throwing an error. Write 32766 parameters per batch using the [ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#onconflictreplace) policy. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. This API returns immediately upon a failure during the process.

**Since:** 23

<!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<long>): void--><!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

Inserts a batch of data into the target table. The data insertion fails if the API returns an error, or if it returns -1 without throwing an error. Write 32766 parameters per batch using the [ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#onconflictreplace) policy. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. This API returns immediately upon a failure during the process.

**Since:** 23

<!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>--><!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>): Promise<long>-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsertSync

```TypeScript
batchInsertSync(table: string, values: Array<ValuesBucket>): number
```

Inserts a batch of data into the target table. The data insertion fails if the API returns an error, or if it returns -1 without throwing an error. Write 32766 parameters per batch using the [ON_CONFLICT_REPLACE](arkts-arkdata-relationalstore-conflictresolution-e.md#onconflictreplace) policy. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. This API returns immediately upon a failure during the process.

**Since:** 23

<!--Device-RdbStore-batchInsertSync(table: string, values: Array<ValuesBucket>): long--><!--Device-RdbStore-batchInsertSync(table: string, values: Array<ValuesBucket>): long-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsertWithConflictResolution

```TypeScript
batchInsertWithConflictResolution(
        table: string,
        values: Array<ValuesBucket>, 
        conflict: ConflictResolution
    ): Promise<number>
```

Inserts a batch of data into the target table. A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800000 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since:** 23

<!--Device-RdbStore-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,         conflict: ConflictResolution    ): Promise<long>--><!--Device-RdbStore-batchInsertWithConflictResolution(        table: string,        values: Array<ValuesBucket>,         conflict: ConflictResolution    ): Promise<long>-End-->

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsertWithConflictResolutionSync

```TypeScript
batchInsertWithConflictResolutionSync(
        table: string,
        values: Array<ValuesBucket>,
        conflict: ConflictResolution
    ): number
```

Inserts a batch of data into the target table. A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800000 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since:** 23

<!--Device-RdbStore-batchInsertWithConflictResolutionSync(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): long--><!--Device-RdbStore-batchInsertWithConflictResolutionSync(        table: string,        values: Array<ValuesBucket>,        conflict: ConflictResolution    ): long-End-->

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## batchInsertWithReturning

```TypeScript
batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

Inserts a batch of data into the target table and return a resultSet of changed fields. A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800001 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-RdbStore-batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## batchInsertWithReturningSync

```TypeScript
batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

Inserts a batch of data into the target table and return a resultSet of changed fields. A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit, the error code 14800001 is returned. The product of the number of inserted data records and the size of the union of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10, a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-RdbStore-batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## beginTrans

```TypeScript
beginTrans(): Promise<number>
```

Begins a transaction before executing the SQL statement.

**Since:** 23

<!--Device-RdbStore-beginTrans(): Promise<long>--><!--Device-RdbStore-beginTrans(): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## beginTransaction

```TypeScript
beginTransaction(): void
```

BeginTransaction before execute your sql.

**Since:** 23

<!--Device-RdbStore-beginTransaction(): void--><!--Device-RdbStore-beginTransaction(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void
```

Cleans the dirty data, which is the data deleted in the cloud. Data with a cursor smaller than the specified cursor will be cleaned up.

**Since:** 23

<!--Device-RdbStore-cleanDirtyData(table: string, cursor: long, callback: AsyncCallback<void>): void--><!--Device-RdbStore-cleanDirtyData(table: string, cursor: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| cursor | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, callback: AsyncCallback<void>): void
```

Cleans all dirty data deleted in the cloud.

**Since:** 23

<!--Device-RdbStore-cleanDirtyData(table: string, callback: AsyncCallback<void>): void--><!--Device-RdbStore-cleanDirtyData(table: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## cleanDirtyData

```TypeScript
cleanDirtyData(table: string, cursor?: number): Promise<void>
```

Cleans dirty data deleted in the cloud. If a cursor is specified, data with a cursor smaller than the specified cursor will be cleaned up. otherwise clean all.

**Since:** 23

<!--Device-RdbStore-cleanDirtyData(table: string, cursor?: long): Promise<void>--><!--Device-RdbStore-cleanDirtyData(table: string, cursor?: long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| cursor | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## close

```TypeScript
close(): Promise<void>
```

Close the RdbStore and all resultSets.

**Since:** 23

<!--Device-RdbStore-close(): Promise<void>--><!--Device-RdbStore-close(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void
```

Sync data to cloud.

**Since:** 23

<!--Device-RdbStore-cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void--><!--Device-RdbStore-cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>
```

Sync data to cloud.

**Since:** 23

<!--Device-RdbStore-cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSync

```TypeScript
cloudSync(
      mode: SyncMode,
      tables: string[],
      progress: Callback<ProgressDetails>,
      callback: AsyncCallback<void>
    ): void
```

Sync data to cloud.

**Since:** 23

<!--Device-RdbStore-cloudSync(      mode: SyncMode,      tables: string[],      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void--><!--Device-RdbStore-cloudSync(      mode: SyncMode,      tables: string[],      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | string[] | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>
```

Sync data to cloud.

**Since:** 23

<!--Device-RdbStore-cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | string[] | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSyncEx

```TypeScript
cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>
```

Synchronizes data to the cloud. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [CloudSyncConfig](arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## commit

```TypeScript
commit(): void
```

Commit the the sql you have executed.

**Since:** 23

<!--Device-RdbStore-commit(): void--><!--Device-RdbStore-commit(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## commit

```TypeScript
commit(txId : number): Promise<void>
```

Commits the SQL statement executed.

**Since:** 23

<!--Device-RdbStore-commit(txId : long): Promise<void>--><!--Device-RdbStore-commit(txId : long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| txId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## createTransaction

```TypeScript
createTransaction(options?: TransactionOptions): Promise<Transaction>
```

create a transaction instance and begin.

**Since:** 23

<!--Device-RdbStore-createTransaction(options?: TransactionOptions): Promise<Transaction>--><!--Device-RdbStore-createTransaction(options?: TransactionOptions): Promise<Transaction>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TransactionOptions](arkts-arkdata-relationalstore-transactionoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Transaction](arkts-arkdata-relationalstore-transaction-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## delete

```TypeScript
delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

Deletes data from the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-delete(predicates: RdbPredicates, callback: AsyncCallback<long>): void--><!--Device-RdbStore-delete(predicates: RdbPredicates, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

Deletes data from the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-delete(predicates: RdbPredicates): Promise<long>--><!--Device-RdbStore-delete(predicates: RdbPredicates): Promise<long>-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## deleteSync

```TypeScript
deleteSync(predicates: RdbPredicates): number
```

Deletes data from the database based on a specified instance object of RdbPredicates with sync interface.

**Since:** 23

<!--Device-RdbStore-deleteSync(predicates: RdbPredicates): long--><!--Device-RdbStore-deleteSync(predicates: RdbPredicates): long-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## deleteWithReturning

```TypeScript
deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>
```

Deletes data from the database based on a specified instance object of RdbPredicates and return a resultSet of changed fields.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>--><!--Device-RdbStore-deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## deleteWithReturningSync

```TypeScript
deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result
```

Deletes data from the database based on a specified instance object of RdbPredicates and return a resultSet of changed fields.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result--><!--Device-RdbStore-deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## detach

```TypeScript
detach(attachName: string, waitTime?: number) : Promise<number>
```

Detaches a database from this database.

**Since:** 23

<!--Device-RdbStore-detach(attachName: string, waitTime?: int) : Promise<int>--><!--Device-RdbStore-detach(attachName: string, waitTime?: int) : Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attachName | string | Yes |
| waitTime | number | No |

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## emit_string

```TypeScript
emit(event: string): void
```

Notifies the registered observers of a change to the data resource specified by Uri.

**Since:** 23

<!--Device-RdbStore-emit(event: string): void--><!--Device-RdbStore-emit(event: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800050](../errorcode-data-rdb.md#14800050-failed-to-obtain-the-subscription-service) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## execute

```TypeScript
execute(sql: string, args?: Array<ValueType>): Promise<ValueType>
```

Executes a SQL statement that contains specified parameters and returns a value of ValueType.

**Since:** 23

<!--Device-RdbStore-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>--><!--Device-RdbStore-execute(sql: string, args?: Array<ValueType>): Promise<ValueType>-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## execute

```TypeScript
execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>
```

Executes a SQL statement that contains specified parameters and returns a value of ValueType.

**Since:** 23

<!--Device-RdbStore-execute(sql: string, txId: long, args?: Array<ValueType>): Promise<ValueType>--><!--Device-RdbStore-execute(sql: string, txId: long, args?: Array<ValueType>): Promise<ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| txId | number | Yes |
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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## executeSql

```TypeScript
executeSql(sql: string, callback: AsyncCallback<void>): void
```

Executes a SQL statement that contains specified parameters but returns no value.

**Since:** 23

<!--Device-RdbStore-executeSql(sql: string, callback: AsyncCallback<void>): void--><!--Device-RdbStore-executeSql(sql: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void
```

Executes a SQL statement that contains specified parameters but returns no value.

**Since:** 23

<!--Device-RdbStore-executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void--><!--Device-RdbStore-executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## executeSql

```TypeScript
executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>
```

Executes a SQL statement that contains specified parameters but returns no value.

**Since:** 23

<!--Device-RdbStore-executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>--><!--Device-RdbStore-executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## executeSync

```TypeScript
executeSync(sql: string, args?: Array<ValueType>): ValueType
```

Executes a SQL statement that contains specified parameters and returns a value of ValueType with sync interface.

**Since:** 23

<!--Device-RdbStore-executeSync(sql: string, args?: Array<ValueType>): ValueType--><!--Device-RdbStore-executeSync(sql: string, args?: Array<ValueType>): ValueType-End-->

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
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getModifyTime

```TypeScript
getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>
```

Obtains the modify time of rows corresponding to the primary keys.

**Since:** 23

<!--Device-RdbStore-getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>--><!--Device-RdbStore-getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| columnName | string | Yes |
| primaryKeys | [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## getModifyTime

```TypeScript
getModifyTime(
      table: string,
      columnName: string,
      primaryKeys: PRIKeyType[],
      callback: AsyncCallback<ModifyTime>
    ): void
```

Obtains the modify time of rows corresponding to the primary keys.

**Since:** 23

<!--Device-RdbStore-getModifyTime(      table: string,      columnName: string,      primaryKeys: PRIKeyType[],      callback: AsyncCallback<ModifyTime>    ): void--><!--Device-RdbStore-getModifyTime(      table: string,      columnName: string,      primaryKeys: PRIKeyType[],      callback: AsyncCallback<ModifyTime>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| columnName | string | Yes |
| primaryKeys | [PRIKeyType](arkts-arkdata-relationalstore-prikeytype-t.md)[] | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ModifyTime](arkts-arkdata-relationalstore-modifytime-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void
```

Inserts a row of data into the target table.

**Since:** 23

<!--Device-RdbStore-insert(table: string, values: ValuesBucket, callback: AsyncCallback<long>): void--><!--Device-RdbStore-insert(table: string, values: ValuesBucket, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>): void
```

Inserts a row of data into the target table.

**Since:** 23

<!--Device-RdbStore-insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<long>): void--><!--Device-RdbStore-insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket): Promise<number>
```

Inserts a row of data into the target table.

**Since:** 23

<!--Device-RdbStore-insert(table: string, values: ValuesBucket): Promise<long>--><!--Device-RdbStore-insert(table: string, values: ValuesBucket): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insert

```TypeScript
insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<number>
```

Inserts a row of data into the target table.

**Since:** 23

<!--Device-RdbStore-insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<long>--><!--Device-RdbStore-insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insertSync

```TypeScript
insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number
```

Inserts a row of data into the target table with sync interface.

**Since:** 23

<!--Device-RdbStore-insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): long--><!--Device-RdbStore-insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): long-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## insertSync

```TypeScript
insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number
```

Inserts a row of data into the target table with sync interface.

**Since:** 12

<!--Device-RdbStore-insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number--><!--Device-RdbStore-insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | sendableRelationalStore.ValuesBucket | Yes |
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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## lockRow

```TypeScript
lockRow(predicates: RdbPredicates): Promise<void>
```

Locks data from the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-lockRow(predicates: RdbPredicates): Promise<void>--><!--Device-RdbStore-lockRow(predicates: RdbPredicates): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800018](../errorcode-data-rdb.md#14800018-no-match) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void
```

Obtain distributed table name of specified remote device according to local table name. When query remote device database, distributed table name is needed.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void--><!--Device-RdbStore-obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string): Promise<string>
```

Obtain distributed table name of specified remote device according to local table name. When query remote device database, distributed table name is needed.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-obtainDistributedTableName(device: string, table: string): Promise<string>--><!--Device-RdbStore-obtainDistributedTableName(device: string, table: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## offAutoSyncProgress

```TypeScript
offAutoSyncProgress(progress?: Callback<ProgressDetails>): void
```

Unregister the database auto synchronization callback.

**Since:** 23

<!--Device-RdbStore-offAutoSyncProgress(progress?: Callback<ProgressDetails>): void--><!--Device-RdbStore-offAutoSyncProgress(progress?: Callback<ProgressDetails>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## offDataChange

```TypeScript
offDataChange(type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void
```

Remove specified observer of specified type from the database.

**Since:** 23

<!--Device-RdbStore-offDataChange(type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void--><!--Device-RdbStore-offDataChange(type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## offPerfStat

```TypeScript
offPerfStat(observer?: Callback<SqlExecutionInfo>): void
```

Unsubscribes from the SQL performance statistics.

**Since:** 23

<!--Device-RdbStore-offPerfStat(observer?: Callback<SqlExecutionInfo>): void--><!--Device-RdbStore-offPerfStat(observer?: Callback<SqlExecutionInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## offSqliteErrorOccurred

```TypeScript
offSqliteErrorOccurred(observer?: Callback<ExceptionMessage>): void
```

Unsubscribes from the SQL execution error logs.

**Since:** 23

<!--Device-RdbStore-offSqliteErrorOccurred(observer?: Callback<ExceptionMessage>): void--><!--Device-RdbStore-offSqliteErrorOccurred(observer?: Callback<ExceptionMessage>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## offStatistics

```TypeScript
offStatistics(observer?: Callback<SqlExecutionInfo> ): void
```

Unsubscribes from the SQL statistics.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-offStatistics(observer?: Callback<SqlExecutionInfo> ): void--><!--Device-RdbStore-offStatistics(observer?: Callback<SqlExecutionInfo> ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_autoSyncProgress

```TypeScript
off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void
```

Unregister the database auto synchronization callback.

**Since:** 11

<!--Device-RdbStore-off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void--><!--Device-RdbStore-off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'autoSyncProgress' | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_dataChange

```TypeScript
off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

Remove specified observer of specified type from the database.

**Since:** 9

<!--Device-RdbStore-off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void--><!--Device-RdbStore-off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_dataChange

```TypeScript
off(
      event: 'dataChange',
      type: SubscribeType,
      observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>
    ): void
```

Remove specified observer of specified type from the database.

**Since:** 10

<!--Device-RdbStore-off(      event: 'dataChange',      type: SubscribeType,      observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>    ): void--><!--Device-RdbStore-off(      event: 'dataChange',      type: SubscribeType,      observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_perfStat

```TypeScript
off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void
```

Unsubscribes from the SQL performance statistics.

**Since:** 20

<!--Device-RdbStore-off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void--><!--Device-RdbStore-off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'perfStat' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_sqliteErrorOccurred

```TypeScript
off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void
```

Unsubscribes from the SQL execution error logs.

**Since:** 20

<!--Device-RdbStore-off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void--><!--Device-RdbStore-off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'sqliteErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_statistics

```TypeScript
off(event: 'statistics', observer?: Callback<SqlExecutionInfo> ): void
```

Unsubscribes from the SQL statistics.

**Since:** 12

<!--Device-RdbStore-off(event: 'statistics', observer?: Callback<SqlExecutionInfo> ): void--><!--Device-RdbStore-off(event: 'statistics', observer?: Callback<SqlExecutionInfo> ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'statistics' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## off_string

```TypeScript
off(event: string, interProcess: boolean, observer?: Callback<void>): void
```

Remove specified observer of specified type from the database.

**Since:** 23

<!--Device-RdbStore-off(event: string, interProcess: boolean, observer?: Callback<void>): void--><!--Device-RdbStore-off(event: string, interProcess: boolean, observer?: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| interProcess | boolean | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800050](../errorcode-data-rdb.md#14800050-failed-to-obtain-the-subscription-service) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## onAutoSyncProgress

```TypeScript
onAutoSyncProgress(progress: Callback<ProgressDetails>): void
```

Register an automatic synchronization callback to the database.

**Since:** 23

<!--Device-RdbStore-onAutoSyncProgress(progress: Callback<ProgressDetails>): void--><!--Device-RdbStore-onAutoSyncProgress(progress: Callback<ProgressDetails>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## onDataChange

```TypeScript
onDataChange(
      type: SubscribeType, 
      observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>
    ): void
```

Subscribes to data changes of this RDB store. The registered callback will be called when data in a distributed RDB store changes.

**Since:** 23

<!--Device-RdbStore-onDataChange(      type: SubscribeType,       observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>    ): void--><!--Device-RdbStore-onDataChange(      type: SubscribeType,       observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## onPerfStat

```TypeScript
onPerfStat(observer: Callback<SqlExecutionInfo>): void
```

Subscribes to the SQL performance statistics.

**Since:** 23

<!--Device-RdbStore-onPerfStat(observer: Callback<SqlExecutionInfo>): void--><!--Device-RdbStore-onPerfStat(observer: Callback<SqlExecutionInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## onSqliteErrorOccurred

```TypeScript
onSqliteErrorOccurred(observer: Callback<ExceptionMessage>): void
```

Subscribes to the SQL execution error logs.

**Since:** 23

<!--Device-RdbStore-onSqliteErrorOccurred(observer: Callback<ExceptionMessage>): void--><!--Device-RdbStore-onSqliteErrorOccurred(observer: Callback<ExceptionMessage>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## onStatistics

```TypeScript
onStatistics(observer: Callback<SqlExecutionInfo> ): void
```

Subscribes to the SQL statistics.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-onStatistics(observer: Callback<SqlExecutionInfo> ): void--><!--Device-RdbStore-onStatistics(observer: Callback<SqlExecutionInfo> ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_autoSyncProgress

```TypeScript
on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void
```

Register an automatic synchronization callback to the database.

**Since:** 11

<!--Device-RdbStore-on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void--><!--Device-RdbStore-on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'autoSyncProgress' | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ProgressDetails](arkts-arkdata-relationalstore-progressdetails-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_dataChange

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

Subscribes to data changes of this RDB store. The registered callback will be called when data in a distributed RDB store changes. the callback will be invoked.

**Since:** 9

<!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void--><!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_dataChange

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void
```

Subscribes to data changes of this RDB store. The registered callback will be called when data in a distributed RDB store changes.

**Since:** 10

<!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void--><!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; \| [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ChangeInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_perfStat

```TypeScript
on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void
```

Subscribes to the SQL performance statistics.

**Since:** 20

<!--Device-RdbStore-on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void--><!--Device-RdbStore-on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'perfStat' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_sqliteErrorOccurred

```TypeScript
on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void
```

Subscribes to the SQL execution error logs.

**Since:** 20

<!--Device-RdbStore-on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void--><!--Device-RdbStore-on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'sqliteErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ExceptionMessage](arkts-arkdata-relationalstore-exceptionmessage-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_statistics

```TypeScript
on(event: 'statistics', observer: Callback<SqlExecutionInfo> ): void
```

Subscribes to the SQL statistics.

**Since:** 12

<!--Device-RdbStore-on(event: 'statistics', observer: Callback<SqlExecutionInfo> ): void--><!--Device-RdbStore-on(event: 'statistics', observer: Callback<SqlExecutionInfo> ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'statistics' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SqlExecutionInfo](arkts-arkdata-relationalstore-sqlexecutioninfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## on_string

```TypeScript
on(event: string, interProcess: boolean, observer: Callback<void>): void
```

Registers an observer for the database.

**Since:** 23

<!--Device-RdbStore-on(event: string, interProcess: boolean, observer: Callback<void>): void--><!--Device-RdbStore-on(event: string, interProcess: boolean, observer: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| interProcess | boolean | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800050](../errorcode-data-rdb.md#14800050-failed-to-obtain-the-subscription-service) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## query

```TypeScript
query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void
```

Queries data in the database based on specified conditions.

**Since:** 23

<!--Device-RdbStore-query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## query

```TypeScript
query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

Queries data in the database based on specified conditions.

**Since:** 23

<!--Device-RdbStore-query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Queries data in the database based on specified conditions.

**Since:** 23

<!--Device-RdbStore-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryByStep

```TypeScript
queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

Query data in the database step‑by‑step based on SQL statements.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>--><!--Device-RdbStore-queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryByStep

```TypeScript
queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Queries data in the database step‑by‑step based on specified conditions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

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
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryLockedRow

```TypeScript
queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Queries locked data in the database based on specified conditions.

**Since:** 23

<!--Device-RdbStore-queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

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
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## querySql

```TypeScript
querySql(sql: string, callback: AsyncCallback<ResultSet>): void
```

Queries data in the database based on SQL statement.

**Since:** 23

<!--Device-RdbStore-querySql(sql: string, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySql(sql: string, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySql

```TypeScript
querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void
```

Queries data in the database based on SQL statement.

**Since:** 23

<!--Device-RdbStore-querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySql

```TypeScript
querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

Queries data in the database based on SQL statement.

**Since:** 23

<!--Device-RdbStore-querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>--><!--Device-RdbStore-querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySqlSync

```TypeScript
querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet
```

Queries data in the database based on SQL statement with sync interface.

**Since:** 23

<!--Device-RdbStore-querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet--><!--Device-RdbStore-querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySqlWithoutRowCount

```TypeScript
querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>
```

Queries data from the RDB store based on specified conditions without calculating the row count. This API uses a promise to return the result and delivers better performance than the [querySql](arkts-arkdata-relationalstore-transaction-i.md#querysql) API. The number of relational operators between expressions and operators in the SQL statement cannot exceed 1,000.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>--><!--Device-RdbStore-querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>-End-->

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

<!--Device-RdbStore-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet--><!--Device-RdbStore-querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet-End-->

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

Queries data in the database based on specified conditions with sync function.

**Since:** 23

<!--Device-RdbStore-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet--><!--Device-RdbStore-querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet-End-->

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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## queryWithoutRowCount

```TypeScript
queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>
```

Queries data without rowCount in the database based on specified conditions.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>--><!--Device-RdbStore-queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>-End-->

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

Queries data without rowCount in the database based on specified conditions with sync function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet--><!--Device-RdbStore-queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet-End-->

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

## rekey

```TypeScript
rekey(cryptoParam?: CryptoParam): Promise<void>
```

Changes the key used to encrypt the database.

**Since:** 23

<!--Device-RdbStore-rekey(cryptoParam?: CryptoParam): Promise<void>--><!--Device-RdbStore-rekey(cryptoParam?: CryptoParam): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cryptoParam](arkts-arkdata-relationalstore-storeconfig-i.md) | [CryptoParam](arkts-arkdata-relationalstore-cryptoparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## rekeyEx

```TypeScript
rekeyEx(cryptoParam: CryptoParam): Promise<void>
```

Change the encryption parameters of the database.

**Since:** 23

<!--Device-RdbStore-rekeyEx(cryptoParam: CryptoParam): Promise<void>--><!--Device-RdbStore-rekeyEx(cryptoParam: CryptoParam): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cryptoParam](arkts-arkdata-relationalstore-storeconfig-i.md) | [CryptoParam](arkts-arkdata-relationalstore-cryptoparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800023](../errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

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

Queries remote data in the database based on specified conditions before Synchronizing Data.

**Since:** 23

<!--Device-RdbStore-remoteQuery(      device: string,      table: string,      predicates: RdbPredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void--><!--Device-RdbStore-remoteQuery(      device: string,      table: string,      predicates: RdbPredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## remoteQuery

```TypeScript
remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>
```

Queries remote data in the database based on specified conditions before Synchronizing Data.

**Since:** 23

<!--Device-RdbStore-remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## restore

```TypeScript
restore(srcName: string, callback: AsyncCallback<void>): void
```

Restores a database from a specified database file.

**Since:** 23

<!--Device-RdbStore-restore(srcName: string, callback: AsyncCallback<void>): void--><!--Device-RdbStore-restore(srcName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## restore

```TypeScript
restore(srcName: string): Promise<void>
```

Restores a database from a specified database file.

**Since:** 23

<!--Device-RdbStore-restore(srcName: string): Promise<void>--><!--Device-RdbStore-restore(srcName: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## rollBack

```TypeScript
rollBack(): void
```

Roll back the sql you have already executed.

**Since:** 23

<!--Device-RdbStore-rollBack(): void--><!--Device-RdbStore-rollBack(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## rollback

```TypeScript
rollback(txId : number): Promise<void>
```

Rolls back the SQL statement executed.

**Since:** 23

<!--Device-RdbStore-rollback(txId : long): Promise<void>--><!--Device-RdbStore-rollback(txId : long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| txId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void
```

Set table to be distributed table.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void--><!--Device-RdbStore-setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>): Promise<void>
```

Set table to be distributed table.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>): Promise<void>--><!--Device-RdbStore-setDistributedTables(tables: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void
```

Set table to be distributed table.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void--><!--Device-RdbStore-setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800051](../errorcode-data-rdb.md#14800051-inconsistent-distributed-table-type) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## setDistributedTables

```TypeScript
setDistributedTables(
      tables: Array<string>,
      type: DistributedType,
      config: DistributedConfig,
      callback: AsyncCallback<void>
    ): void
```

Set table to be distributed table.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(      tables: Array<string>,      type: DistributedType,      config: DistributedConfig,      callback: AsyncCallback<void>    ): void--><!--Device-RdbStore-setDistributedTables(      tables: Array<string>,      type: DistributedType,      config: DistributedConfig,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | Yes |
| config | [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800051](../errorcode-data-rdb.md#14800051-inconsistent-distributed-table-type) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>
```

Set table to be a distributed table.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>--><!--Device-RdbStore-setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |
| type | [DistributedType](arkts-arkdata-relationalstore-distributedtype-e.md) | No |
| config | [DistributedConfig](arkts-arkdata-relationalstore-distributedconfig-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800051](../errorcode-data-rdb.md#14800051-inconsistent-distributed-table-type) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## setLocale

```TypeScript
setLocale(locale: string) : Promise<void>
```

Support for collations in different languages.

**Since:** 23

<!--Device-RdbStore-setLocale(locale: string) : Promise<void>--><!--Device-RdbStore-setLocale(locale: string) : Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [14800026](../errorcode-data-rdb.md#14800026-sqlite-insufficient-database-memory) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## stopCloudSync

```TypeScript
stopCloudSync(): Promise<void>
```

Stops synchronizing data with the cloud.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-stopCloudSync(): Promise<void>--><!--Device-RdbStore-stopCloudSync(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void
```

Sync data between devices.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, int]>>): void--><!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, int]>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>
```

Sync data between devices.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, int]>>--><!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, int]>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;[string, number] & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## syncEx

```TypeScript
syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>
```

Sync data between devices. 1. The difference between the sync interface and the syncEx interface is that they can return more error codes, but their functionality is similar. 2. Before invoking synchronization, call setdistributedTable to set the distributed table.

**Since:** 26.0.0

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>--><!--Device-RdbStore-syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;SyncResult & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## unlockRow

```TypeScript
unlockRow(predicates: RdbPredicates): Promise<void>
```

Unlocks data from the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-unlockRow(predicates: RdbPredicates): Promise<void>--><!--Device-RdbStore-unlockRow(predicates: RdbPredicates): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800018](../errorcode-data-rdb.md#14800018-no-match) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<long>): void--><!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## update

```TypeScript
update(
      values: ValuesBucket,
      predicates: RdbPredicates,
      conflict: ConflictResolution,
      callback: AsyncCallback<number>
    ): void
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-update(      values: ValuesBucket,      predicates: RdbPredicates,      conflict: ConflictResolution,      callback: AsyncCallback<long>    ): void--><!--Device-RdbStore-update(      values: ValuesBucket,      predicates: RdbPredicates,      conflict: ConflictResolution,      callback: AsyncCallback<long>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| conflict | [ConflictResolution](../../apis-asset-store-kit/arkts-apis/arkts-assetstore-asset-conflictresolution-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates): Promise<long>--><!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<number>
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 23

<!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<long>--><!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
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
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## updateSync

```TypeScript
updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number
```

Updates data in the database based on a specified instance object of RdbPredicates with sync interface.

**Since:** 23

<!--Device-RdbStore-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long--><!--Device-RdbStore-updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): long-End-->

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
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
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
| [14800030](../errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

## updateWithReturning

```TypeScript
updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Promise<Result>
```

Updates data in the database based on a specified instance object of RdbPredicates and return a resultSet of changed fields.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>--><!--Device-RdbStore-updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Promise<Result>-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## updateWithReturningSync

```TypeScript
updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,
      conflict?: ConflictResolution): Result
```

Updates data in the database based on a specified instance object of RdbPredicates and return a resultSet of changed fields.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result--><!--Device-RdbStore-updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig,      conflict?: ConflictResolution): Result-End-->

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
| [14800027](../errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## rebuilt

```TypeScript
rebuilt: RebuildType
```

Set whether the database is rebuilt.

**Type:** [RebuildType](arkts-arkdata-relationalstore-rebuildtype-e.md)

**Since:** 23

<!--Device-RdbStore-rebuilt: RebuildType--><!--Device-RdbStore-rebuilt: RebuildType-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## version

```TypeScript
version: number
```

Set RdbStore version. The version number must be an integer greater than 0. Obtains the RdbStore version.

**Type:** number

**Since:** 23

<!--Device-RdbStore-version: int--><!--Device-RdbStore-version: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core
