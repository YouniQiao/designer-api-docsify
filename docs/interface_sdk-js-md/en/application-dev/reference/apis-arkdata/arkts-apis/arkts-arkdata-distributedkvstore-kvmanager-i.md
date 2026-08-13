# KVManager

Provides an instance to obtain information about a distributed KV store. Before calling any API in **KVManager**, you must use [createKVManager](arkts-arkdata-distributedkvstore-createkvmanager-f.md#createKVManager) to create a **KVManager** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-distributedKVStore-interface KVManager--><!--Device-distributedKVStore-interface KVManager-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## closeKVStore

```TypeScript
closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void
```

Closes a distributed KV store. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void--><!--Device-KVManager-closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |
| storeId | string | Yes | Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.closeKVStore(appId, 'storeId', (err: BusinessError)=> {
        if (err != undefined) {
          console.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in closing KVStore');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

## closeKVStore

```TypeScript
closeKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>
```

Closes a distributed KV store. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-closeKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>--><!--Device-KVManager-closeKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |
| storeId | string | Yes | Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| kvConfig | Options | No | Indicates the {@code Options} object used for close the KVStore database.<br>**Since:** 24 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |

## deleteKVStore

```TypeScript
deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void
```

Deletes a distributed KV store. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void--><!--Device-KVManager-deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |
| [15100004](../errorcode-distributedKVStore.md#15100004-failed-to-find-data) | Not found. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId is the one in createKVManager.
      kvManager.deleteKVStore(appId, 'storeId', (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info(`Succeeded in deleting KVStore`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to delete KVStore.code is ${error.code},message is ${error.message}`);
}
```

## deleteKVStore

```TypeScript
deleteKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>
```

Deletes a distributed KV store. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-deleteKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>--><!--Device-KVManager-deleteKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |
| storeId | string | Yes | Unique identifier of the KV store to delete. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| kvConfig | Options | No | Indicates the {@code Options} object used for delete the KVStore database.<br>**Since:** 24 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |
| [15100004](../errorcode-distributedKVStore.md#15100004-failed-to-find-data) | Not found. |

## getAllKVStoreId

```TypeScript
getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void
```

Obtains the IDs of all distributed KV stores that are created by getKVStore and have not been deleted by [deleteKVStore](#deleteKVStore) . This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void--><!--Device-KVManager-getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string[]&gt; | Yes | Callback used to return the IDs of all the distributed KV stores created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId is the one in createKVManager.
  kvManager.getAllKVStoreId(appId, (err: BusinessError, data: string[]) => {
    if (err != undefined) {
      console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting AllKVStoreId');
    console.info(`GetAllKVStoreId size = ${data.length}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
}
```

## getAllKVStoreId

```TypeScript
getAllKVStoreId(appId: string): Promise<string[]>
```

Obtains the IDs of all distributed KV stores that are created by getKVStore and have not been deleted by [deleteKVStore](#deleteKVStore) . This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-getAllKVStoreId(appId: string): Promise<string[]>--><!--Device-KVManager-getAllKVStoreId(appId: string): Promise<string[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Bundle name of the application. The value cannot be empty or exceed 256 bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string[]&gt; | Promise used to return the IDs of all the distributed KV stores created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId is the one in createKVManager.
  console.info('GetAllKVStoreId');
  kvManager.getAllKVStoreId(appId).then((data: string[]) => {
    console.info('Succeeded in getting AllKVStoreId');
    console.info(`GetAllKVStoreId size = ${data.length}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
}
```

## getKVStore

```TypeScript
getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void
```

Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses an asynchronous callback to return the result. > **NOTE：**> > If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV > store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV > store instance. For important data that cannot be regenerated, you are advised to use the backup and restore > feature to prevent data loss. For details, see > [Database Backup and Restoration](../../../database/data-backup-and-restore.md).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void--><!--Device-KVManager-getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| storeId | string | Yes | Unique identifier of the KV store. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| options | Options | Yes | Configuration of the KV store to create. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | Yes | Callback used to return the **SingleKVStore** or **DeviceKVStore** instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types; &lt;br&gt;3.Parameter verification failed. |
| [15100002](../errorcode-distributedKVStore.md#15100002-parameter-configuration-changes) | Open existed database with changed options. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore('storeId', options, (err: BusinessError, store: distributedKVStore.SingleKVStore) => {
    if (err) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info("Succeeded in getting KVStore");
    kvStore = store;
    if (kvStore !== null) {
       // Perform subsequent data operations, such as adding, deleting, modifying, and querying data, and subscribing to data changes.
       // ...
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

## getKVStore

```TypeScript
getKVStore<T>(storeId: string, options: Options): Promise<T>
```

Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses a promise to return the result. > **NOTE：**> > If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV > store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV > store instance. For important data that cannot be regenerated, you are advised to use the backup and restore > feature to prevent data loss. For details, see > [Database Backup and Restoration](../../../database/data-backup-and-restore.md).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-getKVStore<T>(storeId: string, options: Options): Promise<T>--><!--Device-KVManager-getKVStore<T>(storeId: string, options: Options): Promise<T>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| storeId | string | Yes | Unique identifier of the KV store. The KV store ID allows only letters, digits, and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH](arkts-arkdata-distributedkvstore-constants-i.md#Constants) in length. |
| options | Options | Yes | Configuration of the KV store to create. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;T&gt; | Promise used to return the **SingleKVStore** or **DeviceKVStore** instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types; &lt;br&gt;3.Parameter verification failed. |
| [15100002](../errorcode-distributedKVStore.md#15100002-parameter-configuration-changes) | Open existed database with changed options. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then((store: distributedKVStore.SingleKVStore) => {
    console.info("Succeeded in getting KVStore");
    kvStore = store;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

## offDistributedDataServiceDie

```TypeScript
offDistributedDataServiceDie(deathCallback?: Callback<void>): void
```

Unregister the death callback. Not notification will be received when the data manager service is terminated. &lt;p&gt;The unregistered death callback must be a registered death callback of the database. If no death callback parameter is passed, all database death callbacks will be unregistered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-offDistributedDataServiceDie(deathCallback?: Callback<void>): void--><!--Device-KVManager-offDistributedDataServiceDie(deathCallback?: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deathCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | the data manager service is terminated callback which has been registered. |

## off_distributedDataServiceDie

```TypeScript
off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void
```

Unsubscribes from the termination (death) of the distributed data service. The **deathCallback** parameter must be a callback registered for subscribing to the termination of the distributed data service. Otherwise, the unsubscription will fail.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-KVManager-off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void--><!--Device-KVManager-off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'distributedDataServiceDie' | Yes | Event type. The value is **distributedDataServiceDie**, which indicates the termination of the distributed data service. |
| deathCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the **distributedDataServiceDie** event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types; &lt;br&gt;3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOff');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

## onDistributedDataServiceDie

```TypeScript
onDistributedDataServiceDie(deathCallback: Callback<void>): void
```

Register a death callback to get notification when the data manager service is terminated. &lt;p&gt;If the data manager service is terminated,you need to re-subscribe to data change notifications and synchronization completion notifications, and calling the sync method will return a failure.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KVManager-onDistributedDataServiceDie(deathCallback: Callback<void>): void--><!--Device-KVManager-onDistributedDataServiceDie(deathCallback: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deathCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | callback to be invoked when the data manager service is terminated. |

## on_distributedDataServiceDie

```TypeScript
on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void
```

Subscribes to the termination (death) of the distributed data service. If the service is terminated, you need to register the callbacks for data change notifications and cross-device sync completion notifications again. In addition, an error will be returned for a sync operation.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-KVManager-on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void--><!--Device-KVManager-on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'distributedDataServiceDie' | Yes | Event type. The value is **distributedDataServiceDie**, which indicates the termination of the distributed data service. |
| deathCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the subscription is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types; &lt;br&gt;3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOn');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

