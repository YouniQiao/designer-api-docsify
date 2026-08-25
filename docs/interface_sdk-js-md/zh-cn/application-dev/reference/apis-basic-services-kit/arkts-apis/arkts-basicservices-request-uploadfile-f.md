# uploadFile

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## uploadFile

```TypeScript
function uploadFile(context: BaseContext, config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过 on('complete'|'fail') 可获取任务上传时的成功信息或错误信息。

> **说明：**&gt;
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400002](../errorcode-request.md#13400002-文件路径异常) |


## uploadFile

```TypeScript
function uploadFile(context: BaseContext, config: UploadConfig): Promise<UploadTask>
```

创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过 on('complete'|'fail') 可获取任务上传时的成功信息或错误信息。

> **说明：**&gt;
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 9

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400002](../errorcode-request.md#13400002-文件路径异常) |
