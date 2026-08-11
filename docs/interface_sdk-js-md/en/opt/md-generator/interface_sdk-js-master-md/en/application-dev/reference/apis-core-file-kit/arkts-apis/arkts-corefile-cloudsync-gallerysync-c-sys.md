# GallerySync (System API)

Provides APIs to implement device-cloud sync of media assets in **Gallery**. Before using the APIs of  
**GallerySync**, you need to create a **GallerySync** instance.

**Since:** 10

<!--Device-cloudSync-class GallerySync--><!--Device-cloudSync-class GallerySync-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **GallerySync** instance.

**Since:** 10

<!--Device-GallerySync-constructor()--><!--Device-GallerySync-constructor()-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

## Examples

```TypeScript
let gallerySync = new cloudSync.GallerySync()
```

## off

```TypeScript
off(evt: 'progress', callback: (pg: SyncProgress) => void): void
```

Removes the specified callback from the device-cloud sync progress.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-off(evt: 'progress', callback: (pg: SyncProgress) => void): void--><!--Device-GallerySync-off(evt: 'progress', callback: (pg: SyncProgress) => void): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| evt | 'progress' | Yes |
| callback | (pg: SyncProgress) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
let gallerySync = new cloudSync.GallerySync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("gallery sync state: " + pg.state + "error type: " + pg.error);
}

gallerySync.on('progress', callback);

gallerySync.off('progress', callback);
```

## off

```TypeScript
off(evt: 'progress'): void
```

Removes all callbacks from the device-cloud sync progress.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-off(evt: 'progress'): void--><!--Device-GallerySync-off(evt: 'progress'): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| evt | 'progress' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
    console.info("syncState: " + pg.state);
});

gallerySync.off('progress');
```

## on

```TypeScript
on(evt: 'progress', callback: (pg: SyncProgress) => void): void
```

Registers a listener for the device-cloud sync progress.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-on(evt: 'progress', callback: (pg: SyncProgress) => void): void--><!--Device-GallerySync-on(evt: 'progress', callback: (pg: SyncProgress) => void): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| evt | 'progress' | Yes |
| callback | (pg: SyncProgress) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
  console.info("syncState: " + pg.state);
});
```

## start

```TypeScript
start(): Promise<void>
```

Starts device-cloud sync. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-start(): Promise<void>--><!--Device-GallerySync-start(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 22400001 |
| 22400003 |
| 22400002 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts device-cloud sync. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-start(callback: AsyncCallback<void>): void--><!--Device-GallerySync-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 22400001 |
| 22400003 |
| 22400002 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

## stop

```TypeScript
stop(): Promise<void>
```

Stops device-cloud sync. This API uses a promise to return the result.

> **NOTE：**
> 
> Calling **stop** will stop the sync process. To resume the sync, call
> [start](arkts-corefile-cloudsync-gallerysync-c-sys.md#start).

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-stop(): Promise<void>--><!--Device-GallerySync-stop(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops device-cloud sync. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Calling **stop** will stop the sync process. To resume the sync, call
> [start](arkts-corefile-cloudsync-gallerysync-c-sys.md#start).

**Since:** 10

**Required permissions:** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-stop(callback: AsyncCallback<void>): void--><!--Device-GallerySync-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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
