# FileSync

云盘同步对象，用于支撑文件管理器应用完成云盘文件的端云同步流程。在使用前，需要先创建FileSync实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cloudSync-class FileSync--><!--Device-cloudSync-class FileSync-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## constructor

```TypeScript
constructor()
```

端云同步流程的构造函数，用于获取FileSync类的实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-constructor()--><!--Device-FileSync-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
let fileSync = new cloudSync.FileSync()
```

## getLastSyncTime

```TypeScript
getLastSyncTime(): Promise<number>
```

异步方法获取上次同步时间。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-getLastSyncTime(): Promise<long>--><!--Device-FileSync-getLastSyncTime(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

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

## getLastSyncTime

```TypeScript
getLastSyncTime(callback: AsyncCallback<number>): void
```

获取上次同步时间。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void--><!--Device-FileSync-getLastSyncTime(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

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

## offProgress

```TypeScript
offProgress(callback?: Callback<SyncProgress>): void
```

Unsubscribes from sync progress event.

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void--><!--Device-FileSync-offProgress(callback?: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## off_progress

```TypeScript
off(event: 'progress', callback?: Callback<SyncProgress>): void
```

云盘同步对象移除'progress'类型的指定callback回调。

**起始版本：** 12

**废弃版本：** -1

<!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void--><!--Device-FileSync-off(event: 'progress', callback?: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

```TypeScript
let fileSync = new cloudSync.FileSync();

let callback = (pg: cloudSync.SyncProgress) => {
  console.info(`file sync state: ${pg.state}, error type: ${pg.error}`);
}

fileSync.on('progress', callback);

fileSync.off('progress', callback);
```

## onProgress

```TypeScript
onProgress(callback: Callback<SyncProgress>): void
```

Subscribes to sync progress change event. This method uses a callback to get sync progress changes.

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void--><!--Device-FileSync-onProgress(callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## on_progress

```TypeScript
on(event: 'progress', callback: Callback<SyncProgress>): void
```

云盘同步对象添加同步过程事件监听。

**起始版本：** 12

**废弃版本：** -1

<!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void--><!--Device-FileSync-on(event: 'progress', callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

```TypeScript
let fileSync = new cloudSync.FileSync();
let callback = (pg: cloudSync.SyncProgress) => {
  console.info(`file sync state: ${pg.state}, error type: ${pg.error}`);
}

fileSync.on('progress', callback);
```

## start

```TypeScript
start(): Promise<void>
```

异步方法启动云盘端云同步。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-start(): Promise<void>--><!--Device-FileSync-start(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 22400001 |
| 22400003 |
| 22400002 |
| 13600001 |

## 示例

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

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

异步方法启动云盘端云同步。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-start(callback: AsyncCallback<void>): void--><!--Device-FileSync-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 22400001 |
| 22400003 |
| 22400002 |
| 13600001 |

## 示例

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

异步方法停止云盘端云同步。使用Promise异步回调。 调用stop接口，同步流程会停止。再次调用[start](#start)接口会继续同步。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-stop(): Promise<void>--><!--Device-FileSync-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

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

异步方法停止云盘端云同步。使用callback异步回调。 调用stop接口，同步流程会停止。再次调用[start](#start)接口会继续同步。

**起始版本：** 23

**废弃版本：** -1

<!--Device-FileSync-stop(callback: AsyncCallback<void>): void--><!--Device-FileSync-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |

## 示例

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
