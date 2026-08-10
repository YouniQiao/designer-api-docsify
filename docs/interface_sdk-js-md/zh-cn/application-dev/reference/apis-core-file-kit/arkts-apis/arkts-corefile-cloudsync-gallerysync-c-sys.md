# GallerySync（系统接口）

云图同步对象，用来支撑图库应用媒体资源端云同步流程。在使用前，需要先创建GallerySync实例。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-cloudSync-class GallerySync--><!--Device-cloudSync-class GallerySync-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

端云同步流程的构造函数，用于获取GallerySync类的实例。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-GallerySync-constructor()--><!--Device-GallerySync-constructor()-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

## 示例

```TypeScript
let gallerySync = new cloudSync.GallerySync()
```

## off

```TypeScript
off(evt: 'progress', callback: (pg: SyncProgress) => void): void
```

云图同步对象移除'progress'类型中指定的callback回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-off(evt: 'progress', callback: (pg: SyncProgress) => void): void--><!--Device-GallerySync-off(evt: 'progress', callback: (pg: SyncProgress) => void): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| evt | 'progress' | 是 | 取消订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | (pg: SyncProgress) =&gt; void | 是 | 回调函数。同步过程事件，入参为[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)，返 回值为void。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## 示例

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

云图同步对象移除'progress'类型的所有回调。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-off(evt: 'progress'): void--><!--Device-GallerySync-off(evt: 'progress'): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| evt | 'progress' | 是 | 取消订阅的事件类型，取值为'progress'（同步过程事件）。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## 示例

```TypeScript
let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
    console.info("syncState: " + pg.state);
});

gallerySync.off('progress');
```

## offProgress

```TypeScript
offProgress(callback: Callback<SyncProgress>): void
```

Unsubscribes from sync progress event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-offProgress(callback: Callback<SyncProgress>): void--><!--Device-GallerySync-offProgress(callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SyncProgress&gt; | 是 | callback function with a `SyncProgress` argument. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## offProgress

```TypeScript
offProgress(): void
```

Unsubscribes all callbacks objects from sync progress event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-offProgress(): void--><!--Device-GallerySync-offProgress(): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## on

```TypeScript
on(evt: 'progress', callback: (pg: SyncProgress) => void): void
```

云图同步对象添加同步过程事件监听。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-on(evt: 'progress', callback: (pg: SyncProgress) => void): void--><!--Device-GallerySync-on(evt: 'progress', callback: (pg: SyncProgress) => void): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| evt | 'progress' | 是 | 订阅的事件类型，取值为'progress'（同步过程事件）。 |
| callback | (pg: SyncProgress) =&gt; void | 是 | 回调函数。同步过程事件，入参为[SyncProgress](arkts-corefile-cloudsync-syncprogress-i.md)，返 回值为void。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## 示例

```TypeScript
let gallerySync = new cloudSync.GallerySync();

gallerySync.on('progress', (pg: cloudSync.SyncProgress) => {
  console.info("syncState: " + pg.state);
});
```

## onProgress

```TypeScript
onProgress(callback: Callback<SyncProgress>): void
```

Subscribes to sync progress change event. This method uses a callback to get sync progress changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-onProgress(callback: Callback<SyncProgress>): void--><!--Device-GallerySync-onProgress(callback: Callback<SyncProgress>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SyncProgress&gt; | 是 | callback function with a `SyncProgress` argument. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: &lt;br&gt;1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error |

## start

```TypeScript
start(): Promise<void>
```

启动端云同步。使用Promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-start(): Promise<void>--><!--Device-GallerySync-start(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 22400001 | Cloud status not ready. |
| 22400003 | Low battery level. |
| 22400002 | Network unavailable. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |

## 示例

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

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

异步方法启动端云同步。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-start(callback: AsyncCallback<void>): void--><!--Device-GallerySync-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。异步启动端云同步。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 22400001 | Cloud status not ready. |
| 22400003 | Low battery level. |
| 22400002 | Network unavailable. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |

## 示例

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

## stop

```TypeScript
stop(): Promise<void>
```

异步方法停止端云同步。使用Promise异步回调。

> **说明：**
> 
> 调用stop接口，同步流程会停止。再次调用[start](arkts-corefile-cloudsync-gallerysync-c-sys.md#start)接口会继续同步。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-stop(): Promise<void>--><!--Device-GallerySync-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |

## 示例

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

异步方法停止端云同步。使用callback异步回调。

> **说明：**
> 
> 调用stop接口，同步流程会停止。再次调用[start](arkts-corefile-cloudsync-gallerysync-c-sys.md#start)接口会继续同步。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-GallerySync-stop(callback: AsyncCallback<void>): void--><!--Device-GallerySync-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。异步停止端云同步。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |

## 示例

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

