# FileSync

Provides APIs for the file manager application to perform device-cloud sync of the files stored in the Drive Kit. Before using the APIs of this class, you need to create a **FileSync** instance.

**Since:** 23

<!--Device-cloudSync-class FileSync--><!--Device-cloudSync-class FileSync-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'cloudSync';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **FileSync** instance.

**Since:** 23

<!--Device-FileSync-constructor()--><!--Device-FileSync-constructor()-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:Incorrect parameter types. |

**Examples**

```TypeScript
let fileSync = new cloudSync.FileSync()
```

## getLastSyncTime

```TypeScript
getLastSyncTime(): Promise<long>
```

Obtains the last sync time. This API uses a promise to return the result.

**Since:** 23

<!--Device-FileSync-getLastSyncTime(): Promise<long>--><!--Device-FileSync-getLastSyncTime(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the last sync time. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime().then((timeStamp: number) => {
  let date = new Date(timeStamp);
  console.info("get last sync time successfully:"+ date);
}).catch((err: BusinessError) => {
  console.error("get last sync time failed with error message: " + err.message + ", error code: " + err.code);
});
```

## getLastSyncTime

```TypeScript
getLastSyncTime(callback: AsyncCallback<long>): void
```

Obtains the last sync time. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void--><!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to obtain the last sync time. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime((err: BusinessError, timeStamp: number) => {
  if (err) {
    console.error("get last sync time with error message: " + err.message + ", error code: " + err.code);
  } else {
    let date = new Date(timeStamp);
    console.info("get last sync time successfully:"+ date);
  }
});
```

## offProgress

```TypeScript
offProgress(callback?: Callback<SyncProgress>): void
```

Unsubscribes from sync progress event.

**Since:** 23

<!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void--><!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | No | callback function with a `SyncProgress` argument. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error |

## off_progress

```TypeScript
off(event: 'progress', callback?: Callback<SyncProgress>): void
```

Removes the specified callback from the device-cloud sync progress.

**Since:** 12

<!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void--><!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | No | Callback used to return the sync progress. The default value is null. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 13600001 | IPC error |

**Examples**

```TypeScript
let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);

fileSync.off('progress', callback);
```

## onProgress

```TypeScript
onProgress(callback: Callback<SyncProgress>): void
```

Subscribes to sync progress change event. This method uses a callback to get sync progress changes.

**Since:** 23

<!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void--><!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | Yes | callback function with a `SyncProgress` argument. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes: <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13600001 | IPC error |

## on_progress

```TypeScript
on(event: 'progress', callback: Callback<SyncProgress>): void
```

Registers a listener for the device-cloud sync progress.

**Since:** 12

<!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void--><!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | Yes | Callback used to return the sync progress. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error |

**Examples**

```TypeScript
let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);
```

## start

```TypeScript
start(): Promise<void>
```

Starts device-cloud sync of a file. This API uses a promise to return the result.

**Since:** 23

<!--Device-FileSync-start(): Promise<void>--><!--Device-FileSync-start(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 22400001 | Cloud status not ready. |
| 22400003 | Low battery level. |
| 22400002 | Network unavailable. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type:" + pg.error);
}

fileSync.on('progress', callback);

fileSync.start().then(() => {
  console.info("start sync successfully");
}).catch((err: BusinessError) => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts device-cloud sync of a file. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-FileSync-start(callback: AsyncCallback<void>): void--><!--Device-FileSync-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to start device-cloud sync. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 22400001 | Cloud status not ready. |
| 22400003 | Low battery level. |
| 22400002 | Network unavailable. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.start((err: BusinessError) => {
  if (err) {
    console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start sync successfully");
  }
});
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops device-cloud sync of a file. This API uses a promise to return the result. Calling **stop** will stop the sync process. To resume the sync, call [start](#start).

**Since:** 23

<!--Device-FileSync-stop(): Promise<void>--><!--Device-FileSync-stop(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops device-cloud sync of a file. This API uses an asynchronous callback to return the result. Calling **stop** will stop the sync process. To resume the sync, call [start](#start).

**Since:** 23

<!--Device-FileSync-stop(callback: AsyncCallback<void>): void--><!--Device-FileSync-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to stop device-cloud sync. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.stop((err: BusinessError) => {
  if (err) {
    console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop sync successfully");
  }
});
```

