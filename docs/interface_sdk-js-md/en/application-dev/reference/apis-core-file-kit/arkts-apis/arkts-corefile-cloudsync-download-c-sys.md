# Download (System API)

Provides APIs for downloading image files to **Gallery**. Before using the APIs of **Download**, you need to create a **Download** instance.

**Since:** 23

<!--Device-cloudSync-class Download--><!--Device-cloudSync-class Download-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Download** instance.

**Since:** 23

<!--Device-Download-constructor()--><!--Device-Download-constructor()-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Examples**

```TypeScript
let fileSync = new cloudSync.FileSync()
```

```TypeScript
let gallerySync = new cloudSync.GallerySync()
```

```TypeScript
let download = new cloudSync.Download()
```

```TypeScript
let fileSync = new cloudSync.FileSync("com.ohos.demo")
```

## off_progress

```TypeScript
off(evt: 'progress', callback: (pg: DownloadProgress) => void): void
```

Removes the specified callback from the device-cloud download progress.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-off(evt: 'progress', callback: (pg: DownloadProgress) => void): void--><!--Device-Download-off(evt: 'progress', callback: (pg: DownloadProgress) => void): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| evt | 'progress' | Yes | Event type. The value is **progress**, which indicates the sync progress event. |
| callback | (pg: DownloadProgress) =&gt; void | Yes | Callback used to return the file download progress. The input parameter is [DownloadProgress](arkts-corefile-cloudsync-downloadprogress-i.md), and the return value is **void**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error |

**Examples**

```TypeScript
let download = new cloudSync.Download();

let callback = (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
}

download.on('progress', callback);

download.off('progress', callback);
```

## off_progress

```TypeScript
off(evt: 'progress'): void
```

Removes all callbacks from the device-cloud download progress.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-off(evt: 'progress'): void--><!--Device-Download-off(evt: 'progress'): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| evt | 'progress' | Yes | Event type. The value is **progress**, which indicates the download progress event of a cloud file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error |

**Examples**

```TypeScript
let download = new cloudSync.Download();

download.on('progress', (pg: cloudSync.DownloadProgress) => {
    console.info("download state:" + pg.state);
});

download.off('progress');
```

## offProgress

```TypeScript
offProgress(callback: Callback<DownloadProgress>): void
```

Unsubscribes from download progress event.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-offProgress(callback: Callback<DownloadProgress>): void--><!--Device-Download-offProgress(callback: Callback<DownloadProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | Yes | callback function with a `DownloadProgress` argument. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes: <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13600001 | IPC error |

## offProgress

```TypeScript
offProgress(): void
```

Unsubscribes all callbacks objects from download progress event.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-offProgress(): void--><!--Device-Download-offProgress(): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error |

## on_progress

```TypeScript
on(evt: 'progress', callback: (pg: DownloadProgress) => void): void
```

Registers a listener for the download progress of a cloud file.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-on(evt: 'progress', callback: (pg: DownloadProgress) => void): void--><!--Device-Download-on(evt: 'progress', callback: (pg: DownloadProgress) => void): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| evt | 'progress' | Yes | Event. The value is **progress**, which indicates the download progress event of a cloud file. |
| callback | (pg: DownloadProgress) =&gt; void | Yes | Callback used to return the file download progress. The input parameter is [DownloadProgress](arkts-corefile-cloudsync-downloadprogress-i.md), and the return value is **void**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error |

**Examples**

```TypeScript
let download = new cloudSync.Download();

download.on('progress', (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
});
```

## onProgress

```TypeScript
onProgress(callback: Callback<DownloadProgress>): void
```

Subscribes to download progress change event. This method uses a callback to get download progress changes.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-onProgress(callback: Callback<DownloadProgress>): void--><!--Device-Download-onProgress(callback: Callback<DownloadProgress>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | Yes | callback function with a `DownloadProgress` argument. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes: <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13600001 | IPC error |

## start

```TypeScript
start(uri: string): Promise<void>
```

Starts downloading a cloud file. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-start(uri: string): Promise<void>--><!--Device-Download-start(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the target file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.on('progress', (pg: cloudSync.DownloadProgress) => {
    console.info("download state:" + pg.state);
  });
} catch (e) {
  const error = e as BusinessError;
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}

fileCache.start(uri).then(() => {
  console.info("start download successfully");
}).catch((err: BusinessError) => {
  console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.start(uri, (err: BusinessError) => {
  if (err) {
    console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start download successfully");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
  console.info("syncState: " + pg.state);
});

gallerySync.start().then(() => {
  console.info("start sync successfully");
}).catch((err: BusinessError) => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.start((err: BusinessError) => {
  if (err) {
    console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start sync successfully");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.on('progress', (pg: cloudSync.DownloadProgress) => {
  console.info("download state:" + pg.state);
});

download.start(uri).then(() => {
  console.info("start download successfully");
}).catch((err: BusinessError) => {
  console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.start(uri, (err: BusinessError) => {
  if (err) {
    console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start download successfully");
  }
});
```

## start

```TypeScript
start(uri: string, callback: AsyncCallback<void>): void
```

Starts downloading a cloud file. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-start(uri: string, callback: AsyncCallback<void>): void--><!--Device-Download-start(uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the target file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to start downloading a cloud file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13900002 | No such file or directory. |
| 13900025 | No space left on device. |

**Examples**

See [start](#start)

## stop

```TypeScript
stop(uri: string): Promise<void>
```

Stops downloading a cloud file. This API uses a promise to return the result.

> **NOTE：**&gt;
> Calling **stop** will terminate the download of the current file and clear the cache file. You can use
> **start** to start the download again.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-stop(uri: string): Promise<void>--><!--Device-Download-stop(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the target file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.stop(uri, true).then(() => {
  console.info("stop download successfully");
}).catch((err: BusinessError) => {
  console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

fileCache.stop(uri, (err: BusinessError) => {
  if (err) {
    console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop download successfully");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.stop((err: BusinessError) => {
  if (err) {
    console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop sync successfully");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.stop(uri).then(() => {
  console.info("stop download successfully");
}).catch((err: BusinessError) => {
  console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.stop(uri, (err: BusinessError) => {
  if (err) {
    console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop download successfully");
  }
});
```

## stop

```TypeScript
stop(uri: string, callback: AsyncCallback<void>): void
```

Stops downloading a cloud file. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Calling **stop** will terminate the download of the current file and clear the cache file. You can use
> **start** to start the download again.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-Download-stop(uri: string, callback: AsyncCallback<void>): void--><!--Device-Download-stop(uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the target file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to stop downloading a cloud file. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |

**Examples**

See [stop](#stop)

