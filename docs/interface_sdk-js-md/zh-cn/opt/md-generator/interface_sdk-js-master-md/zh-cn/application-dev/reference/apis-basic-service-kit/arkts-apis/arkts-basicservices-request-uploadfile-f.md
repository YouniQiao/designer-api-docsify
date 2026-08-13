# uploadFile

## uploadFile

```TypeScript
function uploadFile(context: BaseContext, config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过 [on('complete'|'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) 可获取任务上传时的成功信息或错误信息。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

<!--Device-request-function uploadFile(context: BaseContext, config: UploadConfig, callback: AsyncCallback<UploadTask>): void--><!--Device-request-function uploadFile(context: BaseContext, config: UploadConfig, callback: AsyncCallback<UploadTask>): void-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [13400002](../../apis-basic-services-kit/errorcode-request.md#13400002-文件路径异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: 'POST',
  files: [{ filename: 'test', name: 'test', uri: 'internal://cache/test.jpg', type: 'image/jpeg' }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: 'name123', value: '123' }],
};
try {
  request.uploadFile(context, uploadConfig, (err: BusinessError, data: request.UploadTask) => {
    if (err) {
      console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    uploadTask = data;
  });
} catch (err) {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
}
```


## uploadFile

```TypeScript
function uploadFile(context: BaseContext, config: UploadConfig): Promise<UploadTask>
```

创建并启动一个上传任务，使用Promise异步回调，支持HTTP协议。通过 [on('complete'|'fail')](arkts-basicservices-request-uploadtask-i.md#on_progress) 可获取任务上传时的成功信息或错误信息。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

<!--Device-request-function uploadFile(context: BaseContext, config: UploadConfig): Promise<UploadTask>--><!--Device-request-function uploadFile(context: BaseContext, config: UploadConfig): Promise<UploadTask>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [13400002](../../apis-basic-services-kit/errorcode-request.md#13400002-文件路径异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: 'POST',
  files: [{ filename: 'test', name: 'test', uri: 'internal://cache/test.jpg', type: 'image/jpeg' }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: 'name123', value: '123' }],
};
try {
  request.uploadFile(context, uploadConfig).then((data: request.UploadTask) => {
    uploadTask = data;
  }).catch((err: BusinessError) => {
    console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
}
```
