# upload

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## upload

```TypeScript
function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

创建并启动一个上传任务，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [uploadFile](arkts-basicservices-request-uploadfile-f.md)(context: BaseContext, config: UploadConfig)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## upload

```TypeScript
function upload(config: UploadConfig): Promise<UploadTask>
```

创建并启动一个上传任务，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [uploadFile](arkts-basicservices-request-uploadfile-f.md)(context: BaseContext, config: UploadConfig)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
