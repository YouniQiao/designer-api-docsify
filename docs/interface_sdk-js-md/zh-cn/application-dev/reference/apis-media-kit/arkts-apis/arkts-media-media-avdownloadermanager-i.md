# AVDownloaderManager

离线下载任务管理接口，用于管理媒体资源的离线下载任务，包括创建、暂停、恢复、移除下载任务以及监听下载状态和进度变化事件。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Multimedia.Media.Core

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## addAVDownloadTask

```TypeScript
addAVDownloadTask(source: MediaSource): string
```

根据媒体源创建一个离线下载任务。默认情况下，下载任务仅在Wi-Fi环境下进行，如需在蜂窝网络环境下下载，请先设置allowsCellularAccess为true。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [MediaSource](arkts-media-media-mediasource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## allowsCellularAccess

```TypeScript
allowsCellularAccess(value: boolean): void
```

设置是否允许在蜂窝网络环境下进行下载。默认情况下仅在Wi-Fi环境下进行下载。如果设置不允许在蜂窝网络下载，但网络环境为蜂窝网络环境时，下载任务将暂停等待Wi-Fi环境可用后继续。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## getDownloadTasks

```TypeScript
getDownloadTasks(): Array<string>
```

获取离线下载管理器中的当前所有离线下载任务。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getTaskCacheDirectory

```TypeScript
getTaskCacheDirectory(taskId: string): string
```

获取指定离线下载任务的缓存目录。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## getTaskProgress

```TypeScript
getTaskProgress(taskId: string): number
```

获取指定离线下载任务的下载进度。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## getTaskStatus

```TypeScript
getTaskStatus(taskId: string): AVDownloadTaskState
```

获取指定离线下载任务的状态。状态类型详见AVDownloadTaskState。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AVDownloadTaskState](arkts-media-media-avdownloadtaskstate-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## offProgressChange

```TypeScript
offProgressChange(callback?: OnAVDownloadProgressChangeHandle): void
```

取消注册离线下载任务进度变化的事件监听函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAVDownloadProgressChangeHandle](arkts-media-media-onavdownloadprogresschangehandle-t.md) | 否 |

## offStatusChange

```TypeScript
offStatusChange(callback?: OnAVDownloadTaskStateHandle): void
```

取消注册离线下载任务状态变化的事件监听函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAVDownloadTaskStateHandle](arkts-media-media-onavdownloadtaskstatehandle-t.md) | 否 |

## onProgressChange

```TypeScript
onProgressChange(callback: OnAVDownloadProgressChangeHandle): void
```

注册离线下载任务进度变化的事件监听函数。当下载进度相比上次变化超过1%，且距上次触发时间超过500ms时，触发该事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAVDownloadProgressChangeHandle](arkts-media-media-onavdownloadprogresschangehandle-t.md) | 是 |

## onStatusChange

```TypeScript
onStatusChange(callback: OnAVDownloadTaskStateHandle): void
```

注册离线下载任务状态变化的事件监听函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAVDownloadTaskStateHandle](arkts-media-media-onavdownloadtaskstatehandle-t.md) | 是 |

## pauseDownloadTask

```TypeScript
pauseDownloadTask(taskId?: string): void
```

暂停指定离线下载任务，已下载的部分数据将保留，恢复后可从断点继续下载。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |

## release

```TypeScript
release(): void
```

释放AVDownloaderManager对象使用的资源。调用此方法后，所有下载任务将被停止并移除，不可再通过该实例管理下载任务。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

## removeDownloadTask

```TypeScript
removeDownloadTask(taskId?: string): void
```

从离线下载管理器中移除离线下载任务，移除后该任务将停止下载并从管理器中删除。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |

## resumeDownloadTask

```TypeScript
resumeDownloadTask(taskId?: string): void
```

恢复指定离线下载任务，从上次暂停的断点处继续下载。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [5400108](../errorcode-media.md#5400108-参数超过取值范围) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |

## setRequestTimeout

```TypeScript
setRequestTimeout(timeout: number): void
```

设置HTTP请求的网络超时时间。超时后下载任务将失败。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |
