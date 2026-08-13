# CloudFileCache

云盘文件缓存对象，用来支撑文件管理应用原文件下载流程。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cloudSync-class CloudFileCache--><!--Device-cloudSync-class CloudFileCache-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## cleanFileCache

```TypeScript
cleanFileCache(uri: string): void
```

同步方法删除文件缓存。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-cleanFileCache(uri: string): void--><!--Device-CloudFileCache-cleanFileCache(uri: string): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| 13900002 |
| 14000002 |
| 13900012 |
| 13600001 |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.cleanFileCache(uri);
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`clean file cache failed with error message: ${error.message}, error code: ${error.code}`);
}
```

## cleanFileCache

```TypeScript
cleanFileCache(): Promise<void>
```

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CloudFileCache-cleanFileCache(): Promise<void>--><!--Device-CloudFileCache-cleanFileCache(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900010 |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **CloudFileCache** instance. Data is not shared between multiple instances.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-constructor()--><!--Device-CloudFileCache-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
let fileCache = new cloudSync.CloudFileCache();
```

## getCachedTotalSize

```TypeScript
getCachedTotalSize(): Promise<number>
```

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CloudFileCache-getCachedTotalSize(): Promise<long>--><!--Device-CloudFileCache-getCachedTotalSize(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();

fileCache.getCachedTotalSize().then((totalDownloadSize: number) => {
  console.info("totalDownloadSize: " + totalDownloadSize);
}).catch((err: BusinessError) => {
  console.error("get totalDownloadSize failed with error message: " + err.message + ", error code: " + err.code);
});
```

## offBatchDownload

```TypeScript
offBatchDownload(callback?: Callback<MultiDownloadProgress>): void
```

Unsubscribes from cloud file cache download progress event.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-offBatchDownload(callback?: Callback<MultiDownloadProgress>): void--><!--Device-CloudFileCache-offBatchDownload(callback?: Callback<MultiDownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MultiDownloadProgress](arkts-corefile-cloudsync-multidownloadprogress-c.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |

## offProgress

```TypeScript
offProgress(callback?: Callback<DownloadProgress>): void
```

Unsubscribes from cloud file cache download progress event.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-offProgress(callback?: Callback<DownloadProgress>): void--><!--Device-CloudFileCache-offProgress(callback?: Callback<DownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## off_batchDownload

```TypeScript
off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void
```

云盘文件缓存对象移除由 [on](#on_progress)接口添加的云文 件批量缓存过程事件的监听。

**起始版本：** 20

**废弃版本：** -1

<!--Device-CloudFileCache-off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void--><!--Device-CloudFileCache-off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'batchDownload' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MultiDownloadProgress](arkts-corefile-cloudsync-multidownloadprogress-c.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.MultiDownloadProgress) => {
  console.info("download state: " + pg.state);
}

try {
  fileCache.on('batchDownload', callback);
  fileCache.off('batchDownload', callback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}`);
}
```

## off_progress

```TypeScript
off(event: 'progress', callback?: Callback<DownloadProgress>): void
```

云盘文件缓存对象移除'progress'类型的指定callback回调。

**起始版本：** 11

**废弃版本：** -1

<!--Device-CloudFileCache-off(event: 'progress', callback?: Callback<DownloadProgress>): void--><!--Device-CloudFileCache-off(event: 'progress', callback?: Callback<DownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();

let callback = (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
}

try {
  fileCache.on('progress', callback);
  fileCache.off('progress', callback);
} catch (e) {
  const error = e as BusinessError;
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
```

## onBatchDownload

```TypeScript
onBatchDownload(callback: Callback<MultiDownloadProgress>): void
```

Subscribes to a batch of cloud file cache download progress change event. This method uses a callback to get download progress changes.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-onBatchDownload(callback: Callback<MultiDownloadProgress>): void--><!--Device-CloudFileCache-onBatchDownload(callback: Callback<MultiDownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MultiDownloadProgress](arkts-corefile-cloudsync-multidownloadprogress-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |

## onProgress

```TypeScript
onProgress(callback: Callback<DownloadProgress>): void
```

Subscribes to cloud file cache download progress change event. This method uses a callback to get download progress changes.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-onProgress(callback: Callback<DownloadProgress>): void--><!--Device-CloudFileCache-onProgress(callback: Callback<DownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## on_batchDownload

```TypeScript
on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void
```

添加云文件批量缓存事件的监听。

**起始版本：** 20

**废弃版本：** -1

<!--Device-CloudFileCache-on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void--><!--Device-CloudFileCache-on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'batchDownload' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MultiDownloadProgress](arkts-corefile-cloudsync-multidownloadprogress-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (data: cloudSync.MultiDownloadProgress) => {
  console.info(`Batch download progress: downloadedSize: ${data.downloadedSize}, totalSize: ${data.totalSize}`);
  if (data.state == cloudSync.State.COMPLETED) {
    console.info('Batch download finished.');
  } else if (data.state == cloudSync.State.FAILED) {
    console.info(`Batch download stopped, error type: ${data.errType}.`);
  }
};

try {
  fileCache.on('batchDownload', callback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to register download callback, error code: ${error.code}, message: ${error.message}`);
}
```

## on_progress

```TypeScript
on(event: 'progress', callback: Callback<DownloadProgress>): void
```

添加云盘文件缓存过程事件监听。

**起始版本：** 11

**废弃版本：** -1

<!--Device-CloudFileCache-on(event: 'progress', callback: Callback<DownloadProgress>): void--><!--Device-CloudFileCache-on(event: 'progress', callback: Callback<DownloadProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DownloadProgress&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
};

try {
  fileCache.on('progress', callback);
} catch (e) {
  const error = e as BusinessError;
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
```

## start

```TypeScript
start(uri: string): Promise<void>
```

异步方法启动云盘文件缓存。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-start(uri: string): Promise<void>--><!--Device-CloudFileCache-start(uri: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900002 |
| 14000002 |
| 13900025 |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);

try {
  fileCache.on('progress', (pg: cloudSync.DownloadProgress) => {
    console.info("download state: " + pg.state);
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

## start

```TypeScript
start(uri: string, callback: AsyncCallback<void>): void
```

异步方法启动云盘文件缓存。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-start(uri: string, callback: AsyncCallback<void>): void--><!--Device-CloudFileCache-start(uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900002 |
| 14000002 |
| 13900025 |
| 13600001 |

## 示例

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

## startBatch

```TypeScript
startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>
```

启动云文件批量缓存。使用Promise异步回调。 不同的批量缓存任务可以通过接口返回的任务ID区分。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<long>--><!--Device-CloudFileCache-startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array & lt;string & gt; | 是 |
| fileType | [DownloadFileType](arkts-corefile-cloudsync-downloadfiletype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| 22400004 |
| 14000002 |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
try {
  fileCache.on('batchDownload', (pg: cloudSync.MultiDownloadProgress) => {
    console.info(`batch download state: ${pg.state}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to unregister download callback, error code: ${error.code}, message: ${error.message}`);
}

let uriList: Array<string> = [];
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  console.info(`start batch download successfully, taskId: ${downloadId}`);
}).catch((err: BusinessError) => {
  console.error(`start download failed with error message: ${err.message}, error code: ${err.code}`);
});
```

## stop

```TypeScript
stop(uri: string, needClean?: boolean): Promise<void>
```

Stops downloading a file from the Drive Kit to the local device. This API uses a promise to return the result. When **stop()** is called, the current file download process terminates, and downloaded files are retained by default. You can call **start()** to resume the download.

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-stop(uri: string, needClean?: boolean): Promise<void>--><!--Device-CloudFileCache-stop(uri: string, needClean?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| needClean | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900002 |
| 14000002 |
| 13600001 |

## 示例

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

## stop

```TypeScript
stop(uri: string, callback: AsyncCallback<void>): void
```

异步方法停止云盘文件缓存。使用callback异步回调。 调用stop接口，当前文件下载流程会终止，不删除缓存文件，再次调用start接口重新启动下载。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-stop(uri: string, callback: AsyncCallback<void>): void--><!--Device-CloudFileCache-stop(uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900002 |
| 14000002 |
| 13600001 |

## 示例

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

## stopBatch

```TypeScript
stopBatch(downloadId: number, needClean?: boolean): Promise<void>
```

停止由[startBatch](#startBatch)启动的云文件批量缓存任务。使用Promise异步回调。 调用stopBatch接口会终止当前文件批量缓存流程，未下载完成的缓存文件是否删除由needClean参数决定。

**起始版本：** 23

**废弃版本：** -1

<!--Device-CloudFileCache-stopBatch(downloadId: long, needClean?: boolean): Promise<void>--><!--Device-CloudFileCache-stopBatch(downloadId: long, needClean?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [downloadId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-downloadinfo-i.md) | number | 是 |
| needClean | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 22400005 |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let taskId = -1;
let uriList: Array<string> = [];
let fileCache = new cloudSync.CloudFileCache();
fileCache.startBatch(uriList, cloudSync.DownloadFileType.CONTENT).then((downloadId: number) => {
  taskId = downloadId;
  console.info("start batch download successfully");
}).catch((err: BusinessError) => {
  console.error(`start batch download failed with error message: ${err.message}, error code: ${err.code}`);
});

let needStop = true;
if (needStop && taskId > 0) {
  fileCache.stopBatch(taskId, true).then(() => {
    console.info("stop batch download successfully");
  }).catch((err: BusinessError) => {
    console.error(`stop batch download failed with error message: ${err.message}, error code: ${err.code}`);
  });
}
```
