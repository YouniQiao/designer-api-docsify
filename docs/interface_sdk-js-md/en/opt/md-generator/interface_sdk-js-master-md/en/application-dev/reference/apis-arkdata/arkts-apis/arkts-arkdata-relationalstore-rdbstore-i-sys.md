# RdbStore

Provides APIs for managing data in an RDB store.

Before using the following APIs, you should obtain an **RdbStore** instance by calling the   
[getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md#getrdbstore) method and then call the corresponding method through the instance.

In addition, use   
[execute](arkts-arkdata-relationalstore-rdbstore-i.md#execute) to initialize the database table structure and related data first, ensuring that the prerequisites for related API calls are met.

**Since:** 9

<!--Device-relationalStore-interface RdbStore--><!--Device-relationalStore-interface RdbStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## cleanDeviceDirtyData

```TypeScript
cleanDeviceDirtyData(table: string, cursor?: number): Promise<void>
```

Cleans dirty data deleted in the cross-device sync.If a cursor is specified, data whose cursor is smaller than the specified cursor is cleaned.Otherwise, all data is cleaned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>--><!--Device-RdbStore-cleanDeviceDirtyData(table: string, cursor?: long): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| cursor | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| 14800043 |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSync

```TypeScript
cloudSync(
      mode: SyncMode,
      predicates: RdbPredicates,
      progress: Callback<ProgressDetails>,
      callback: AsyncCallback<void>
    ): void
```

Sync data to cloud.

**Since:** 11

<!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void--><!--Device-RdbStore-cloudSync(      mode: SyncMode,      predicates: RdbPredicates,      progress: Callback<ProgressDetails>,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProgressDetails&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## cloudSync

```TypeScript
cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>
```

Sync data to cloud.

**Since:** 11

<!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>--><!--Device-RdbStore-cloudSync(mode: SyncMode, predicates: RdbPredicates, progress: Callback<ProgressDetails>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ProgressDetails&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## delete

```TypeScript
delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

Deletes data from the database based on a specified instance object of RdbPredicates.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

Deletes data from the database based on a specified instance object of RdbPredicates.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-delete(table: string, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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

## lockCloudContainer

```TypeScript
lockCloudContainer(): Promise<number>
```

Lock cloud container before non-auto cloud sync.

**Since:** 12

<!--Device-RdbStore-lockCloudContainer(): Promise<int>--><!--Device-RdbStore-lockCloudContainer(): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## query

```TypeScript
query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void
```

Queries data in the database based on specified conditions.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(table: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns: Array<string>,
      callback: AsyncCallback<ResultSet>
    ): void
```

Queries data in the database based on specified conditions.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns: Array<string>,      callback: AsyncCallback<ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## query

```TypeScript
query(
      table: string,
      predicates: dataSharePredicates.DataSharePredicates,
      columns?: Array<string>
    ): Promise<ResultSet>
```

Queries data in the database based on specified conditions.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>--><!--Device-RdbStore-query(      table: string,      predicates: dataSharePredicates.DataSharePredicates,      columns?: Array<string>    ): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array&lt;string&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ResultSet&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Obtains sharing resource of rows corresponding to the predicates.

**Since:** 11

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| columns | Array&lt;string&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ResultSet&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void
```

Obtains sharing resource of rows corresponding to the predicates.

**Since:** 11

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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

## querySharingResource

```TypeScript
querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

Obtains sharing resource of rows corresponding to the predicates.

**Since:** 11

<!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySharingResource(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |
| columns | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
restore(): Promise<void>
```

Restores a database from a specified database file.

**Since:** 12

<!--Device-RdbStore-restore(): Promise<void>--><!--Device-RdbStore-restore(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-uiability-required) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
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

## retainDeviceData

```TypeScript
retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>
```

Remove distributed table remote data.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>--><!--Device-RdbStore-retainDeviceData(retainDevices?: Record<string, Array<string>>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| retainDevices | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;string&gt;&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| 14800043 |
| 14800042 |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |

## unlockCloudContainer

```TypeScript
unlockCloudContainer(): Promise<void>
```

Unlock cloud container.

**Since:** 12

<!--Device-RdbStore-unlockCloudContainer(): Promise<void>--><!--Device-RdbStore-unlockCloudContainer(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## update

```TypeScript
update(
      table: string,
      values: ValuesBucket,
      predicates: dataSharePredicates.DataSharePredicates,
      callback: AsyncCallback<number>
    ): void
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void--><!--Device-RdbStore-update(      table: string,      values: ValuesBucket,      predicates: dataSharePredicates.DataSharePredicates,      callback: AsyncCallback<long>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

Updates data in the database based on a specified instance object of RdbPredicates.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>--><!--Device-RdbStore-update(table: string, values: ValuesBucket, predicates: dataSharePredicates.DataSharePredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800033](../errorcode-data-rdb.md#14800033-sqlite-data-types-mismatch) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |
| [14800032](../errorcode-data-rdb.md#14800032-sqlite-abort-due-to-constraint-violation) |
| [14800034](../errorcode-data-rdb.md#14800034-incorrect-use-of-sqlite-library) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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

## updateDistributedInfo

```TypeScript
updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<number>
```

Update distributed table log.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>--><!--Device-RdbStore-updateDistributedInfo(info: DistributedInfo, predicates: RdbPredicates): Promise<long>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [DistributedInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800024](../errorcode-data-rdb.md#14800024-sqlite-database-file-locked) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14800011](../errorcode-data-rdb.md#14800011-database-file-corrupted) |
| 14800043 |
| [14800015](../errorcode-data-rdb.md#14800015-rdb-store-not-respond) |
| [14800014](../errorcode-data-rdb.md#14800014-target-instance-closed) |
