# DownloadTask

下载任务，使用下列方法前，需要先获取DownloadTask对象，promise形式通过 [request.downloadFile](arkts-basicservices-request-downloadfile-f.md)获取，callback形式通过 [request.downloadFile](arkts-basicservices-request-downloadfile-f.md) 获取。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.Download

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## delete

```TypeScript
delete(callback: AsyncCallback<boolean>): void
```

移除下载的任务，使用callback异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## delete

```TypeScript
delete(): Promise<boolean>
```

移除下载的任务，使用Promise异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getTaskInfo

```TypeScript
getTaskInfo(callback: AsyncCallback<DownloadInfo>): void
```

查询下载的任务，使用callback异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DownloadInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getTaskInfo

```TypeScript
getTaskInfo(): Promise<DownloadInfo>
```

查询下载任务的信息，使用Promise异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;DownloadInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getTaskMimeType

```TypeScript
getTaskMimeType(callback: AsyncCallback<string>): void
```

查询下载任务的 MimeType（HTTP中表示资源的媒体类型），使用callback异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getTaskMimeType

```TypeScript
getTaskMimeType(): Promise<string>
```

查询下载的任务的MimeType(HTTP中表示资源的媒体类型)，使用Promise异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## off('progress')

```TypeScript
off(type: 'progress', callback?: (receivedSize: number, totalSize: number) => void): void
```

取消订阅下载任务进度事件。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progress' | 是 |
| callback | (receivedSize: number, totalSize: number) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('complete' | 'pause' | 'remove')

```TypeScript
off(type: 'complete' | 'pause' | 'remove', callback?: () => void): void
```

取消订阅下载任务相关的事件。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('complete' | 'pause' | 'remove')

```TypeScript
off(type: 'complete' | 'pause' | 'remove', callback?: () => void): void
```

取消订阅下载任务相关的事件。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('complete' | 'pause' | 'remove')

```TypeScript
off(type: 'complete' | 'pause' | 'remove', callback?: () => void): void
```

取消订阅下载任务相关的事件。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('fail')

```TypeScript
off(type: 'fail', callback?: (err: number) => void): void
```

取消订阅下载任务失败事件。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'fail' | 是 |
| callback | (err: number) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('progress')

```TypeScript
on(type: 'progress', callback: (receivedSize: number, totalSize: number) => void): void
```

订阅下载任务进度事件，使用callback异步回调。

> **说明：**&gt;
> 应用处于后台时，为满足功耗性能要求，不支持调用此接口进行回调。

**起始版本：** 6

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progress' | 是 |
| callback | (receivedSize: number, totalSize: number) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('complete' | 'pause' | 'remove')

```TypeScript
on(type: 'complete' | 'pause' | 'remove', callback: () => void): void
```

订阅下载任务相关的事件，使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('complete' | 'pause' | 'remove')

```TypeScript
on(type: 'complete' | 'pause' | 'remove', callback: () => void): void
```

订阅下载任务相关的事件，使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('complete' | 'pause' | 'remove')

```TypeScript
on(type: 'complete' | 'pause' | 'remove', callback: () => void): void
```

订阅下载任务相关的事件，使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'complete' \| 'pause' \| 'remove' | 是 |
| callback | () = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('fail')

```TypeScript
on(type: 'fail', callback: (err: number) => void): void
```

订阅下载任务失败事件，使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'fail' | 是 |
| callback | (err: number) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停下载正在运行中的任务，使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [suspend](#suspend)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [suspend](#suspend)(callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## pause

```TypeScript
pause(): Promise<void>
```

暂停下载正在运行中的任务，使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用[suspend](#suspend)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [suspend](#suspend)()

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## query

```TypeScript
query(callback: AsyncCallback<DownloadInfo>): void
```

查询下载任务，返回下载任务的信息，使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [getTaskInfo](#gettaskinfo)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTaskInfo](#gettaskinfo)(callback: AsyncCallback&lt;DownloadInfo&gt;)

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DownloadInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## query

```TypeScript
query(): Promise<DownloadInfo>
```

查询下载任务，返回下载任务的信息，使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃,建议使用[getTaskInfo](#gettaskinfo)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTaskInfo](#gettaskinfo)()

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;DownloadInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## queryMimeType

```TypeScript
queryMimeType(callback: AsyncCallback<string>): void
```

查询下载的任务的MimeType，使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [getTaskMimeType](#gettaskmimetype)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTaskMimeType](#gettaskmimetype)(callback: AsyncCallback&lt;string&gt;)

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## queryMimeType

```TypeScript
queryMimeType(): Promise<string>
```

查询下载任务的MimeType，使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用[getTaskMimeType](#gettaskmimetype)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getTaskMimeType](#gettaskmimetype)()

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## remove

```TypeScript
remove(callback: AsyncCallback<boolean>): void
```

移除下载的任务，使用callback异步回调。

> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [delete](arkts-basicservices-request-uploadtask-i.md#delete)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [delete](arkts-basicservices-request-uploadtask-i.md#delete)(callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## remove

```TypeScript
remove(): Promise<boolean>
```

移除下载的任务，使用Promise异步回调。

> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃，建议使用[delete](arkts-basicservices-request-uploadtask-i.md#delete)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [delete](arkts-basicservices-request-uploadtask-i.md#delete)()

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## restore

```TypeScript
restore(callback: AsyncCallback<boolean>): void
```

重新启动被暂停的下载任务，使用callback异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## restore

```TypeScript
restore(): Promise<boolean>
```

重新启动被暂停的下载任务，使用Promise异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

重新启动被暂停的下载任务，使用callback异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [restore](#restore)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [restore](#restore)(callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## resume

```TypeScript
resume(): Promise<void>
```

重新启动被暂停的下载任务，使用Promise异步回调。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用[restore](#restore)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [restore](#restore)()

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## suspend

```TypeScript
suspend(callback: AsyncCallback<boolean>): void
```

暂停下载正在运行中的任务，已暂停的任务可被[restore](#restore)恢复，使用callback异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## suspend

```TypeScript
suspend(): Promise<boolean>
```

暂停下载正在运行中的任务，已暂停的任务可被[restore](#restore)恢复，使用Promise异步回调。

> **说明：**&gt;
> 由于不存在401报错场景，在api12中 `401 the parameters check fails` 这个错误码被移除。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
