# downloadFile

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## downloadFile

```TypeScript
function downloadFile(context: BaseContext, config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void
```

创建并启动一个下载任务，使用callback异步回调，支持HTTP协议。通过 on('complete'|'pause'|'remove') 可获取任务下载时的状态信息，包括任务完成、暂停或移除。通过 on('fail')可获取任务下载时的错误信息。

> **说明：**&gt;
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400001](../errorcode-request.md#13400001-文件操作异常) |
| [13400002](../errorcode-request.md#13400002-文件路径异常) |
| [13400003](../errorcode-request.md#13400003-服务异常) |


## downloadFile

```TypeScript
function downloadFile(context: BaseContext, config: DownloadConfig): Promise<DownloadTask>
```

创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'|'pause'|'remove') 可以获取任务下载时的状态信息，包括任务完成、暂停或移除。通过 on('fail')可以获取任务下载时的错误信息。

> **说明：**&gt;
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400001](../errorcode-request.md#13400001-文件操作异常) |
| [13400002](../errorcode-request.md#13400002-文件路径异常) |
| [13400003](../errorcode-request.md#13400003-服务异常) |
