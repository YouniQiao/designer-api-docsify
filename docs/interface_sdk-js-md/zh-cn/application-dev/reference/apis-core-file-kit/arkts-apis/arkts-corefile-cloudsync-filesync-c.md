# FileSync

云盘同步对象，用于支撑文件管理器应用完成云盘文件的端云同步流程。在使用前，需要先创建FileSync实例。

**起始版本：** 23

<!--Device-cloudSync-class FileSync--><!--Device-cloudSync-class FileSync-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## 导入模块

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

端云同步流程的构造函数，用于获取FileSync类的实例。

**起始版本：** 23

<!--Device-FileSync-constructor()--><!--Device-FileSync-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:Incorrect parameter types. |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync()
```

```TypeScript
let fileCache = new cloudSync.CloudFileCache();
```

```TypeScript
let fileVersion = new cloudSync.FileVersion();
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

```TypeScript
let fileCache = new cloudSync.CloudFileCache("com.ohos.demo");
```

## getLastSyncTime

```TypeScript
getLastSyncTime(): Promise<long>
```

异步方法获取上次同步时间。使用Promise异步回调。

**起始版本：** 23

<!--Device-FileSync-getLastSyncTime(): Promise<long>--><!--Device-FileSync-getLastSyncTime(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;long&gt; | Promise对象，返回上次同步时间。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime().then((timeStamp: number) => {
  let date = new Date(timeStamp);
  console.info("get last sync time successfully: "+ date);
}).catch((err: BusinessError) => {
  console.error("get last sync time failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
fileSync.getLastSyncTime().then<long>((timeStamp: long): void => {
  let date = new Date(timeStamp);
  console.info("get last sync time successfully: "+ date);
}).catch((err: BusinessError<void>): void => {
  console.error("get last sync time failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.getLastSyncTime((err: BusinessError, timeStamp: number) => {
  if (err) {
    console.error("get last sync time with error message: " + err.message + ", error code: " + err.code);
  } else {
    let date = new Date(timeStamp);
    console.info("get last sync time successfully: "+ date);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
fileSync.getLastSyncTime((err: BusinessError<void> | null, timeStamp: long | undefined): void => {
  if (err && err.code) {
    console.error("get last sync time with error message: " + err.message + ", error code: " + err.code);
  } else {
    if (timeStamp == undefined) {
      console.error("get last sync time successfully, but timeStamp is undefined.");
      return;
    }
    let date = new Date(timeStamp);
    console.info("get last sync time successfully: "+ date);
  }
});
```

## getLastSyncTime

```TypeScript
getLastSyncTime(callback: AsyncCallback<long>): void
```

获取上次同步时间。使用callback异步回调。

**起始版本：** 23

<!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void--><!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 | 回调函数。异步获取上次同步时间。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error. |

**示例**

参见 [getLastSyncTime](#getlastsynctime)

## off_progress

```TypeScript
off(event: 'progress', callback?: Callback<SyncProgress>): void
```

云盘同步对象移除'progress'类型的指定callback回调。

**起始版本：** 12

<!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void--><!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'progress' | 是 | 取消订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 否 | 回调函数。同步过程事件， 默认值为null。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 13600001 | IPC error |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info(`file sync state: ${pg.state}, error type: ${pg.error}`);
}

fileSync.on('progress', callback);

fileSync.off('progress', callback);
```

## offProgress

```TypeScript
offProgress(callback?: Callback<SyncProgress>): void
```

Unsubscribes from sync progress event.

**起始版本：** 23

<!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void--><!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 否 | callback function with a `SyncProgress` argument. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("file sync state: " + pg.state + "error type: " + pg.error);
}
fileSync.onProgress(callback);
fileSync.offProgress(callback);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state);
}
try {
  fileCache.onProgress(callback);
  fileCache.offProgress(callback);
} catch (error) {
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
let gallerySync = new cloudSync.GallerySync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("gallery sync state: " + pg.state + "error type: " + pg.error);
}
gallerySync.onProgress(callback);
gallerySync.offProgress(callback);
```

```TypeScript
let gallerySync = new cloudSync.GallerySync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("gallery sync state: " + pg.state + "error type: " + pg.error);
}
gallerySync.onProgress(callback);
gallerySync.offProgress();
```

```TypeScript
let download = new cloudSync.Download();
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state);
}
download.onProgress(callback);
download.offProgress(callback);
```

```TypeScript
let download = new cloudSync.Download();
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state);
}
download.onProgress(callback);
download.offProgress();
```

## on_progress

```TypeScript
on(event: 'progress', callback: Callback<SyncProgress>): void
```

云盘同步对象添加同步过程事件监听。

**起始版本：** 12

<!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void--><!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'progress' | 是 | 订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 是 | 回调函数。同步过程事件。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress) => {
  console.info(`file sync state: ${pg.state}, error type: ${pg.error}`);
}

fileSync.on('progress', callback);
```

## onProgress

```TypeScript
onProgress(callback: Callback<SyncProgress>): void
```

Subscribes to sync progress change event. This method uses a callback to get sync progress changes.

**起始版本：** 23

<!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void--><!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 是 | callback function with a `SyncProgress` argument. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes: <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 13600001 | IPC error |

**示例**

```TypeScript
let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("file sync state: " + pg.state + "error type: " + pg.error);
}
fileSync.onProgress(callback);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileCache = new cloudSync.CloudFileCache();
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state);
};
try {
  fileCache.onProgress(callback);
} catch (error) {
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("syncState: " + pg.state);
};
try {
  gallerySync.onProgress(callback);
} catch (error) {
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
let download = new cloudSync.Download();
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state + "error type: " + pg.error);
}
download.onProgress(callback);
```

## start

```TypeScript
start(): Promise<void>
```

异步方法启动云盘端云同步。使用Promise异步回调。

**起始版本：** 23

<!--Device-FileSync-start(): Promise<void>--><!--Device-FileSync-start(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info("file sync state: " + pg.state + "error type: " + pg.error);
}

fileSync.on('progress', callback);

fileSync.start().then(() => {
  console.info("start sync successfully");
}).catch((err: BusinessError) => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("file sync state: " + pg.state + "error type: " + pg.error);
}
fileSync.on('progress', callback);
fileSync.start().then<void>((): void => {
  console.info("start sync successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
fileSync.start((err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start sync successfully");
  }
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
try {
  fileCache.on('progress', (pg: cloudSync.DownloadProgress): void => {
    console.info("download state: " + pg.state);
  });
} catch (error) {
  console.error(`Error code: ${error.code}, message: ${error.message}`);
}
fileCache.start(uri).then<void>((): void => {
  console.info("start download successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
fileCache.start(uri, (err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start download successfully");
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
  console.info("syncState: " + pg.state);
});

gallerySync.start().then(() => {
  console.info("start sync successfully");
}).catch((err: BusinessError) => {
  console.error(`start sync failed with error message: ${err.message}, error code: ${err.code}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();
let callback = (pg: cloudSync.SyncProgress): void => {
  console.info("gallery sync state: " + pg.state + "error type: " + pg.error);
}
gallerySync.onProgress(callback);
gallerySync.start().then((): void => {
  console.info("start sync successfully");
}).catch((err: BusinessError): void => {
  console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.start((err: BusinessError) => {
  if (err) {
    console.error(`start sync failed with error message: ${err.message}, error code: ${err.code}`);
  } else {
    console.info("start sync successfully");
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();
gallerySync.start((err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("start sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start sync successfully");
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.on('progress', (pg: cloudSync.DownloadProgress) => {
  console.info("download state: " + pg.state);
});

download.start(uri).then(() => {
  console.info("start download successfully");
}).catch((err: BusinessError) => {
  console.error(`start download failed with error message: ${err.message}, error code: ${err.code}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";
let callback = (pg: cloudSync.DownloadProgress): void => {
  console.info("download state: " + pg.state);
}
download.on('progress', callback);
download.start(uri).then<void>((): void => {
  console.info("start download successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.start(uri, (err: BusinessError) => {
  if (err) {
    console.error(`start download failed with error message: ${err.message}, error code: ${err.code}`);
  } else {
    console.info("start download successfully");
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";
download.start(uri, (err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("start download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("start download successfully");
  }
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

异步方法启动云盘端云同步。使用callback异步回调。

**起始版本：** 23

<!--Device-FileSync-start(callback: AsyncCallback<void>): void--><!--Device-FileSync-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。异步启动端云同步。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 13600001 | IPC error. |
| 22400001 | Cloud status not ready. |
| 22400002 | Network unavailable. |
| 22400003 | Low battery level. |

**示例**

参见 [start](#start)

## stop

```TypeScript
stop(): Promise<void>
```

异步方法停止云盘端云同步。使用Promise异步回调。调用stop接口，同步流程会停止。再次调用[start](#start)接口会继续同步。

**起始版本：** 23

<!--Device-FileSync-stop(): Promise<void>--><!--Device-FileSync-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 13600001 | IPC error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();

fileSync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
fileSync.stop().then<void>((): void => {
  console.info("stop sync successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let fileSync = new cloudSync.FileSync();
fileSync.stop((err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop sync successfully");
  }
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
fileCache.stop(uri, true).then<void>((): void => {
  console.info("stop download successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let fileCache = new cloudSync.CloudFileCache();
let path: string = "/data/storage/el2/cloud/1.txt";
let uri: string = fileUri.getUriFromPath(path);
fileCache.stop(uri, (err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop download successfully");
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.stop().then(() => {
  console.info("stop sync successfully");
}).catch((err: BusinessError) => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();
gallerySync.stop().then<void>((): void => {
  console.info("stop sync successfully");
}, (err: BusinessError<void>): void => {
  console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();

gallerySync.stop((err: BusinessError) => {
  if (err) {
    console.error(`stop sync failed with error message: ${err.message}, error code: ${err.code}`);
  } else {
    console.info("stop sync successfully");
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let gallerySync = new cloudSync.GallerySync();
gallerySync.stop((err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("stop sync failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop sync successfully");
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.stop(uri).then(() => {
  console.info("stop download successfully");
}).catch((err: BusinessError) => {
  console.error(`stop download failed with error message: ${err.message}, error code: ${err.code}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";
download.stop(uri).then<void>((): void => {
  console.info("stop download successfully");
}).catch((err: BusinessError<void>): void => {
  console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";

download.stop(uri, (err: BusinessError) => {
  if (err) {
    console.error(`stop download failed with error message: ${err.message}, error code: ${err.code}`);
  } else {
    console.info("stop download successfully");
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let download = new cloudSync.Download();
let uri: string = "file:///media/Photo/1";
download.stop(uri, (err: BusinessError<void> | null): void => {
  if (err && err.code) {
    console.error("stop download failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("stop download successfully");
  }
});
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

异步方法停止云盘端云同步。使用callback异步回调。调用stop接口，同步流程会停止。再次调用[start](#start)接口会继续同步。

**起始版本：** 23

<!--Device-FileSync-stop(callback: AsyncCallback<void>): void--><!--Device-FileSync-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。异步停止端云同步。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameter types. |
| 13600001 | IPC error. |

**示例**

参见 [stop](#stop)

